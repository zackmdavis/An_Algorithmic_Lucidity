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
# Absolute now that DNS is cut over and a real cert is live: was deliberately
# root-relative during pre-launch testing (see git history), since a bare
# https://... would have hardcoded https into every internal link regardless
# of protocol, breaking preview over plain HTTP before a cert existed. Now
# that both http and https genuinely work in production (see nginx_siteconf
# -- deliberately no forced https redirect), an absolute SITEURL is correct:
# it makes feed <link> entries and any other absolute-URL consumer point at
# the real site regardless of which protocol/page they were generated from.
SITEURL = 'https://zackmdavis.net/blog'

# Both RSS and Atom, at parallel paths (.../feed/rss/ and .../feed/atom/).
# RSS keeps the WordPress-era /feed/ as its bare-directory default (an
# nginx redirect, see provisioning/nginx_siteconf) since that's what
# existing subscribers' bookmarks expect; Atom is new.
FEED_ALL_RSS = 'feed/rss/index.xml'
CATEGORY_FEED_RSS = 'category/{slug}/feed/rss/index.xml'
FEED_ALL_ATOM = 'feed/atom/index.xml'
CATEGORY_FEED_ATOM = 'category/{slug}/feed/atom/index.xml'

# Feed readers fetch feed XML out of any page context, so its content
# ideally wants absolute URLs -- Pelican only uses FEED_DOMAIN for the feed's
# own self-referential link (writers.py), while each post's own <link> is
# built straight from SITEURL; now that SITEURL is itself absolute, both
# come out fully-qualified and agree with each other.
FEED_DOMAIN = 'https://zackmdavis.net'

DELETE_OUTPUT_DIRECTORY = True
