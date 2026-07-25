# An Algorithmic Lucidity

Pelican static-site conversion of a WordPress blog (zackmdavis.net/blog). Content lives in `content/`, one Markdown file per post/page. `analgorithmiclucidity.WordPress.*.xml` is the original WXR export, used as ground truth when cross-checking whether the WordPress→Markdown conversion silently lost or corrupted formatting.

## Deployment

The blog is a DigitalOcean VPS. `provisioning/` holds the server's config, but nothing self-installs. Either `scp` straight to `root@` at the destination path, or `scp` to `blogmistress@zackmdavis.net:~/` and `install` into place on the box — the latter sets the mode explicitly instead of inheriting the repo file's, and leaves a staging copy to diff against what's live before overwriting it.

| repo | server |
| --- | --- |
| `nginx_siteconf` | `/etc/nginx/sites-available/an_algorithmic_lucidity` (symlinked from `sites-enabled/`) |
| `conf.d/*.conf` | `/etc/nginx/conf.d/` (included from `nginx.conf`'s `http{}`; `log_format` and `map` are only valid at that scope) |
| `gitweb.conf` | `/etc/gitweb.conf` (pinned by `fastcgi_param GITWEB_CONFIG` in `nginx_siteconf`) |
| `ai_bot_digest.py` | `/usr/local/bin/ai_bot_digest` |
| `systemd/*` | `/etc/systemd/system/` |
| `pelican_scheduler.py` | symlinked as the bare repo's `hooks/post-receive` |

After nginx edits, `nginx -t && systemctl reload nginx` — `nginx -t` catches a `conf.d` file that didn't land, since the site config references things defined there. After unit edits, `systemctl daemon-reload` **and** `systemctl restart ai-bot-digest.timer`; a daemon-reload alone leaves an already-scheduled timer on its old schedule.

**Server state not tracked here:** `/etc/mime.types` (OS-managed) has a hand-added `text/markdown md;` line. Without it `.md` serves as `application/octet-stream`, and gitweb's mimetype lookup reads this file too.

The access log uses the `combined_extended` format from `conf.d/common_log_formats.conf` — stock `combined` plus `"$host" "$sent_http_content_type"`. The Content-Type field is what makes a Markdown content negotiation visible at all (`try_files` picks a different file without rewriting `$request`, so the request line is identical either way). `ai_bot_digest.py` parses both formats, treating the extras as optional, so rotated pre-change archives still work.

## Known gotchas

### Bare `$` math delimiter collides with currency amounts

We use the `pelican-render-math` plugin (`PLUGINS = ['render_math']` in `pelicanconf.py`) for MathJax. Its inline-math regex is hardcoded to bare `$...$` with **no way to disable it** (source: `.venv/lib/python3.12/site-packages/pelican/plugins/render_math/pelican_mathjax_markdown_extension.py`). If a paragraph contains two or more literal `$` (e.g. two dollar amounts), they can pair up and get swallowed into a bogus math span, corrupting the render. Backslash-escaping (`\$`) does *not* help — the plugin's pattern runs at higher Markdown inline-pattern priority (185) than the `escape` pattern (180) specifically so real LaTeX commands survive, which as a side effect means it never sees escape sequences at all.

Current fix, applied case-by-case as encountered: replace one or more of the conflicting `$` with the HTML entity `&#36;` (bypasses the regex entirely since it isn't a literal `$` character in the raw source). Confirmed no other post in the corpus has this problem as of 2026-07-14 (see `content/2016/joined.md` for the one confirmed instance).

**If this keeps recurring and the per-instance entity patching becomes annoying**: the real fix is switching to the `python-markdown-math` package (`mdx_math`) instead, configured with `enable_dollar_delimiter: False` (that's the default). Unlike `pelican-render-math`, it makes bare `$` a plain, forever-ordinary character and requires `\(...\)` for inline math instead — which is also MathJax's own actual default behavior (bare `$` inline math is opt-in upstream, precisely to avoid currency collisions; this Pelican plugin skipped that safety rail). Confirmed via its source (`enable_dollar_delimiter` default `False`, pattern priority 185, same escape-priority trick).

Migration cost if we ever do this: (1) swap the plugin and reimplement the "only inject the MathJax `<script>` tag on pages that actually contain math" auto-detection ourselves, since that's Pelican-specific glue `pelican-render-math` provides that the plain extension doesn't; (2) convert every existing inline `$...$` math span across the corpus to `\(...\)` (display math `$$...$$` is already unambiguous and can stay as-is); (3) revert the `&#36;` entities back to plain `$`. Not done as of 2026-07-14 — decided the entity workaround is fine for now since it's a single confirmed instance.

### Automatic email-autolinking of `<...>` disabled

Python-Markdown's core `automail` inline pattern (priority 110, baked into every `Markdown` instance regardless of extensions) greedily swallows any bare `<foo@bar>` into a `mailto:` autolink as one atomic match — so `<_zmd@sfsu.edu_>` (used in the Putnam posts to mimic italicized "From:"/"To:" email-client headers) got mangled: underscores baked in literally as part of the (broken) address, angle brackets consumed. Backslash-escaping didn't help either, since `<` isn't in Markdown's default escapable-character list (`>` is, `<` isn't), so `\<` just left a literal backslash in the output.

Fixed permanently (rather than patched per-instance) by deregistering the pattern globally: see `_DisableAutomailExtension` in `pelicanconf.py`, wired in via `MARKDOWN['extensions']`. Confirmed this doesn't affect the separate `autolink` pattern (bare `<http://...>` URLs still auto-link fine). As of 2026-07-14, plain `<_email_>` syntax works correctly everywhere in the corpus with no escaping needed.

### gitweb's charset config knobs don't reach `.md` blobs

gitweb serves raw blobs (`a=blob_plain`) as `text/markdown` — but the charset came out `ISO-8859-1`, mojibaking UTF-8 prose for anything honoring the header. Two obvious fixes both fail: gitweb's own `$default_text_plain_charset` is gated on `$type eq 'text/plain'` (exact match, so `text/markdown` never qualifies), and `$CGI::DEFAULT_CHARSET` is captured when CGI.pm constructs its object, which happens before gitweb evaluates the config. The `ISO-8859-1` is CGI.pm's default, appended to any `text/*` response lacking a charset.

Fixed by wrapping `blob_contenttype` in `provisioning/gitweb.conf` so the type already carries a charset, which makes CGI.pm stand down. That file's comment explains the Perl line by line. It monkey-patches a gitweb internal by name, so a gitweb upgrade that renames `blob_contenttype` would break raw-blob requests loudly — deliberate, since the alternative is silently reverting to mojibake.

### Every deploy 404s the whole site for the length of a build (unfixed)

`publishconf.py` sets `DELETE_OUTPUT_DIRECTORY = True`, so the post-receive hook wipes `output/` and regenerates it from scratch. Until the build finishes, every URL on the blog 404s — confirmed by accident on 2026-07-25, when `.md` mirrors 404'd mid-push and returned 200 a minute later. It hits crawlers as well as people, and some of the 404s in the AI-crawler digests are probably this rather than junk-URL probing.

The fix, when it's worth doing: build into a sibling directory and flip a symlink, so `output/` is always a complete tree — keeping the reason `DELETE_OUTPUT_DIRECTORY` is set (stale files from deleted posts don't linger) without the outage. Touches `SITEGEN_COMMAND` in `provisioning/pelican_scheduler.py`; nginx's `alias` re-resolves symlinks per request, so a flip takes effect immediately with no reload.

### AI-crawler observability

`provisioning/ai_bot_digest.py` runs daily via systemd and files `<site>-<date>.txt` into `/var/log/ai-bot-digest/`, summarizing which crawlers fetched which posts. Its own docstring covers usage and the second-site story. Two structural limits worth knowing before trusting it: User-Agents are forgeable (it quarantines UAs whose traffic is ≥60% 404s as likely impostors), and Google/Apple AI-training use is invisible in principle, since `Google-Extended`/`Applebot-Extended` are robots.txt tokens that no request carries.
