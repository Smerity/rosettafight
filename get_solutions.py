#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
A simple look-up script to allow easy retrieval of a solution to a task
for a given language. Requires a precomputed set of solutions.
"""
# Python stdlib
import json
# Third Party
# Local files

solutions = json.loads(open('solutions.json').read())

task_title = raw_input('Task: ')
task = solutions[task_title]
print('Language Choices:', ', '.join(sorted(task.keys())))
language = raw_input('Lang: ')

print('=-=-' * 5)
for sol in task[language]:
  print('\t' + sol.replace('\n', '\n\t'))
  print('=-=-' * 5)
