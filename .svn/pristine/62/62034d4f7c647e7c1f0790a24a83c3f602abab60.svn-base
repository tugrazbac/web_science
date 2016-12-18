#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import json
import numpy
import networkx
import matplotlib.pylab as plt

def perform(graph):
  ''' Takes a networkx.Graph, calculates certain clustering related metrics and
  returns a tuple containing the graph's average clustering coefficient and
  the graph's clustering coeffiecients as a histogram with twenty bins. '''

  average_clustering_coefficient, clustering_coefficients_bhist = 0.0, []

  # TODO Student: Calculate the graph's average clustering coefficient.
  average_clustering_coefficient = networkx.average_clustering(graph)

  # TODO Student: Calculate the graph's clustering coefficients and return a
  #               histogram with 20 bins.
  clustering_coefficients = networkx.clustering(graph)
  clustering_coefficients = [v for v in clustering_coefficients.values()]
  clustering_coefficients_bhist = numpy.histogram(clustering_coefficients, 20)
  clustering_coefficients_bhist = list(clustering_coefficients_bhist[0])

  if average_clustering_coefficient > 0 and len(clustering_coefficients) > 0:
    plot(clustering_coefficients, average_clustering_coefficient)

  return (average_clustering_coefficient, clustering_coefficients_bhist)

def plot(clustering_coefficients, average_clustering_coefficient):
  ''' Plots the given results returned from 'perform' and stores the resulting
      file in the submission folder. '''

  plt.title("Clustering Coefficient: $avg(C) = %0.4f$" % average_clustering_coefficient)
  plt.xlabel("$c$")
  plt.ylabel("$f(c)$")
  plt.hist(clustering_coefficients)
  plt.savefig("submission/clustering.png")

if __name__ == u'__main__':
  graph = networkx.read_gml(u'graph-b.gml.gz')
  results = perform(graph)

  with open(u'submission/clustering.json', 'w') as fh:
    json.dump(results, fh)

