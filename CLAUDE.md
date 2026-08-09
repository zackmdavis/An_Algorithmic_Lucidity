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
| `root_index.html` | `/home/blogmistress/zackmdavis.net/index.html` — **renamed on the way over**; scp'ing it under its repo name lands a dead file beside the real one and changes nothing visible |
| `robots.txt` | `/home/blogmistress/zackmdavis.net/robots.txt` (the true domain root, not `/blog` — see the `STATIC_PATHS` comment in `pelicanconf.py` for why Pelican deliberately doesn't generate it) |

The last two live under the webroot — `root /home/blogmistress/zackmdavis.net` in `nginx_siteconf`, which is also what serves `/docs` and `/media`. Being inside `blogmistress`'s own home, they're the only two deployable without root; `install` as root would leave them root-owned.

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

**Alternative worth preferring — `rsync -a --checksum --delete newbuild/ output/`.** Same `SITEGEN_COMMAND`, and it closes the window without any symlink machinery: `--checksum` compares content rather than timestamps, so files whose bytes didn't change are left physically untouched, `--delete` still reaps files for deleted posts, and `output/` is never in a wiped state. It also fixes a second, subtler effect of the wipe: nginx derives static-file ETags from **mtime + size** (verified live — `etag: "6a736bfe-f07a"` decodes to the same timestamp as `last-modified`), and a full regenerate stamps every file with a fresh mtime, so *every* page's ETag changes on *every* deploy even when its bytes are identical. Any client holding a cached copy gets a failed revalidation and a full re-download.

Priority note: that ETag effect sounds worse than it measures. Across 2026-07-25→08-06 the digests record **35 total 304 revalidations against ~1M requests** — near-nobody sends conditional requests here, so almost nothing is actually paying the invalidation cost. Justify this change on the 404 window, which hits human readers; treat the ETag hygiene as a free side effect, not a reason.

### AI-crawler observability

`provisioning/ai_bot_digest.py` runs daily via systemd and files `<site>-<date>.txt` into `/var/log/ai-bot-digest/`, summarizing which crawlers fetched which posts. Its own docstring covers usage and the second-site story. Two structural limits worth knowing before trusting it: User-Agents are forgeable (it quarantines UAs whose traffic is ≥60% 404s as likely impostors), and Google/Apple AI-training use is invisible in principle, since `Google-Extended`/`Applebot-Extended` are robots.txt tokens that no request carries.

**The dominant finding in the digests so far is the gitweb trap, and it's growing fast** (noted 2026-08-07, from `notes/ai_bot_digests/`):

| date | `/blog/source` requests | content pages read |
| --- | --- | --- |
| 2026-07-25 | 21,147 | 500 |
| 2026-07-29 | 61,345 | 234 |
| 2026-08-01 | 102,867 | 265 |
| 2026-08-04 | **312,894** | 138 |
| 2026-08-06 | 107,180 | 151 |

Roughly **99.9% of AI-crawler traffic is the gitweb interface**, up ~15× in twelve days, while actual fetching of posts *declined* over the same window. Meta/Facebook AI logged 69,074 requests and **zero** content pages in one day; GPTBot 37,122 requests for one page.

This is permitted behavior, not abuse: `provisioning/robots.txt` is `Allow: /` with **no `Disallow` lines at all**, and git history is a near-infinite URL space (commits × files × view modes × blame/diff/raw). The cheap experiment is `Disallow: /blog/source` — the digests confirm ClaudeBot, Applebot, PerplexityBot, and OAI-SearchBot all reliably fetch robots.txt, so compliant bots would stop; whatever keeps hammering afterward is then a much clearer signal about who's ignoring it. Not done as of 2026-08-07. Weigh it against actually wanting the git history publicly crawlable, which is a real thing to want and the reason it's exposed.

### `llms.txt` is generated where nothing will find it (unfixed, low priority)

`_write_llms_txt` in `pelicanconf.py` emits it into the Pelican output tree, so it lands at `/blog/llms.txt` — but `llms.txt` is a domain-root convention like `robots.txt`, so a crawler that goes looking checks `zackmdavis.net/llms.txt` and gets a 404. Nothing links to the real one either, from `robots.txt` or from any page. It has **zero fetches** across every digest in `notes/ai_bot_digests/` (2026-07-25 through 2026-08-03) — the file is currently dead weight.

Note this means the heavy `.md` fetching visible in those digests is *not* evidence llms.txt works: the mirrors are reachable from the HTML anyway, via the `<link rel="alternate">` in `theme/templates/article.html` and the visible "Markdown source" link in `theme/templates/includes/post_card.html`.

The fix is placement, not content — `_canonical_url` already builds absolute `https://zackmdavis.net/blog/...` links, so a copy served from the webroot works unmodified. It's the same problem `STATIC_PATHS` in `pelicanconf.py` already solves for `robots.txt` by deploying that standalone, but `llms.txt` is build-generated, so it needs copying out of `output/` after each build (`provisioning/pelican_scheduler.py`) rather than a one-time `scp`. While in there: there's no `sitemap.xml` at all and no `Sitemap:` line in `robots.txt`, which is the same missing-machine-discovery-surface problem — robots.txt *is* reliably fetched (ClaudeBot, Applebot, PerplexityBot, OAI-SearchBot all hit it), so it's the better hook of the two.

### Internal links are root-relative on purpose — don't "fix" them

Every internal link in `content/` is `/blog/YYYY/Mon/slug/`. This is deliberate and matches the convention on the other blog: root-relative links survive a scheme change, work in local builds where `SITEURL` is `''`, and don't bake the hostname into ~500 source files. They are **not** an oversight to be absolutized.

Where absolute URLs are genuinely needed — the `.md` mirrors, which exist to be read detached from the site — `_absolutize_site_links` in `pelicanconf.py` converts them at build time, guarded on `SITEURL` being set. Add destinations there, not in the source.

Before 2026-08-07 these were absolute `http://zackmdavis.net/blog/YYYY/MM/slug/`, resolving only via the legacy-permalink redirect in `nginx_siteconf`. That redirect still exists for inbound links from elsewhere, but nothing in the corpus depends on it now.

## Less Wrong cross-posting (designed, not built — nothing decided)

Two related wants, neither implemented: a "Discussion on Less Wrong" link on each post, and a script that rewrites internal blog links to their LW equivalents when preparing a linkpost. Findings below so this doesn't get re-derived.

**Two directions, don't conflate them.** 46 posts carry `[(originally published at _Less Wrong_)](url)` as the first body line — that's the *old* relation, LW-canonical and mirrored here. New posts are the reverse: canonical here, linkposted to LW, so they want different wording ("Discussion on Less Wrong"). Backfilling the 46 into whatever mechanism gets chosen is mechanical but separate.

**Where the LW URL should live — leaning sidecar, undecided.** The obvious answer is a `Lesswrong:` line in the post header; Pelican supports arbitrary metadata with no config change (`readers.py:320` lowercases the key, `:341` returns a single-line value as a string, `:117` passes unknown names through), exposing `article.lesswrong`. The problem is sequencing: the LW URL doesn't exist until *after* publishing, so post-header metadata forces a second commit per post that touches the post file. A sidecar `slug → LW URL` JSON keeps the publish commit clean and lets updates batch — which matters beyond tidiness, since every push triggers a full rebuild and the site-wide 404 window described above. Read it once in `pelicanconf.py` and attach `article.lesswrong` the way `_prepare_markdown_mirrors` attaches `article.markdown_url`; warn on a key matching no post, since the sidecar loses the typo-safety of co-located metadata. Slugs are verified unique corpus-wide, so slug is a safe key. Third option: linkpost *before* pushing (the blog URL is predictable from date and filename), publish once with the field already filled — costs a window where the LW post points at a 404.

**Gotcha either way:** `_write_markdown_mirrors` restates a **hardcoded** field list (Author, date, Category, Tags, Canonical URL), so a new field silently vanishes from the `.md` mirrors — i.e. the artifact that exists for LLM legibility — unless added there too. It also pipes the body through `_absolutize_site_links`, so anything else that reuses post bodies for off-site consumption wants the same treatment.

**Link-rewriting script.** Key on slug, not whole-URL matching. Since 2026-08-07 the corpus is uniform — every internal link is root-relative `/blog/YYYY/Mon/slug/` (293 of them: 287 in published posts, 6 in drafts), with no absolute or legacy-numeric-month forms left, so the script only has one input shape to parse. Dispositions: mapped post → LW URL; unmapped post → absolutize; link with a `#fragment` → leave pointing home, since LW has no corresponding anchor and a wrong landing spot beats an off-site one; `/blog/` and `/blog/tag/...` → absolutize only; plus a self-link guard.

`pelicanconf.py`'s `_absolutize_site_links` already implements the absolutizing half (for the `.md` mirrors) — reuse it rather than reimplementing. It encodes the principle worth keeping: **absolutization is a per-destination publishing transform, not a constraint on the source.** An earlier version of this note had that backwards, calling absolute source links "mandatory" on the grounds that root-relative ones resolve against lesswrong.com once pasted — but rewriting links is the script's entire job, so that's the problem it exists to solve, not a reason to avoid the convention.

Make it a standalone CLI with a `--check` mode that reports each link's disposition, *not* a build hook — no reason to grow the job that owns the 404 window.

We should also include, corpus links to the _Less Wrong_ version (from posts that were originally _Less Wrong_ exclusives) should be changed to point to our version.

**Scope boundary.** Link rewriting is the easy half; your Markdown is not LW's Markdown (footnotes `[^name]`, `~~` via `pymdownx.tilde`, `$...$` MathJax, the `&#36;` entity workaround). "Swap the links" is bounded; "paste without touching" is open-ended. Build the first and let the footnotes say whether the second is needed.

**Incidental:** `SOCIAL = ()` in `pelicanconf.py` is dead — the theme references `LINKS` (`theme/templates/base.html:94`) and never `SOCIAL`. It's `pelican-quickstart` scaffolding, and site-global anyway, so it's not a mechanism for per-post links.
