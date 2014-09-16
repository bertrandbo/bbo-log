#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bertrand Bousquet'
SITENAME = u'bbo-log'
SITEURL = ''

###
# Custom properties
AUTHOR_DESCRIPTION = "Ingénieur logiciel"
AUTHOR_EMAIL = "me@bertrand-bousquet.info"
###

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

GITHUB_URL = "https://github.com/bertrandbo"

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (	('Contenu sous licence CC BY-SA', 'http://creativecommons.org/licenses/by-sa/3.0/fr/'),
			('Propulsé par Pelican', 'http://getpelican.com/'),
			('Hébergé par OVH', 'https://www.ovh.com/fr/index.xml'),
			('Thème pompé chez Tom Preston-Werner', 'http://github.com/mojombo/jekyll'),
			('Icone RSS provenant de Wikipedia', 'http://en.wikipedia.org/wiki/File:Feed-icon.svg'),)



# Social widget
SOCIAL = (	('linkedin.com/bertrandbousquet', 'http://fr.linkedin.com/in/bertrandbousquet'),
			('github.com/bertrandbo', 'https://github.com/bertrandbo'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

CATEGORY_URL = '{slug}'
CATEGORY_SAVE_AS = '{slug}/index.html'

#YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
