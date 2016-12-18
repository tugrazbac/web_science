#!/usr/bin/env python
# encoding: utf-8
import os
import sys
import json
import numpy
import networkx
import matplotlib.pylab as plt

def perform(graph):
  ''' Takes a networkx.Graph, calculates certain component related metrics and
  returns a 3-tuple containing the graph's number of components, the size of
  the largest component and the component distribution. '''
  number_of_components, largest_component_size, component_distribution = 0, 0, []

  # TODO Student: Calculate the graph's number of components
  number_of_components = networkx.number_connected_components(graph)

  # TODO Student: Calculate the size of the graph's largest component.
  components = [comp for comp in networkx.connected_components(graph)]
  component_size = [len(comp) for comp in components]
  largest_component_size = max(component_size)

  # TODO Student: Calculate the graph's component distribution (fraction of
  #               nodes in percent belonging to a component of size n).
  all_len = [len(c) for c in sorted(networkx.connected_components(graph), key=len, reverse=True)]
  count_occurences = dict((x,all_len.count(x)) for x in set(all_len))

  #find missing keys and add zeros
  keys = list(count_occurences.keys())
  i = 1
  if(keys[-1] != len(keys)):
    while(i <= max(keys)):
      if i not in count_occurences.keys():
        count_occurences.update({i: 0})
      i = i + 1

  for key, value in count_occurences.iteritems():
    component_distribution.append((float(key)/graph.number_of_nodes()) * value)

  return (number_of_components, largest_component_size, component_distribution)

def plot(results):
  ''' Plots the given results returned from 'perform' and stores the resulting
      file in the submission folder. '''

  _, size_of_largest_component, component_distribution = results

  plt.bar(range(1, size_of_largest_component + 1), component_distribution)
  plt.ylabel("Fraction of Nodes %")
  plt.xlabel("Size of Component")
  plt.title("Component Distribution")
  plt.savefig("submission/components.png")

if __name__ == u'__main__':
  graph = networkx.read_gml(u'graph-a.gml.gz')
  results = perform(graph)
  plot(results)

  with open(u'submission/components.json', 'w') as fh:
    json.dump(results, fh)

