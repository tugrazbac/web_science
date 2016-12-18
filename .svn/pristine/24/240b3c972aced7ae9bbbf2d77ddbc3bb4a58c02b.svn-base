#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import json
import numpy
import networkx
import matplotlib.pylab as plt

def perform(graph):
  ''' Takes a networkx.Graph, calculates the degrees and clustering
  coefficients for the given graph, calls 'plot' to generate a scatterplot
  (degree vs.  clustering coefficients) and returns a 2-tuple containing two
  lists with the degrees and clustering coefficients. '''

  degree, clustering = [], []

  # TODO Student: Calculate list of degrees.
  degree = networkx.degree(graph).values()
  degree = [v for v in degree]

  # TODO Student: Calculate list of clustering coefficients.
  coefficient = networkx.clustering(graph).values()
  clustering = [ v for v in coefficient]

  if(len(degree) > 0 and len(clustering) > 0):
    plot(degree, clustering)

  return (degree, clustering)

def plot(degree, clustering):
  ''' Takes the 'degree' and 'clustering' lists and produces a scatter plot. '''

  # TODO Student: Visualize the results using a scatter plot.
  # TODO Student: Store the plot in 'submission/scatter.png'.
  plt.scatter(degree, clustering)
  # plt.show()
  plt.savefig("submission/scatter.png")

  return True

if __name__ == u'__main__':
  graph = networkx.read_gml(u'graph-b.gml.gz')
  results = perform(graph)

  with open(u'submission/scatter.json', 'w') as fh:
    json.dump(results, fh)

