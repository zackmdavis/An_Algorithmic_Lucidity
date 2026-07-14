#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Zack M. Davis'
SITENAME = 'An Algorithmic Lucidity'
SITESUBTITLE = 'a blog'
SITEURL = ''

PATH = 'content'
THEME = 'theme'

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
    ('Beach City Bugle', 'http://www.beachcitybugle.com/'),
    ('Claude Opus 4.5', 'https://claudeopus45.substack.com/'),
    ('Compass Rose', 'http://benjaminrosshoffman.com/'),
    ('Daniel Lemire', 'http://lemire.me/blog/'),
    ('David R. MacIver', 'http://www.drmaciver.com/blog/'),
    ('Equestria Daily', 'http://www.equestriadaily.com/'),
    ('From Automorphy to Electricity', 'http://automorphy.blogspot.com/'),
    ('Gallabytes', 'http://gallabytes.com/archive.html'),
    ('Jeff Kaufman', 'http://www.jefftk.com/index'),
    ('Julia Evans', 'http://jvns.ca/'),
    ('Meteuphoric', 'http://meteuphoric.wordpress.com/'),
    ('Otium', 'http://srconstantin.wordpress.com/'),
    ('Reflective Disequilibrium', 'http://reflectivedisequilibrium.blogspot.com/'),
    ('Ribbonfarm', 'http://www.ribbonfarm.com/'),
    ('Seeking Whence', 'http://grognor.blogspot.com/'),
    ('Slate Star Codex', 'http://slatestarcodex.com/'),
    ('Stuart Spence Stuff', 'http://stuartspencestuff.blogspot.com/'),
    ('The Rationalist Conspiracy', 'http://rationalconspiracy.com/'),
    ("The Story's Story", 'http://jseliger.wordpress.com/'),
    ('The Unit of Caring', 'http://theunitofcaring.tumblr.com/'),
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
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
    },
    'output_format': 'html5'
}

# Don't use relative URLs in production - using False for proper absolute URLs
RELATIVE_URLS = False
