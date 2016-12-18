# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import clustering
import tests

clustering.plot = tests.skip_plot

class TestClusteringTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.barabasi_albert_graph (200, 50, seed=2015)
    self._results = clustering.perform(self._graph)
    self._average_clustering_coefficient = 0.4862821
    self._clustering_coefficients = numpy.array([1, 4, 10, 17, 26, 26, 27, 14,
                                                15, 15, 1, 11, 5, 6, 10, 4, 2,
                                                 2, 2, 2])

    self.assertEqual(len(self._results), 2)
    self.average_clustering_coefficient, self.clustering_coefficients = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self._average_clustering_coefficient),
                     type(self.average_clustering_coefficient))
    self.assertEqual(type(self.clustering_coefficients), type([]))

  def test_if_average_clustering_coefficient_matches_expectation(self):
    self.assertGreater(self.average_clustering_coefficient, 0)
    numpy.testing.assert_almost_equal(self.average_clustering_coefficient,
                                      self._average_clustering_coefficient)

  def test_if_clustering_coefficients_match_expectations(self):
    self.assertGreater(len(self.clustering_coefficients), 0)
    self.assertEqual(len(self.clustering_coefficients), self._clustering_coefficients.size)
    numpy.testing.assert_almost_equal(self.clustering_coefficients,
                                      self._clustering_coefficients)
