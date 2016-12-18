# encoding: utf-8
import sys
import numpy
import unittest
import networkx
import distance
import tests

distance.plot = tests.skip_plot

class TestDistanceTask(unittest.TestCase):

  def setUp(self):
    self._graph = networkx.karate_club_graph()
    self._results = distance.perform(self._graph)
    self._diameter = 5
    self._average_distance = 2.4081996434937611
    self._distances = numpy.array([0.1390374,
                                   0.4723707,
                                   0.2442067,
                                   0.1301247,
                                   0.0142602])

    self.assertEqual(len(self._results), 3)
    self.diameter, self.average_distance, self.distances = self._results

  def test_if_result_tuple_contains_proper_types(self):
    self.assertEqual(type(self.diameter),         type(self._diameter))
    self.assertEqual(type(self.average_distance), type(self._average_distance))
    self.assertEqual(type(self.distances),        type([]))

  def test_if_diameter_matches_expectation(self):
    self.assertGreater(self.diameter, 0)
    self.assertEqual(self.diameter, self._diameter)

  def test_if_average_distance_matches_expectation(self):
    self.assertGreater(self.average_distance, 0.0)
    numpy.testing.assert_almost_equal(self.average_distance, self._average_distance)

  def test_if_distances_match_expectations(self):
    self.assertGreater(len(self.distances), 0)
    self.assertEqual(len(self.distances), self._distances.size)
    numpy.testing.assert_almost_equal(self.distances, self._distances)

