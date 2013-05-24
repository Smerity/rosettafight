#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
1) Retrieve the MediaWiki markup for each task and store it to avoid repeated crawling
2) Extract the languages and their solutions from each of the MediaWiki pages
"""
# Python stdlib
import codecs
import json
import os
import re
import time
from collections import defaultdict
# Third Party
import requests
# Local files
from crawler_settings import CRAWLER_HEADERS


def retrieve_task_markup(title):
  # Retrieve the MediaWiki markup using their API
  params = {'format': 'json', 'action': 'query', 'titles': title, 'prop': 'revisions', 'rvprop': 'content'}
  resp = requests.get('http://rosettacode.org/mw/api.php',
                      params=params,
                      headers=CRAWLER_HEADERS
                      )
  data = json.loads(resp.content)
  # Quick and dirty hack to retrieve the MediaWiki markup
  text = data['query']['pages'].values()[0]["revisions"][0]['*']
  return text


def find_solutions(text):
  # Scary naive regex to retrieve the language and the solutions
  # (?s) makes the DOTALL character match any character, specifically newline
  pat = re.compile(r'(?s)<lang ([^>]+?)>(.+?)</lang>')
  solutions = defaultdict(list)
  for lang, solution in pat.findall(text):
    solutions[lang].append(solution)
  return solutions


if __name__ == '__main__':
  titles = codecs.open('../tasklist.txt', encoding='utf-8').readlines()
  titles = [x.strip() for x in titles]

  if os.path.exists('../tasks.json'):
    retrieved = json.loads(open('../tasks.json').read())
    titles = [x for x in titles if x not in retrieved]
  else:
    retrieved = {}

  for i, title in enumerate(titles):
    print('#{} of {}: {}'.format(i, len(titles), title))
    data = retrieve_task_markup(title)
    retrieved[title] = data
    # Their robots.txt doesn't specify anything, but let's be nice, eh?
    time.sleep(0.5)

    # Store the retrieved data locally in JSON
    f = open('../tasks.json', 'w')
    f.write(json.dumps(retrieved, indent=4))
    f.close()
