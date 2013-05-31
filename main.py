#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dynamic web view for local testing and generation of static JSON files
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


@app.route('/data/tasks/<task>.json')
def solutions_json(task):
  title = None
  for x in tasks:
    h = simple_name(x)
    if h == task:
      title = x
      break
  if title not in solutions:
    return 'Given task does not exist', 404
  sols = solutions[title]
  return flask.jsonify(solutions=sols)


@app.route('/test')
def test():
  return open('templates/angular_test.html').read()


@app.route('/')
def index():
  return open('templates/angular.html').read()

if __name__ == '__main__':
  app.run(debug=True)
