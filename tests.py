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
  def test_index(self):
    rv = self.client.get(flask.url_for('index'))
    self.assert200(rv)
    self.assertIn('HelloStr', unicode(rv.data, encoding='utf-8'))
    self.assertIn('Integer64', unicode(rv.data, encoding='utf-8'))

  def test_view_non_existing_task(self):
    rv = self.client.get(flask.url_for('index', task='FourthWall'))
    self.assert404(rv)

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_view_task(self):
    rv = self.client.get(flask.url_for('index', task='HelloStr'))
    self.assert200(rv)
    self.assertIn('print', unicode(rv.data, encoding='utf-8'))
    self.assertIn('fmt.Println', unicode(rv.data, encoding='utf-8'))

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_json_tasklist(self):
    rv = self.client.get(flask.url_for('tasklist_json'))
    self.assert200(rv)
    self.assertEqual(rv.json, dict(tasklist=tasks))

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_json_solutions(self):
    rv = self.client.get(flask.url_for('solutions_json', simple_title='HelloStr'))
    self.assert200(rv)
    self.assertEqual(rv.json, dict(solutions=solutions['HelloStr']))

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_missing_json_solutions(self):
    rv = self.client.get(flask.url_for('solutions_json', simple_title='FourthWalled'))
    self.assert404(rv)


if __name__ == '__main__':
  unittest.main()
