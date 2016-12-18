# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import components
import tests

components.plot = tests.skip_plot

class TestComponentTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.erdos_renyi_graph(12, 0.15, 2015, False)
    self._results = components.perform(self._graph)
    self._number_of_components = 4
    self._largest_component_size = 6
    self._component_distribution = numpy.array([0.16666666666666666, 0, 0, 0.3333333333333333, 0, 0.5])

    self.assertEqual(len(self._results), 3)
    self.number_of_components, self.largest_component_size, self.component_distribution = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self.number_of_components),   type(self._number_of_components))
    self.assertEqual(type(self.largest_component_size), type(self._largest_component_size))
    self.assertEqual(type(self.component_distribution), type([]))

  def test_if_number_of_components_matches_expectation(self):
    self.assertGreater(self.number_of_components, 0)
    self.assertEqual(self.number_of_components, self._number_of_components)

  def test_if_largest_component_size_matches_expectation(self):
    self.assertGreater(self.largest_component_size, 0)
    numpy.testing.assert_almost_equal(self.largest_component_size, self._largest_component_size)

  def test_if_component_distribution_match_expectations(self):
    self.assertGreater(len(self.component_distribution), 0)
    self.assertEqual(len(self.component_distribution), self._component_distribution.size)
    numpy.testing.assert_almost_equal(self.component_distribution, self._component_distribution)

