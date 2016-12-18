# encoding: utf-8
import os
import json
import unittest
import tests

class TestDegreeSubmission(unittest.TestCase):

  def test_if_degree_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'degree')))

  def test_if_degree_file_contains_results_tuple(self):
    tests.valid_json_file(u'degree')
    with open(tests.get_submission_location(u'degree'), 'r') as fh:
      _, _, _ = json.load(fh)

  def test_if_degree_plot_exists(self):
    _plot = tests.get_plot_location(u'degree')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)

