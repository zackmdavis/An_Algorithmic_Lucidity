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
| *(generated)* | `/home/blogmistress/zackmdavis.net/sitemap.xml` and `llms.txt` are **symlinks** into `/home/blogmistress/An_Algorithmic_Lucidity/output/`, which the build regenerates. Created once by hand (`ln -sfn`), never deployed. Untracked server state — recreate both if the box is rebuilt. |

`root_index.html` and `robots.txt` live under the webroot — `root /home/blogmistress/zackmdavis.net` in `nginx_siteconf`, which is also what serves `/docs` and `/media` (and now `sitemap.xml`, though the hook puts that one there). Being inside `blogmistress`'s own home, they're the only two deployable without root; `install` as root would leave them root-owned.

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

**The dominant finding in the digests is the gitweb trap** (from `notes/ai_bot_digests/`). A sample of days, chosen to show the range:

| date | `/blog/source` requests | content pages read |
| --- | --- | --- |
| 2026-07-25 | 21,147 | 500 |
| 2026-07-29 | 61,345 | 234 |
| 2026-08-01 | 102,867 | 265 |
| 2026-08-04 | **312,894** | 138 |
| 2026-08-06 | 107,180 | 151 |

gitweb is **typically ~91% of AI-crawler requests** (median across all 45 digests; range 75–99%). Meta/Facebook AI logged 69,074 requests and **zero** content pages in one day; GPTBot 37,122 requests for one page.

**Corrected 2026-09-10 — there is no crowding-out effect, and an earlier version of this section implied one.** Reading the five rows above as "gitweb up 15× while post-fetching declined" was a selective read; across all 45 digests the two are uncorrelated (Pearson r = **−0.15**, n = 45). Gitweb volume swung ~65× over the window and content-page fetching did not move:

| | median gitweb | median content pages |
| --- | --- | --- |
| Jul 25 – Aug 16 | 66,360 | 297 |
| Aug 17 – Sep 7 | 15,687 | 288 |
| days with gitweb >50k (n=18) | — | 291 |
| days with gitweb <20k (n=20) | — | 287 |

So the trap was **not** consuming crawl budget that would otherwise have gone to posts. The case for `Disallow: /blog/source` rests on it being waste, not on it costing content ingestion — and the load was evidently tolerable. Don't re-derive the crowding-out argument; it was tested and is false.

**Resolved 2026-09-10 — what the trap actually served, measured from the raw access log** (27 Aug – 10 Sep, ~1.2M gitweb requests; `ai_bot_digest.py:313` strips the query string, so this came from `access.log*` directly, extracting the request field with `awk -F'"' '{print $2}'` — grepping whole lines double-counts, because gitweb pages link to each other and the Referer field is full of `/blog/source` URLs too).

The tempting intuition — "crawlers were just walking navigation pages, no real content" — is **false**:

| view class | requests | share |
| --- | --- | --- |
| full text (`blob_plain`, `blob`, `snapshot`) | 520,765 | 43.4% |
| diffs (`blobdiff*`, `commitdiff*`, `patch*`) | 429,563 | 35.8% |
| navigation / metadata | 248,630 | 20.7% |

~79% carried actual file text, ~35k full-text fetches/day. `history` alone was 174,249, i.e. crawlers pulling each file's revision list and then walking it — deliberate enumeration of the SHA cross-product, not incidental link-following.

**But it was worth nothing anyway, and this is the number that matters:**

| | |
| --- | --- |
| distinct `blob_plain` URLs fetched | **213,374** |
| distinct blob versions that have *ever existed* in `content/` | **1,773** |
| redundancy | **~120×** |

Only 66 commits have ever touched `content/` across 632 files, giving 1,773 file-modification events total — 1,600 published-post versions, 113 image versions, **57 draft versions**, 3 other. And `blob_plain?f=X;hb=<commit>` returns X *as of that commit*, so for every commit where X didn't change the response is **byte-identical**. The cross-product doesn't produce "slightly different versions of the corpus"; it produces the same bytes at 120 different URLs.

That matters for the one hypothesis worth taking seriously — that the explosion was *increasing* pretraining weight, since memorization scales with duplicate count. It would need near-dedup to be failing. What it actually needs is exact-match dedup (hash the doc, drop repeats — the cheapest and first step in any pipeline) to be failing. Not a live worry.

**So the unique text gitweb provided that nothing else did was 57 draft blob versions.** The 1,600 published-post versions duplicate the `.md` mirrors, which are served cleanly at stable URLs. 57 is exactly the scale of "a model knows a few stray things about me from drafts" — the observation that started this whole thread. The mechanism was real and that small.

**Don't reopen `/blog/source` hoping for pretraining weight.** It was measured; there isn't any.

Incidentals from the same measurement: **`content/images` was the single largest `blob_plain` category (61,562 fetches, 113 distinct files)** — binaries, no prose value, probably most of the bandwidth. And `notes/` didn't crack the top 20 (<992 fetches), largely because most of it is untracked and so was never in gitweb at all.

This was permitted behavior, not abuse: through 2026-09-09 `provisioning/robots.txt` was `Allow: /` with no `Disallow` lines at all, and git history is a near-infinite URL space (commits × files × view modes × blame/diff/raw). **`Disallow: /blog/source` was added and deployed 2026-09-09 (commit `ca16a4b`).** The digests confirm ClaudeBot, Applebot, PerplexityBot, and OAI-SearchBot all reliably fetch robots.txt, so compliant bots should stop; whatever keeps hammering afterward is a much clearer signal about who's ignoring it. Note what this gives up, deliberately: see the next section.

**Settled 2026-09-25 — the trap is closed, and compliance was total.** The `source` bucket was the whole measurement and it has run out:

| digest | `/blog/source` requests |
| --- | --- |
| 2026-09-09 | 190,539 |
| 2026-09-10 | 156,633 |
| 2026-09-11 | 3,236 (Applebot 2,707, Meta 512) |
| 2026-09-12 | 10 (Meta) |
| **09-13 → 09-25** | **0, every day** |

Thirteen consecutive days of exactly zero, across 63 digests total. Every UA that was hammering it stopped, including ones with no particular reputation for politeness. The 09-09/09-10 spike back to ~190k was a last gasp before compliance, not a new phase — don't read it as the rule failing.

**Content-page volume did not move**, which confirms the no-crowding-out finding in the other direction too: median ~250 pages/day before, ~290 after. Closing the trap neither cost nor freed content ingestion. Bursts since (ClaudeBot 367 pages on 09-16, GPTBot 302 on 09-17, PerplexityBot 371 on 09-18 and 322 on 09-25) match the bursty pattern that predates the change (ClaudeBot 491 on 08-07, 421 on 08-27) — **not** a post-`Disallow` reallocation, and it would be easy to misread them as one.

**The digest splits plumbing three ways (2026-09-25).** `classify_path` used to return one `meta` bucket for robots.txt + sitemap.xml + feeds, printed as a single `46× robots/sitemap/feeds`. That fused three questions: robots.txt tells you whether a bot that ignored a `Disallow` had *read the rules* (the DataForSeoBot question), sitemap.xml tells you whether anything consumes the `Sitemap:` directive (an open question, see the ClaudeBot section), and feeds are ordinary polling that was drowning both. They're now `robots` / `sitemap` / `feed`. Redirects are additionally bucketed by the class of the *requested* path, so the line reads `19× redirects (15 feed, 4 content)`.

Two notes. `llms.txt` is deliberately left in `content`, not moved to a plumbing bucket — `content` is the only bucket that prints a path *by name* rather than as a bare count, which is the entire reason we can say it has zero fetches. And this is a reporting change only: the log format is untouched so rotated archives still parse, but **the 63 digests already on disk keep the old aggregate**; getting the breakdown retroactively means re-running over `access.log*`, which reaches back only as far as logrotate kept.

### The bare-feed redirect is a 302, and crawlers re-traverse it forever (unfixed)

`nginx_siteconf:128` answers `/blog/feed/` and `/blog/category/<slug>/feed/` with `return 302 $1/rss/`. A 302 is not cacheable and clients don't rewrite stored subscription URLs on it, so **every poll costs two requests, permanently**. The file's own header comment already called this — it's 302 "only because it hasn't been revisited," and it's "the only redirect here that a client re-traverses on a schedule rather than once." The stuck-cache worry that motivated the 302s is separately documented there as moot (`expires $expires` maps `text/html` to `epoch`, and `return` emits a `text/html` body, so redirects already go out `no-cache`).

What put this on the list: ClaudeBot's redirect count sits at ~35–55/day, flat, **decoupled from how much content it reads** (18–27 pages on those same days), and tracks its meta count almost 1:1 — the signature of a fixed set of URLs re-fetched on a schedule. The contrast on 09-25 is clean: PerplexityBot did 322 pages with 4 meta / 96 redirects (redirects scaling with content — the legacy WordPress-permalink 301 at `nginx_siteconf:137`), ClaudeBot did 18 pages with 49 meta / 35 redirects. Two redirect sources, two signatures.

**Not yet confirmed** — it's a leading explanation, not a settled one (redirects exceed meta on some days, so the 1:1 isn't exact). The digest's new redirect breakdown makes it readable directly: a ClaudeBot line reading `Nx redirects (N feed, ...)` confirms it. Confirm first, then make it a 301; don't do both at once, or the measurement disappears with the cause.

### Decided 2026-09-09: gitweb closed, drafts deliberately not exposed

The want recorded here through 2026-08-11 was asymmetric — unpublished writing (`content/drafts/`, `notes/`) legible to AI crawlers is a *feature*, the every-file-at-every-SHA explosion is waste — and the plan was to separate them. That was reconsidered and dropped. What was decided, and why, so it isn't re-litigated from the old premise:

**gitweb was probably the mechanism that worked, and closing it is a real cost.** The evidence that unpublished writing reaches models comes from the *other* blog: `Ultimately_Untrue_Thought` has **no robots.txt at all**, serves gitweb at `/source` over a repo containing 73 drafts and 51 `notes/` files, and links to none of them. There is no other plausible ingestion route, so gitweb crawling almost certainly *is* the surface. Treating "drafts crawlable" and "SHA cross-product crawlable" as separable is true in principle but describes machinery that was never built; in practice they were the same mechanism. `Disallow: /blog/source` therefore switches off the thing that produced the impressive result — accepted knowingly, not overlooked. **Quantified 2026-09-10 (see the section above): the cost is 57 draft blob versions.** Everything else gitweb served was byte-identical duplicates of published posts already available as `.md` mirrors. The mechanism was real; the magnitude was tiny.

**Drafts were left out of the sitemap on purpose.** A draft and its published version live at different URLs (`drafts/<slug>.html` vs `YYYY/Mon/<slug>/`), and the draft URL 404s once the file leaves `content/drafts/`. So a crawler that captured a draft has no live page to revisit and no canonical link to the finished piece: the superseded take persists uncorrected, in a way an edited published post at a stable URL never does. That matters disproportionately for a corpus where changing one's mind in public is a recurring move. Checked at the time: every draft had been touched within the previous month, so there was no safe subset of abandoned ones. The deciding asymmetry is that drafts can be added to the sitemap any time, whereas nothing can un-train a captured draft — and the observed value was thin (the models' impressive knowledge is overwhelmingly of *published* work; draft hits were strays).

**`notes/` is consequently dark to crawlers**, since gitweb was its only URL — but this mattered far less than this section originally implied. The 2026-09-10 measurement above puts `notes/` below 992 `blob_plain` fetches over two weeks, outside the top 20 paths, largely because most of `notes/` is untracked and so was never in gitweb to begin with. If it's ever genuinely wanted, don't reopen gitweb — symlink or copy an explicit allowlist of files under the webroot (`/docs` and `/media` are already served that way with `autoindex on`, and `sitemap.xml`/`llms.txt` are symlinked there), which is path-shaped and stays deliberate about what's exposed.

**What does work, if this is revisited: links.** The site has run the experiment. The `.md` mirrors are fetched heavily and are linked from HTML (`theme/templates/article.html`, `includes/post_card.html`); `llms.txt` is a root convention that nothing links to and has **zero fetches across all 45 digests** (2026-07-25 → 09-07). Convention alone gets nothing crawled here. The Diary links added to `provisioning/root_index.html` in `186d3f3` are the right shape for this. A sitemap is the exception that proves it — it's the one mechanism designed to advertise unlinked URLs — but note that its reliable consumers are *search* crawlers; no digest evidence shows an AI training crawler following a `Sitemap:` line.

**Don't expect politeness headers to help with load.** gitweb already emits `<meta name="robots" content="index, nofollow"/>` on every HTML page (`/usr/share/gitweb/gitweb.cgi:4214`) and `nginx_siteconf` already sets `X-Robots-Tag: noindex` on the location — and the trap still drew 312,894 requests in a day. `nofollow` is about endorsement, not crawl budget; `blob_plain` responses aren't HTML and carry no meta tag at all; `X-Robots-Tag` governs indexing rather than fetching. **robots.txt is the only lever here that reduces requests.**

**Measurement gotcha:** `ai_bot_digest.py:313` drops the query string before counting, so the digests never could tell which gitweb *views* were being hammered — only that `/blog/source` totals fell. Moot now that the bucket is flat zero; if query-string bucketing by `a=` is ever wanted for something else, that's the line to change. Confirming *which* bots ignore the `Disallow` means grepping the raw access log, or teaching the digest to bucket by `a=` parameter.

### robots.txt: a blank line or a rule order can silently void the whole file

Two footguns, both of which make rules *look* present while doing nothing, and both hit while adding `Disallow: /blog/source` on 2026-09-09 (caught only by testing the file, not by reading it):

* **A blank line ends the `User-Agent` group.** Every `Disallow`/`Allow` after it is discarded — they're only recorded while the parser is inside a group. Putting the new `Disallow` in its own visually-tidy stanza below `Allow: /` meant *no rule applied at all*. Keep the rules flush against `User-Agent:` with no blank line anywhere among them.
* **`Disallow` must come before `Allow: /`.** Longest-match precedence (`/blog/source` beating `/`) is Google's rule and RFC 9309's, but it is *not* universal: Python's `urllib.robotparser` takes the **first** matching rule, so `Allow: /` first leaves gitweb fully allowed. Disallow-first is correct under both semantics, so it's the portable order.

`Sitemap:` is exempt from all of this — the sitemaps.org protocol makes it independent of the user-agent line ("it doesn't matter where you place it in your file"), and stdlib honors that explicitly, so the trailing stanza is fine.

Check changes rather than eyeballing them:

```
python3 -c "import urllib.robotparser as rp; p=rp.RobotFileParser(); \
  p.parse(open('provisioning/robots.txt').read().splitlines()); \
  print(p.site_maps()); print(p.can_fetch('ClaudeBot','https://zackmdavis.net/blog/source'))"
```

### `/docs/diary` is open to AI crawlers but closed to search (2026-09-09)

The diaries are linked from `provisioning/root_index.html` (commit `186d3f3`), so they're discoverable now. They discuss a named third party at length, and the concern is specifically **her name becoming a search key** — someone googling her and landing here. `robots.txt` therefore blocks `/docs/diary` in the `*` group and allows it in a named group listing the AI training/on-demand crawlers.

**Why an allowlist rather than blocking Googlebot and Bingbot.** A crawler obeys exactly one group — the most specific `User-agent` match — and ignores every other group including `*`, so a named group must restate every rule it needs (which is why `Disallow: /blog/source` appears twice). Given that, enumerating the crawlers to *permit* is bounded and stable; enumerating search bots to *deny* is unbounded, and half the entries in `ai_bot_digest.py`'s `BOTS` are ambiguous between search and AI (PetalBot, Amazonbot, YouBot).

**The line: pretraining crawlers only.** The diary is online to increase pretraining footprint, nothing else — so on-demand fetchers and answer-engine indexes are both out, even where the same vendor's training crawler is in. Excluded for that reason: `ChatGPT-User`, `Claude-User`, `Perplexity-User` and `meta-externalfetcher` (on-demand, fetched because a human asked); `OAI-SearchBot`, `Claude-SearchBot` and `PerplexityBot` (build queryable indexes — someone can type her name into Perplexity exactly as into Google). Watch out for `ai_bot_digest.py:197`, which lumps `Meta-ExternalAgent`, `meta-externalfetcher` and `FacebookBot` under one "Meta / Facebook AI" label; only the first and third are training crawlers.

**`GoogleOther` is in the group but does little.** It's Google's non-search R&D crawler, so it's not a search-key risk — but Gemini training rides on `Googlebot` fetches governed by the `Google-Extended` token, and Googlebot is blocked from the diary by the `*` group. So Google-side training is blocked regardless; `GoogleOther` doesn't recover it. Same shape for Apple: `Applebot` is blocked, so Apple Intelligence is too.

**What this cannot do:**

* **Google and Apple are all-or-nothing.** `Google-Extended`/`Applebot-Extended` are robots.txt *tokens* governing what a vendor may do with bytes its ordinary crawler already fetched — there is no separate training fetch. So blocking Googlebot from the diary also blocks Gemini training, and Applebot likewise for Apple Intelligence. Accepted: the search-key risk is the one being managed.
* **`Disallow` is not `noindex`.** Google can list a `Disallow`ed URL without content, from links and anchor text alone. That's harmless here only because the URLs and their link text are both opaque (`Diary_01B.md`, "Diary 1B") — a URL-only listing leaks no name. If a diary is ever given a descriptive filename or link text, this stops being true and `X-Robots-Tag: noindex` on a `location /docs/diary` block becomes the right instrument (it works on `.md`, being an HTTP header).
* **robots.txt is voluntary**, so this is no protection against scrapers that ignore it, and none at all against anyone who has the URL.

**Measured 2026-09-25 (63 digests, 07-25 → 09-25). The allowlist works; the diary is being ingested; and the UA-allowlist design has one real hole.**

*What reads the diaries.* 1A went up 2026-08-05 (`d727656`); 1B–2D around 09-06, committed 09-09 (`186d3f3`). Discovery was fast and link-driven:

| crawler | behaviour |
| --- | --- |
| GPTBot | found all 8 within a day; full sweeps 09-07, 09-09, 09-18, 09-19, then **stopped** — on 09-22 it fetched `/` and five posts and did not follow. Four sweeps and done, the normal shape for a crawler that has captured a small static set. |
| Bytespider | took over from 09-12; full 8-file sweeps 09-24 and 09-25 with repeats (`01D`×4). Now the heaviest consumer. |
| Amazonbot, GoogleOther, YouBot | one-off partial sweeps, all pre-`Disallow`. |
| ClaudeBot | **never** — see the section below, it's the interesting case. |

So the mechanism works and the vendor changed hands. Don't conclude from GPTBot going quiet that it broke.

*The exclusions hold where it matters most.* PerplexityBot became the **largest content crawler on the site** (777 requests/371 pages on 09-18, 769/322 on 09-25) and fetched **zero** diaries. It's excluded on purpose — a queryable index is the search-key risk — and it complies. That is the design working on exactly the bot it was written for.

*Two crawlers ignored the `Disallow`*, both search-flavoured and both outside the allowlist: **DataForSeoBot** took all 8 on 09-11, having fetched robots/sitemap URLs the same day (an SEO backlink/SERP vendor — precisely the search-key exposure the rule exists to prevent); **PetalBot** took `01D` on 09-17, one hit, plausibly a stale queue entry. robots.txt is voluntary and this is what that costs.

*The hole: a UA allowlist grants access to anyone who types the string.* Every UA in the named group has been forged on this site, counted from the digests' own quarantine sections — GPTBot 17 days, ClaudeBot 6, Bytespider 5, CCBot 4, cohere-ai 4. **`cohere-ai` has never made a legitimate request here; it appears only as a forgery** — that entry is pure attack surface with no observed benefit, and should be dropped.

*And the URL has leaked.* On 09-24 a spoofed-UA scanner (forging GPTBot, 86% 404, quarantined by the ≥60% heuristic) probed `/docs/diary/Diary_01A.md` **by name**, in a wordlist between `/config.py` and `/env.json`, alongside `/.env.production` and `/actuator/heapdump`. First diary probe in 63 digests. Only `01A` — the longest-exposed one — so whatever fed that list predates the 09-06 batch. **Watch for `01B`–`02D` appearing in scanner wordlists; that would date the leak.** This doesn't defeat anything robots.txt was doing (the third bullet above already says it's no protection against scrapers), but it moves that from hypothetical to observed.

**The unresolved tension, recorded deliberately:** this protects against the *reversible* harm (a search listing can be delisted and decays) while accepting the *irreversible* one (training ingestion has no removal mechanism) — the inverse of the reasoning applied to drafts in the section above. The counterweight is that search is the higher-*probability* path (people google names; they less often interrogate models about private individuals) and model memorization of a low-frequency name is uncertain. Redaction is the only measure that covers both paths plus non-compliant scrapers, and remains an open option.

### ClaudeBot doesn't follow the root page's links; GPTBot does (open, 2026-09-25)

ClaudeBot has fetched `/` — `root_index.html`, the page carrying the Diary links — on essentially every digest day since the links went up, and has **never** followed one to `1B`–`2D`. Its only diary hits ever are `Diary_01A` on 08-07 and 09-02. GPTBot, given the same page, fetches `/` and then all eight files in a single 10-request burst. Two crawlers, one page, opposite behaviour.

It is not a coverage problem: ClaudeBot is one of the busiest crawlers here (120–580 requests/day, up to 367 content pages) and it is not being blocked.

**Ruled out:**

* **robots.txt.** Parsed the live file: the multi-`User-Agent` group resolves to one entry carrying all eight agents, and ClaudeBot is granted `/docs/diary` (`can_fetch` → `True`). The consecutive-`User-Agent` construct is explicitly blessed by RFC 9309 §2.2.1. Can't rule out Anthropic's parser differing, but it's a weak suspect. Use the check command in the robots.txt section above to re-verify after any edit.
* **The deploy 404 window.** `/docs/diary` is served from the webroot, not from `output/`, so `DELETE_OUTPUT_DIRECTORY` never makes those URLs 404. Unrelated.
* **Hidden links — weakened, not dead.** `p.quiet { display: none }` in `root_index.html` is a textbook hidden-link spam signal, but it has been there since `d727656` (08-05) and ClaudeBot followed the hidden `01A` link twice anyway. So `display:none` isn't a hard blocker for it. Still plausible as a soft demotion that a bigger link set tipped over — test it last, since un-hiding is the one fix with a cost to you.

**Leading hypothesis: ClaudeBot works from the sitemap and near-exclusively inside `/blog/`.** Supporting fact, and it's a strong one: **ClaudeBot has fetched exactly two `/docs/` URLs in 63 digests**, both `Diary_01A`, and **zero** PDFs — while Applebot, Bytespider, PetalBot and ChatGPT-User pull `/docs/*.pdf` routinely. (Verified this isn't a bucketing artifact: `.pdf` is not in `_ASSET_EXT` and `_ASSET_PREFIXES` are all under `/blog/`, so `/docs/*.pdf` classifies as `content` and would print by name.) The sitemap lists the 495 published posts and nothing else, so the diaries are not in its work queue.

**Correction, so it isn't written down as fact:** an earlier reading had ClaudeBot's crawl "changing shape on exactly the day `sitemap.xml` went live" — median pages/day 5 → 28, meta 20 → 46, redirects 5 → 51. The step is real but the timing is wrong. It appears in the **09-09 digest**, whose window ends `2026-09-09 08:00 UTC`; `fa79060` was committed `2026-09-09T20:42:51-07:00` = **09-10 03:42 UTC**, ~20 hours later. The behaviour change *precedes* the sitemap, so the sitemap didn't cause it — the apparent correlation was an artifact of a 30-day/13-day split boundary landing at 09-09. The hypothesis now rests on the structural `/docs/`-avoidance above, not on that step.

**What to try, cheapest first:**

1. **Measure before changing anything** — `zgrep -h ClaudeBot /var/log/nginx/access.log* | awk -F'"' '{print $2}' | awk '{print $2}' | sort | uniq -c | sort -rn | head -40`. The digest can now split robots/sitemap/feeds (see below), so from here on this is readable off the digests instead.
2. **Add the diaries to the sitemap.** Highest prior, and it tests the never-tested claim that no AI training crawler follows a `Sitemap:` line. Two things to decide deliberately: the Pelican-generated file sits at `/blog/sitemap.xml`, where `/docs/diary/*` is out of sitemaps.org scope (the webroot symlink at `/` is in scope), so either accept that or emit a separate root sitemap. And **don't conflate this with the drafts decision** — drafts are excluded because their URLs 404 once the file moves, stranding a superseded take; the diaries are at stable webroot URLs that don't move, so that reasoning doesn't transfer. Added search risk is near-zero: `*` still `Disallow`s the path, and the URL-only-listing caveat holds because `Diary_01B.md` / "Diary 1B" are opaque.
3. **Link them from inside `/blog/`**, where ClaudeBot actually spends its budget. Orthogonal to whether the sitemap theory is right.
4. **Drop `display: none`** — only if 2 and 3 fail.

### Sitemap (built 2026-09-09)

`_write_sitemap` in `pelicanconf.py` emits `sitemap.xml` on the `finalized` signal, listing the 495 published posts and nothing else — no drafts (above), no `.md` mirrors (same content at a second URL; already reachable via `<link rel="alternate">`), no tag/category/archive indexes (navigation, not content). Justified independently of any crawler-ingestion question: a sitemap is worth having for ordinary search discovery.

* **Placement — two rules that get conflated.** *Scope*: the sitemaps.org protocol bounds a sitemap by its own location, so one at `/blog/sitemap.xml` may only list URLs under `/blog/`, which every URL here satisfies anyway. *Discovery*: crawlers look for `/sitemap.xml` at the true domain root. Both are handled outside `pelicanconf.py` — the deploy hook installs a copy at the webroot, and `robots.txt` carries a `Sitemap:` line naming it. This is a **genuine difference from `llms.txt`**, which has no equivalent of the `Sitemap:` directive: nothing at the root can redirect attention to a copy elsewhere, so for that file the physical move is the whole fix rather than a redundancy.
* **The webroot copy is a symlink, not a deploy step.** An earlier version had `pelican_scheduler.py` `install`-ing the file on every build; that was replaced by a one-time symlink, which is always current, keeps the hook out of the webroot, and needs no write permission there. It also sidesteps the hook-staleness trap below. The one caveat: `DELETE_OUTPUT_DIRECTORY = True` wipes `output/` at the start of each build, so the symlink dangles until the build finishes — during which the whole site is 404ing anyway (see the deploy-window gotcha above). The `rsync --checksum --delete` fix for that window would eliminate this too.
* **`llms.txt` got the same treatment** on 2026-09-10 — see its section below.
* **`lastmod` comes from git, not from the post's `Date:` header.** Publication date was simply wrong: **491 of 495 posts have been edited since publication** (the WordPress import on 2026-07-15, then the root-relative link sweep on 2026-08-07), so `Date:` understated every one of them. `Modified:` in the post header would be the tidy fix but requires remembering it on every edit forever; git already knows. `_git_last_modified` in `pelicanconf.py` runs **one** `git log --name-only` over `content/` and maps source path → latest commit date.
    * **One pass, not one call per file** — measured at ~35 ms for the whole corpus versus ~1.9 s for per-file calls, i.e. 1% of build time rather than half of it. Don't "simplify" it into a loop of `git log -1`.
    * Commit lines are prefixed with a **NUL sentinel** (`--format=%x00%cI`) because NUL is the one byte a path can't contain, so commit lines and filenames are never confused.
    * On any failure — not a git checkout, shallow clone, no `git` binary — it returns `{}` and the sitemap **omits** `<lastmod>` for every URL. That's legal (it's optional per-URL) and better than inventing a date. Same for an individual uncommitted post in a local build.
    * The resulting dates cluster hard (381 posts on 2026-07-15) because that's genuinely when those files last changed. That's a one-time historical artifact, not an ongoing defect: from here on, editing one post moves exactly that post's date. A future bulk rewrite of the corpus *will* bump everything again, and that will be accurate.
    * `DEFAULT_DATE = 'fs'` is *not* a shortcut to this — it would overwrite every post's publication date too.
* **A sitemap can't override robots.txt.** A `Disallow`ed URL isn't fetched just because it's listed — which is why nothing under `/blog/source` appears here.

### `llms.txt` placement fixed by symlink (2026-09-10)

`_write_llms_txt` emits into the Pelican output tree, so it lands at `/blog/llms.txt` — but `llms.txt` is a domain-root convention like `robots.txt`, and a crawler that goes looking checks `zackmdavis.net/llms.txt`. **Fixed the same way as `sitemap.xml`:** `/home/blogmistress/zackmdavis.net/llms.txt` is a symlink to `output/llms.txt`. Verified live (200, `text/plain; charset=utf-8`). No code change was needed — `_canonical_url` already builds absolute `https://zackmdavis.net/blog/...` links, so the file works unmodified from the root.

Unlike `sitemap.xml`, there's no `Sitemap:`-style directive that could have pointed at a copy elsewhere, so relocation was the entire fix rather than a redundancy.

**What this does and doesn't settle.** It had **zero fetches** across all 45 digests (2026-07-25 → 09-07) while it sat at `/blog/llms.txt`, but that was consistent with two different explanations — nobody looks for `llms.txt`, or nobody could find this one. Only the second is now excluded, so the digests finally measure the interesting question.

**Still zero as of 2026-09-25** — 63 digests, and 15 days at the domain root where the convention says to look. That's long enough that "the convention is dead here" is the answer rather than the hypothesis. Compare the link-driven result in the ClaudeBot section: GPTBot found eight unlinked-from-anywhere-else diary files within a day of a link appearing on `root_index.html`. **Links get crawled here; root-level conventions do not.** Keep watching, but don't spend effort on `llms.txt` content.

Note the heavy `.md` fetching in those digests is *not* evidence llms.txt works: the mirrors are reachable from the HTML anyway, via the `<link rel="alternate">` in `theme/templates/article.html` and the visible "Markdown source" link in `theme/templates/includes/post_card.html`.

Same caveat as the sitemap symlink: `DELETE_OUTPUT_DIRECTORY = True` wipes `output/` at the start of each build, so both links dangle until it finishes — during which the whole site 404s anyway.

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
