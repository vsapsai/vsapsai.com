#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Volodymyr Sapsai'
SITENAME = u'Volodymyr Sapsai'
SITEURL = u'http://vsapsai.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

LOCALE = ('en_US',)
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = 'theme'
COPYRIGHT_URL = 'http://creativecommons.org/licenses/by-nc-sa/3.0/'
DIRECT_TEMPLATES = ('index', )
AUTHOR_SAVE_AS = False    # single author
CATEGORY_SAVE_AS = False  # no categories

STATIC_PATHS = ['static/htaccess.txt']
EXTRA_PATH_METADATA = {
    'static/htaccess.txt': {'path': '.htaccess'}
}

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
