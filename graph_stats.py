# %% import

import networkx as nx
import matplotlib.pyplot as plt
import math
import numpy as np

# %% E1
G=nx.read_edgelist("data/twitter_graph.txt", nodetype=int, data={('timestamp',int)}, create_using=nx.DiGraph())

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))


# %% Digg
digg=nx.read_edgelist("data/digg_friends.txt", nodetype=int, data={('timestamp',int)}, create_using=nx.DiGraph())

print(nx.number_of_nodes(digg))
print(nx.number_of_edges(digg))

# %% Flixster
flixster=nx.read_edgelist("data/flixster-graph.txt", nodetype=int, data={('timestamp',int)}, create_using=nx.DiGraph())

print(nx.number_of_nodes(flixster))
print(nx.number_of_edges(flixster))

# %% Flickr
flickr=nx.read_edgelist("data/flickr-growth.txt", nodetype=int, data={('timestamp',str)}, create_using=nx.DiGraph())

print(nx.number_of_nodes(flickr))
print(nx.number_of_edges(flickr))

# %%
print('density: ' , nx.density(G))


# %% largest_strong

largest_strong = max(nx.weakly_connected_component_subgraphs(G),key=len)

print(largest_strong.number_of_nodes())
print(largest_strong.number_of_edges())


# %% largest_weak

largest_weak = max(nx.weakly_connected_component_subgraphs(G),key=len)

print(largest_weak.number_of_nodes())
print(largest_weak.number_of_edges())

# %% Degree loglog twitter
plt.loglog(nx.degree_histogram(G))
plt.xlabel('degrees')
plt.ylabel('occurrence')
plt.savefig('data/degree-twitter.png')
plt.show()

# %% Degree loglog digg
plt.loglog(nx.degree_histogram(digg))
plt.xlabel('degrees')
plt.ylabel('occurrence')
plt.savefig('data/degree-digg.png')
plt.show()

# %% Degree loglog flixster
plt.loglog(nx.degree_histogram(flixster))
plt.xlabel('degrees')
plt.ylabel('occurrence')
plt.savefig('data/degree-flixster.png')
plt.show()


# %% Degree loglog flickr
plt.loglog(nx.degree_histogram(flickr))
plt.xlabel('degrees')
plt.ylabel('occurrence')
plt.savefig('data/degree-flickr.png')
plt.show()
