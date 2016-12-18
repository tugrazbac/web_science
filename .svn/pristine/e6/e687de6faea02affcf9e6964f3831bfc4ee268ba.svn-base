#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import json
import numpy
import networkx as nx
import matplotlib.pylab as plt

def perform(graph):
  ''' Takes a networkx.Graph, calculates certain degree related metrics and
  returns a 3-tuple containing the graph's highest node degree found in the
  graph, the average degree of a node in the graph and the degree distribution
  itself. '''
  maximum_degree, average_degree, degree_distribution = 0, 0.0, []
  # TODO Student: Calculate the maximum degree.
  degree_dict = nx.degree(graph)
  maximum_degree = max(degree_dict.values())

  # TODO Student: Calculate the average degree of a node.
  average_degree = sum(degree_dict.values())/float(len(degree_dict.values()))

  # TODO Student: Calculate the graph's degree distribution.
  degrees = nx.degree(graph)
  degrees = [v for v in degrees.values()]
  degree_distribution = nx.degree_histogram(graph)

  if len(degrees) > 0 and maximum_degree > 0:
    plot(degrees, maximum_degree)

  return (maximum_degree, average_degree, degree_distribution)

def plot(degrees, maximum_degree):
  ''' Plots the given results returned from 'perform' and stores the resulting
      file in the submission folder. '''

  plt.title("Degree Distribution")
  plt.hist(degrees, bins=maximum_degree, normed=True)
  plt.xlabel("Degree $k$")
  plt.ylabel("$p(k)$")
  plt.savefig("submission/degree.png")

if __name__ == u'__main__':
  graph = nx.read_gml(u'graph-a.gml.gz')
  results = perform(graph)

  with open(u'submission/degree.json', 'w') as fh:
    json.dump(results, fh)

