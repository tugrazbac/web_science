#!/usr/bin/env python
# encoding: utf-8
import json
import networkx
import numpy
from matplotlib.pylab import plt


# TODO Student: Implement PageRank as described in the lecture and implement the
#               "Scaled PageRank Update Rule" etc. Do not use any algorithm
#               implementation provided by networkx or numpy!
# TODO Student: Load the graph stored in 'valar-morghulis.gml.gz'.
# TODO Student: Run the graph through your PageRank implementation multiple
#               times and with 150 steps per run while varying 's' (see
#               slides) from 0.0 to 0.95 in steps of 0.05. Store the
#               resulting rank vector.
# TODO Student: Store the results from every run in a MxN Matrix, where M
#               represents the used 's' and N is the length of the rank vector.
# TODO Student: Create a plot showing the sensibility of the PageRank
#               algorithm with respect to 's'. Label the axes accordingly!
# TODO Student: Save this plot (as a PNG) in 'submissions/pagerank.png'
# TODO Student: Use '.tolist()' on the previously mentioned matrix and pass
#               the resulting list to the 'store_result' function.

def perform(graph):
  return numpy.zeros((20, graph.number_of_nodes()))


def plot(ranks):
  plt.figure(figsize=(20,10))
  plt.title("A2.3 PageRank (s-Sensibility)")
  plt.savefig("submission/pagerank.png")


if __name__ == '__main__':
  graph = networkx.read_gml('valar-morghulis.gml.gz', label='id')
  results = perform(graph)
  plot(results)

  with open(u'submission/pagerank.json', 'w') as fh:
    json.dump(results.tolist(), fh)
