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

  @mock.patch('main.tasks', tasks)
  def test_index(self):
    rv = self.client.get('/')
    self.assert200(rv)
    assert 'HelloStr' in unicode(rv.data, encoding='utf-8')
    assert 'Integer64' in unicode(rv.data, encoding='utf-8')

  def test_view_non_existing_task(self):
    rv = self.client.get('/?task=FourthWall')
    self.assert404(rv)

  @mock.patch('main.solutions', solutions)
  @mock.patch('main.tasks', tasks)
  def test_view_task(self):
    rv = self.client.get('/?task=HelloStr')
    self.assert200(rv)
    assert 'print' in unicode(rv.data, encoding='utf-8')
    assert 'fmt.Println' in unicode(rv.data, encoding='utf-8')


if __name__ == '__main__':
  unittest.main()
