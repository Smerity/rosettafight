#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
Tests for the existing dynamic web view
"""
# Python stdlib
import mock
import unittest
# Third Party
import flask
from flask.ext.testing import TestCase
# Local files
from main import app

# Naive fixtures
solutions = {
    'HelloStr': {'python': ['print'], 'go': ['fmt.Println']},
    'Integer64': {'python': ['int'], 'go': ['int64']},
}
tasks = sorted(solutions.keys())


class RosettaTest(TestCase):
  def create_app(self):
    return app

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_json_tasklist(self):
    rv = self.client.get(flask.url_for('tasklist_json'))
    self.assert200(rv)
    self.assertEqual(rv.json, dict(tasklist=tasks))

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_json_solutions(self):
    rv = self.client.get(flask.url_for('solutions_json', task='HelloStr'))
    self.assert200(rv)
    self.assertEqual(rv.json, dict(solutions=solutions['HelloStr']))

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_missing_json_solutions(self):
    rv = self.client.get(flask.url_for('solutions_json', task='FourthWalled'))
    self.assert404(rv)


if __name__ == '__main__':
  unittest.main()
