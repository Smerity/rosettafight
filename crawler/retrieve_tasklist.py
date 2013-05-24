#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
This file retrieves the task titles from RosettaCode.
You shouldn't need to run this yourself. If you do, please
ensure you have a good reason, change the headers and
use a respectable crawl rate.
Note: written as one-off code. No testing. Not proper code use.
"""
# Python
import codecs
import json
import requests
# Third Party
# Local Files
from crawler_settings import CRAWLER_HEADERS


if __name__ == '__main__':
  # Use the MediaWiki API to collect all the pages that belong to the Programming Task category ('category members')
  target = 'http://rosettacode.org/mw/api.php?format=json&action=query&list=categorymembers&cmtitle=Category:Programming_Tasks&cmlimit=400'
  tasks = []

  data = json.loads(requests.get(target, headers=CRAWLER_HEADERS).content)
  # The total number of tasks may be greater than that returned, indicated by 'query-continue'
  # If it continues, make another call. Repeat this until we have all the category members.
  while True:
    for obj in data['query']['categorymembers']:
      tasks.append(obj['title'])
    if 'query-continue' not in data:
      break
    continue_token = data['query-continue']['categorymembers']['cmcontinue'] if 'query-continue' in data else None
    data = json.loads(requests.get(target + '&cmcontinue=' + continue_token, headers=CRAWLER_HEADERS).content)

  # Write out the list of task titles locally using UTF-8 (damn you Vigenère!)
  f = codecs.open('../tasklist.txt', mode='w', encoding='utf-8')
  f.write('\n'.join(tasks))
  f.close()
