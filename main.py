#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dynamic web view for local testing
"""
from __future__ import print_function, unicode_literals
# Python stdlib
import codecs
import re
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


def simple_name(s):
  return re.sub('[^A-Za-z0-9]', '', s)


@app.route('/data/tasklist.json')
def tasklist_json():
  return flask.jsonify(tasklist=tasks)


@app.route('/data/tasks/<simple_title>.json')
def solutions_json(simple_title):
  title = None
  for x in tasks:
    h = simple_name(x)
    if h == simple_title:
      title = x
      break
  if title not in solutions:
    return 'Given task does not exist', 404
  sols = solutions[title]
  return flask.jsonify(solutions=sols)


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
