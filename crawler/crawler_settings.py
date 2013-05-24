#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
As this code performs crawling, it's only nice to tell the website about us.
For me, that includes mentioning the project, the location of the project,
and my own personal email.
If you modify / run this yourself, please change the crawler_headers!
"""

# Purposely made this invalid so that this fails if not attended to by the user before running
CRAWLER_HEADERS = {
    'User-Agent': 1 / 0  # 'Rosetta Fight (https://github.com/Smerity/rosettafight)',
    'From': 1 / 0  # 'smerity@smerity.com'
}
