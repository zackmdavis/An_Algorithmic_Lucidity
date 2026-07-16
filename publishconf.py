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

# Both RSS and Atom, at parallel paths (.../feed/rss/ and .../feed/atom/).
# RSS keeps the WordPress-era /feed/ as its bare-directory default (an
# nginx redirect, see provisioning/nginx_siteconf) since that's what
# existing subscribers' bookmarks expect; Atom is new.
FEED_ALL_RSS = 'feed/rss/index.xml'
CATEGORY_FEED_RSS = 'category/{slug}/feed/rss/index.xml'
FEED_ALL_ATOM = 'feed/atom/index.xml'
CATEGORY_FEED_ATOM = 'category/{slug}/feed/atom/index.xml'

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
