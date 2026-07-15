# An Algorithmic Lucidity

Pelican static-site conversion of a WordPress blog (zackmdavis.net/blog). Content lives in `content/`, one Markdown file per post/page. `analgorithmiclucidity.WordPress.*.xml` is the original WXR export, used as ground truth when cross-checking whether the WordPress→Markdown conversion silently lost or corrupted formatting.

## Known gotchas

### Bare `$` math delimiter collides with currency amounts

We use the `pelican-render-math` plugin (`PLUGINS = ['render_math']` in `pelicanconf.py`) for MathJax. Its inline-math regex is hardcoded to bare `$...$` with **no way to disable it** (source: `.venv/lib/python3.12/site-packages/pelican/plugins/render_math/pelican_mathjax_markdown_extension.py`). If a paragraph contains two or more literal `$` (e.g. two dollar amounts), they can pair up and get swallowed into a bogus math span, corrupting the render. Backslash-escaping (`\$`) does *not* help — the plugin's pattern runs at higher Markdown inline-pattern priority (185) than the `escape` pattern (180) specifically so real LaTeX commands survive, which as a side effect means it never sees escape sequences at all.

Current fix, applied case-by-case as encountered: replace one or more of the conflicting `$` with the HTML entity `&#36;` (bypasses the regex entirely since it isn't a literal `$` character in the raw source). Confirmed no other post in the corpus has this problem as of 2026-07-14 (see `content/2016/joined.md` for the one confirmed instance).

**If this keeps recurring and the per-instance entity patching becomes annoying**: the real fix is switching to the `python-markdown-math` package (`mdx_math`) instead, configured with `enable_dollar_delimiter: False` (that's the default). Unlike `pelican-render-math`, it makes bare `$` a plain, forever-ordinary character and requires `\(...\)` for inline math instead — which is also MathJax's own actual default behavior (bare `$` inline math is opt-in upstream, precisely to avoid currency collisions; this Pelican plugin skipped that safety rail). Confirmed via its source (`enable_dollar_delimiter` default `False`, pattern priority 185, same escape-priority trick).

Migration cost if we ever do this: (1) swap the plugin and reimplement the "only inject the MathJax `<script>` tag on pages that actually contain math" auto-detection ourselves, since that's Pelican-specific glue `pelican-render-math` provides that the plain extension doesn't; (2) convert every existing inline `$...$` math span across the corpus to `\(...\)` (display math `$$...$$` is already unambiguous and can stay as-is); (3) revert the `&#36;` entities back to plain `$`. Not done as of 2026-07-14 — decided the entity workaround is fine for now since it's a single confirmed instance.

### Automatic email-autolinking of `<...>` disabled

Python-Markdown's core `automail` inline pattern (priority 110, baked into every `Markdown` instance regardless of extensions) greedily swallows any bare `<foo@bar>` into a `mailto:` autolink as one atomic match — so `<_zmd@sfsu.edu_>` (used in the Putnam posts to mimic italicized "From:"/"To:" email-client headers) got mangled: underscores baked in literally as part of the (broken) address, angle brackets consumed. Backslash-escaping didn't help either, since `<` isn't in Markdown's default escapable-character list (`>` is, `<` isn't), so `\<` just left a literal backslash in the output.

Fixed permanently (rather than patched per-instance) by deregistering the pattern globally: see `_DisableAutomailExtension` in `pelicanconf.py`, wired in via `MARKDOWN['extensions']`. Confirmed this doesn't affect the separate `autolink` pattern (bare `<http://...>` URLs still auto-link fine). As of 2026-07-14, plain `<_email_>` syntax works correctly everywhere in the corpus with no escaping needed.
