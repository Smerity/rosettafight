#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dynamic web view for local testing
"""
from __future__ import print_function, unicode_literals
# Python stdlib
import codecs
# Third Party
import flask
# Local files

app = flask.Flask(__name__)

try:
  tasks = [x.strip() for x in codecs.open('tasklist.txt', encoding='utf-8').readlines()]
except IOError:
  tasks = []
try:
  solutions = flask.json.loads(open('solutions.json').read())
except IOError:
  solutions = []


@app.route('/')
def index():
  args = {}
  task = flask.request.args.get('task')

  if task:
    sols = solutions.get(task)
    if not sols:
      return 'No such task exists', 404
    args['task_solutions'] = sorted(sols)
    args['codeA'], args['codeB'] = sols.get('python', []), sols.get('go', [])
  return flask.render_template('base.html', tasks=tasks, selected_task=task, **args)

if __name__ == '__main__':
  app.run(debug=True)
