#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Zack M. Davis'
SITENAME = 'An Algorithmic Lucidity'
SITESUBTITLE = 'a blog'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

PLUGINS = ['render_math']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Compass Rose', 'http://benjaminrosshoffman.com/'),
    ('Daniel Lemire', 'http://lemire.me/blog/'),
    ('David R. MacIver', 'http://www.drmaciver.com/'),
    ('Equestria Daily', 'http://www.equestriadaily.com/'),
    ('Julia Evans', 'http://jvns.ca/'),
    ('Rough Diamonds', 'https://sarahconstantin.substack.com/'),
    ('Ribbonfarm', 'http://www.ribbonfarm.com/'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# URL structure - clean paths without dates in URL
FILENAME_METADATA = '(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
ARCHIVES_URL = 'archives'
ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%b}/index.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Markdown extensions
import markdown as _markdown


class _DisableAutomailExtension(_markdown.Extension):
    """Deregister core Markdown's automatic email-autolinking of bare <...>.

    It greedily swallows any <foo@bar> as one atomic match, so writing
    <_zmd@sfsu.edu_> for italicized email addresses in "From:"/"To:"
    lines got mangled (underscores baked in literally, angle brackets
    consumed) instead of becoming an <em> as intended.
    """

    def extendMarkdown(self, md):
        md.inlinePatterns.deregister('automail')


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'guess_lang': False},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'pymdownx.tilde': {'subscript': False},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'extensions': [_DisableAutomailExtension()],
    'output_format': 'html5'
}

# Don't use relative URLs in production - using False for proper absolute URLs
RELATIVE_URLS = False

# Serve favicon.ico at the site root instead of under /extra/. robots.txt is
# NOT generated here on purpose: crawlers only look for robots.txt at the true
# domain root, but this site is served under /blog, so it's deployed as a
# standalone file directly to the real webroot instead (see
# provisioning/robots.txt) -- if Pelican put it in its own output tree, it'd
# end up at /blog/robots.txt, which crawlers won't find.
STATIC_PATHS = ['extra/favicon.ico', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# --- Markdown mirrors + llms.txt, for LLM/agent legibility ---
# Writes a plain .md sibling next to each article's HTML (e.g. 2026/Jun/slug/
# -> 2026/Jun/slug.md) and an llms.txt index at the site root linking to them.
import os as _os
import re as _re
from urllib.parse import urlsplit as _urlsplit, urlunsplit as _urlunsplit
from pelican import signals as _signals

_markdown_mirror_state = {'output_path': None, 'siteurl': '', 'articles': []}


def _prepare_markdown_mirrors(generator):
    _markdown_mirror_state['output_path'] = generator.output_path
    # generator.settings reflects whatever settings file Pelican was
    # actually invoked with (e.g. publishconf.py's absolute SITEURL
    # override) -- unlike the bare module-level SITEURL constant above,
    # which `from pelicanconf import *` only copies into publishconf.py's
    # own namespace at import time, leaving this module's own SITEURL
    # untouched at '' forever. Reading it straight from generator.settings
    # sidesteps that gotcha entirely.
    _markdown_mirror_state['siteurl'] = generator.settings.get('SITEURL', '')
    _markdown_mirror_state['articles'] = []
    for article in generator.articles:
        article.markdown_url = _os.path.dirname(article.save_as) + '.md'
        _markdown_mirror_state['articles'].append(article)


def _canonical_url(path):
    siteurl = _markdown_mirror_state['siteurl']
    return (siteurl + '/' if siteurl else '/') + path


# Internal links in content/ are root-relative (/blog/YYYY/Mon/slug/): they
# survive a scheme change, work in local builds where SITEURL is '', and don't
# bake the hostname into 500 source files. But the .md mirrors exist precisely
# to be read *detached* from the site -- see the metadata comment in
# _write_markdown_mirrors -- and a bare path has nothing to resolve against
# once the body text is separated from the URL it was fetched from, which is
# exactly what chunked ingestion does. So absolutize on the way out: the source
# stays relative, the published artifact carries whole URLs.
#
# Note this is a *per-destination publishing transform*, not a constraint on
# the source; a Less Wrong linkpost would want the same treatment for the same
# reason, and should reuse this rather than push absolute URLs back upstream.
_ROOT_RELATIVE_LINK = _re.compile(r'(\]\()(/(?!/)[^)]*)(\))')


def _absolutize_site_links(body):
    siteurl = _markdown_mirror_state['siteurl']
    if not siteurl:
        return body  # local build: nothing to resolve against, and a
                     # relative link is already right for a local tree
    split = _urlsplit(siteurl)
    if not split.netloc:
        return body
    # Origin only -- SITEURL includes the /blog path prefix, which the links
    # already carry, so joining against SITEURL itself would double it.
    origin = _urlunsplit((split.scheme, split.netloc, '', '', ''))
    return _ROOT_RELATIVE_LINK.sub(
        lambda m: m.group(1) + origin + m.group(2) + m.group(3), body)


def _write_markdown_mirrors(pelican_obj):
    output_path = _markdown_mirror_state['output_path']
    if not output_path:
        return
    for article in _markdown_mirror_state['articles']:
        with open(article.source_path, encoding='utf-8') as f:
            source = f.read()
        _, _, body = source.partition('\n\n')
        body = _absolutize_site_links(body)
        md_abspath = _os.path.join(output_path, article.markdown_url)
        _os.makedirs(_os.path.dirname(md_abspath), exist_ok=True)
        # The source file's own metadata block was just stripped off by the
        # partition() above, so restate it here in a form a reader of the bare
        # .md can use: these mirrors exist precisely to be read detached from
        # the site, where category and tags are the only signal of what
        # neighborhood a post belongs to. Author comes from the AUTHOR setting
        # (no post sets it per-article), and category is always present, but
        # both are fetched defensively so an untagged or category-less post
        # can't break the build.
        meta = []
        if getattr(article, 'author', None):
            meta.append(f"Author: {article.author.name}")
        meta.append(f"Originally published: {article.date.strftime('%Y-%m-%d')}")
        if getattr(article, 'category', None):
            meta.append(f"Category: {article.category.name}")
        tags = getattr(article, 'tags', None)
        if tags:
            meta.append("Tags: " + ", ".join(tag.name for tag in tags))
        meta.append(f"Canonical URL: {_canonical_url(article.url)}")
        header = "# {}\n\n{}\n\n".format(article.title, "\n".join(meta))
        with open(md_abspath, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(body.strip())
            f.write('\n')


def _write_llms_txt(pelican_obj):
    output_path = _markdown_mirror_state['output_path']
    if not output_path:
        return
    articles = sorted(_markdown_mirror_state['articles'], key=lambda a: a.date, reverse=True)
    lines = [
        "# " + SITENAME,
        "",
        "> Zack M. Davis's blog: computing, mathematics, psychology, "
        "philosophy, social science, arts & culture, fiction. Clean "
        "Markdown versions of every post are linked below.",
        "",
        "## Posts",
        "",
    ]
    for article in articles:
        lines.append(
            f"- [{article.title}]({_canonical_url(article.markdown_url)}) "
            f"({article.date.strftime('%Y-%m-%d')})"
        )
    with open(_os.path.join(output_path, 'llms.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


_signals.article_generator_finalized.connect(_prepare_markdown_mirrors)
_signals.finalized.connect(_write_markdown_mirrors)
_signals.finalized.connect(_write_llms_txt)
