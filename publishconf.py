#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If you have a custom domain, set it here
# SITEURL = 'https://yourdomain.com'

# RSS (not Atom) to match the existing WordPress feed's format at
# zackmdavis.net/blog/feed/. The output path is feed/index.xml rather than
# a bare feed/ so it's a real static file; getting the URL down to exactly
# /feed/ (no filename) needs a webserver directory-index or redirect rule,
# which depends on whatever we end up hosting on.
FEED_ALL_RSS = 'feed/index.xml'
CATEGORY_FEED_RSS = 'category/{slug}/feed/index.xml'

DELETE_OUTPUT_DIRECTORY = True

# Keep RELATIVE_URLS = False for production to get proper absolute URLs
