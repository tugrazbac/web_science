# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import degree
import tests

degree.plot = tests.skip_plot

class TestDegreeTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.erdos_renyi_graph(77, 0.08, 2015, False)
    self._results = degree.perform(self._graph)
    self._average_degree = 6.31168831169
    self._maximum_degree = 12
    self._degree_distribution = numpy.array([0, 0, 2, 2, 9, 14, 18, 12, 8, 8, 3, 0, 1])

    self.assertEqual(len(self._results), 3)
    self.maximum_degree, self.average_degree, self.degree_distribution = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self.maximum_degree),   type(self._maximum_degree))
    self.assertEqual(type(self.average_degree),   type(self._average_degree))
    self.assertEqual(type(self.degree_distribution), type([]))

  def test_if_maximum_degree_matches_expectation(self):
    self.assertGreater(self.maximum_degree, 0)
    self.assertEqual(self.maximum_degree, self._maximum_degree)

  def test_if_average_degree_matches_expectation(self):
    self.assertGreater(self.average_degree, 0)
    numpy.testing.assert_almost_equal(self.average_degree, self._average_degree)

  def test_if_degree_distribution_match_expectations(self):
    self.assertGreater(len(self.degree_distribution), 0)
    self.assertEqual(len(self.degree_distribution), self._degree_distribution.size)
    numpy.testing.assert_almost_equal(self.degree_distribution, self._degree_distribution)


