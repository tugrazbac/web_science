# encoding: utf-8
import os
import json
import unittest
import tests

class TestClusteringSubmission(unittest.TestCase):

  def test_if_clustering_file_exists(self):
    self.assertTrue(os.path.exists(tests.get_submission_location(u'clustering')))

  def test_if_clustering_file_contains_results_tuple(self):
    self.assertTrue(tests.valid_json_file(u'clustering'))
    with open(tests.get_submission_location(u'clustering'), 'r') as fh:
      _, _ = json.load(fh)

  def test_if_clustering_plot_exists(self):
    _plot = tests.get_plot_location(u'clustering')
    self.assertTrue(os.path.exists(_plot))
    self.assertGreater(os.path.getsize(_plot), 0)

