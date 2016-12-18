#!/usr/bin/env python
# encoding: utf-8
import json
import math
import networkx
import matplotlib.pylab as plt

def perform(graph, iterations=100):
  ''' Runs the HITS algorithm (as described in the lectures) on a given
      networkx.Graph and returns the hubs and authority scores for all
      nodes.'''

  # TODO Student: Implement and run the HITS algorithm (as described in the lectures)
  #               on a given networkx.Graph. Do not use the networkx functionality.
  # TODO Student: Do not forget to normalize your scores (see slides)!

  return ({}, {}) # (hubs, authorities)

def plot(hubs, authorities):
  ''' Plots the given results returned from 'perform' and stores the resulting file in the submission folder. '''

  # TODO Student: Create a plot showing the hub and authority scores (y-axis) for every node and label both axes accordingly.
  # TODO Student: Store the plot (as a PNG) in 'submission/hits.png'.

  plt.figure(figsize=(10,6))
  plt.title("A2: Hubs & Authorities")
  plt.savefig("submission/hits.png")


if __name__ == '__main__':
  graph = networkx.read_gml('valar-morghulis.gml.gz', label='id')
  results = perform(graph)
  plot(*results)

  with open(u'submission/hits.json', 'w') as fh:
    json.dump(results, fh)
