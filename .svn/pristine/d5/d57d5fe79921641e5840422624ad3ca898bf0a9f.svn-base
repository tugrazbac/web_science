# encoding: utf-8
import os
import json
import unittest
import tests

class TestComponentsSubmission(unittest.TestCase):

  def test_if_components_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'components')))

  def test_if_components_file_contains_results_tuple(self):
    self.assertTrue(tests.valid_json_file(u'components'))
    with open(tests.get_submission_location(u'components'), 'r') as fh:
      _, _, _ = json.load(fh)

  def test_if_components_plot_exists(self):
    _plot = tests.get_plot_location(u'components')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)

