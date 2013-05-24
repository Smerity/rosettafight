#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
1) Retrieve the MediaWiki markup for each task and store it to avoid repeated crawling
2) Extract the languages and their solutions from each of the MediaWiki pages
"""
# Python stdlib
import json
import os
import re
from collections import defaultdict
# Third Party
# Local files


def find_solutions(text):
  # Scary naive regex to retrieve the language and the solutions
  # (?s) makes the DOTALL character match any character, specifically newline
  pat = re.compile(r'(?s)<lang ([^>]+?)>(.+?)</lang>')
  solutions = defaultdict(list)
  for lang, solution in pat.findall(text):
    solutions[lang.lower()].append(solution)
  return solutions


if __name__ == '__main__':
  if os.path.exists('../tasks.json'):
    solutions = defaultdict(list)
    tasks = json.loads(open('../tasks.json').read())
    for task in sorted(tasks.keys()):
      sols = find_solutions(tasks[task])
      solutions[task] = sols

    f = open('../solutions.json', 'w')
    json.dump(solutions, f, indent=4)
