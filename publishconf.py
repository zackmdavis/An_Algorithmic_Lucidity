#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# The blog lives under /blog on this domain, not at the root (the root is a
# small standalone landing page, not part of this Pelican site) -- no
# trailing slash, matching Pelican's own convention for SITEURL.
#
# Deliberately root-relative (no scheme/host): every template link is built
# by concatenating SITEURL onto a path, so a bare https://... here would
# hardcode https into every internal link (CSS, nav, favicon, ...)
# regardless of what protocol the page itself was loaded over -- breaking
# things like previewing over plain HTTP before a certificate exists.
SITEURL = '/blog'

# RSS (not Atom) to match the existing WordPress feed's format at
# zackmdavis.net/blog/feed/. The output path is feed/index.xml rather than
# a bare feed/ so it's a real static file; getting the URL down to exactly
# /feed/ (no filename) needs a webserver directory-index or redirect rule,
# which depends on whatever we end up hosting on.
FEED_ALL_RSS = 'feed/index.xml'
CATEGORY_FEED_RSS = 'category/{slug}/feed/index.xml'

# Feed readers fetch feed XML out of any page context, so its content
# ideally wants absolute URLs -- but Pelican only uses FEED_DOMAIN for the
# feed's own self-referential link (writers.py); each post's own <link> is
# still built straight from SITEURL, so with SITEURL root-relative those
# come out as bare /blog/... too. Harmless while nobody's actually
# subscribed to this pre-launch server; revisit (probably by making
# SITEURL fully-qualified again) once real DNS + a certificate are live and
# this feed has real subscribers.
FEED_DOMAIN = 'https://zackmdavis.net'

DELETE_OUTPUT_DIRECTORY = True
