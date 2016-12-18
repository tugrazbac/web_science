# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import scatter
import tests

scatter.plot = tests.skip_plot

class TestScatterTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.gnp_random_graph(10, 0.15, 2015, False)
    self._results = scatter.perform(self._graph)
    self._degree = numpy.array([2, 2, 0, 1, 1, 2, 4, 3, 1, 0])
    self._clustering = numpy.array([0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.3333333333333333, 0.0, 0.0])

    self.assertEqual(len(self._results), 2)
    self.degree, self.clustering = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self.degree),     type([]))
    self.assertEqual(type(self.clustering), type([]))

  def test_if_degree_matches_expectations(self):
    self.assertGreater(len(self.degree), 0)
    numpy.testing.assert_almost_equal(self.degree, self._degree)

  def test_if_clustering_matches_expectations(self):
    self.assertGreater(len(self.clustering), 0)
    numpy.testing.assert_almost_equal(self.clustering, self._clustering)

