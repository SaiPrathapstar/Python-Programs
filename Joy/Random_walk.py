# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 10:27:06 2022

@author: Sai Prathap
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.complete_graph(4)
nx.draw(G)
plt.show()