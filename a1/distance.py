#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import json
import numpy as np
import networkx
import matplotlib.pylab as plt

def perform(graph):
  ''' Takes a networkx.Graph, calculates certain distance related metrics and
  returns a 3-tuple containing the graph's diameter, average vertex distance
  and (normalized) distance distribution. '''

  diameter, average_distance, distance_distribution = 0, 0.0, []

  # TODO Student: Calculate the graph's diameter.
  diameter = networkx.diameter(graph)

  # TODO Student: Calculate the graph's average distance between nodes.
  average_distance = networkx.average_shortest_path_length(graph)

  # TODO Student: Calculate the graph's distances.
  distances = []
  for node1 in graph.nodes():
    for node2 in graph.nodes():
      if node1 != node2:
        distances.append(networkx.shortest_path_length(graph, source=node1, target=node2))

  # TODO Student: Calculate the graph's distance distribution.
  distance_occurances = dict((x,distances.count(x)) for x in set(distances))
  values_of_distance_occ = [v for v in distance_occurances.values()]
  distance_distribution = [float(i)/sum(values_of_distance_occ) for i in values_of_distance_occ] #normieren

  if len(distances) > 0 and diameter > 0:
    plot(distances, diameter)

  return (diameter, average_distance, distance_distribution)

def plot(distances, diameter):
  ''' Plots the given results returned from 'perform' and stores the resulting
      file in the submission folder. '''

  plt.title("Distance Distribution")
  plt.hist(distances, bins=diameter, normed=True, align='right')
  plt.xlabel("Distance $d$")
  plt.ylabel("$p(d)$")
  plt.savefig("submission/distance.png")

if __name__ == u'__main__':
  graph = networkx.read_gml(u'graph-b.gml.gz')
  results = perform(graph)

  with open(u'submission/distance.json', 'w') as fh:
    json.dump(results, fh)
