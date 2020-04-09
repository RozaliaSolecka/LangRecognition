import argparse
import copy

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import numpy
import plotly
import networkx as nx
from DistributionCoreHandler import loadCompleteDistro
from cmpAlgorithms import KullbackLeibnerIteration
from globalVariables import LANGS
import statistics as st

def graph_print():
    dist = loadCompleteDistro()
    matrix = numpy.zeros((len(dist), len(dist)))
    i = 0
    labels = {}
    for lang1 in dist.keys():
        labels[i] = lang1
        j = 0
        for lang2 in dist.keys():
            if lang1 != lang2:
                matrix[i][j] = round(KullbackLeibnerIteration(dist[lang1].alain(dist[lang2]), dist[lang2].alain(dist[lang1])),2)
            else:
                matrix[i][j] = 0
            j += 1
        i += 1

    G = nx.from_numpy_matrix(matrix)
    H = nx.relabel_nodes(G, labels)

    vg = []
    for u in H.edges.data():
        vg.append(u[2]["weight"])

    vg.sort()
    median = vg[40]

    Z = copy.deepcopy(H)
    for u in Z.edges.data():
        if u[2]["weight"] > median:
            H.remove_edge(u[0], u[1])


    pos = nx.spring_layout(H,k=1, iterations=20)
    plt.figure(3, figsize=(10, 10))
    labels = nx.get_edge_attributes(H, 'weight')
    nx.draw_networkx(H,pos=pos, with_labels=True,node_size=500)
    nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
    plt.show()


if __name__ == "__main__":
    graph_print()
