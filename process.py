#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 22:42:37 2017

@author: macgx
"""

import time
from datetime import date, datetime
from igraph import *
import calendar
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#==============================================================================
# Input: links.txt (undirected)
# Output grpah_undir.txt and graph_dir.txt
#==============================================================================
# Read the graph
g = Graph.Read_Edgelist("../LinYishi_git/flixster_data/links.txt", directed=False)
print("Number of nodes: ", g.vcount())
print("Number of undirected edges: ", g.ecount())

g_dir = Graph.Read_Edgelist("../LinYishi_git/flixster_data/links.txt", directed=True)
print("Number of directed edges: ", g_dir.ecount())

# Simplify: simple graphs are graphs which do not contain loop and multiple edges.
g = g.simplify()
g.es["weight"] = 0  # dummy weight
print("--------- After simplify:")
print("Number of nodes: ", g.vcount())
print("Number of undirected edges: ", g.ecount())
# Output the undirected graph (with dummy weights)
g.write_ncol("../LinYishi_git/flixster_data/graph_undir.txt", names=None)

# Output the directed graph (with dummy weights)
g.to_directed(mutual=True)
print("Number of directed edges: ", g.ecount()) 
g.write_ncol("../LinYishi_git/flixster_data/graph_dir.txt", names=None)

#==============================================================================
# Input: Ratings.timed.txt
# Output: action_logs.txt
#==============================================================================
fin_rating = open("../LinYishi_git/flixster_data/Ratings_timed.txt", "r")
line = fin_rating.readline()  # skip the first line 
movie_set = set()
action_logs = []
for line in fin_rating:
    arr = line.replace('\00', '').split()
    if len(arr) == 5 :
        user = int(arr[0])
        movie = int(arr[1])
        movie_set.add(movie)
        raw_timestamp = datetime.strptime(arr[3], '%Y-%m-%d') 
        """if action performed in other timezones, we keep its local timestamp and associate epoch.
         use calendar class to avoid interference of my timezone
         """
        timestamp = calendar.timegm(raw_timestamp.timetuple())
        action_logs.append([user, movie, timestamp])
fin_rating.close()
print("Number of logs: ", len(action_logs))
print("Number of action ids: ", len(movie_set))

# sample and write small_action_logs.txt
print("sample and write it into small_action_logs...")
df = pd.DataFrame(data = action_logs, dtype = int, index=None,columns=None)
small_df = df.sample(frac=0.1, replace=True)
np.savetxt('small_flixster_data/small_action_logs.txt', small_df.values, fmt='%d')

# Split action_logs into train and test set
train_actions, test_actions = train_test_split(action_logs, test_size=0.2)

# Sort action logs in the training set and output
print("Sorting train_actions...")
train_actions.sort(key = lambda t:(t[1],t[2])) ## not chronologically ?

print("Writing train_actions...")
with open("../LinYishi_git/flixster_data/action_logs.txt", "w") as fout_action:
    for line in train_actions:
        if line[2] > 1000000000:
            fout_action.write("%d %d %d\n" % (line[0], line[1], line[2]))
            
print("Writing action_ids_in_testset...")
with open("../LinYishi_git/flixster_data/actions_in_testing.txt", "w") as fout_actionid_test:
    movie_id_test = set()
    for line in train_actions:
        movie_id_test.add(line[1])
    for id in movie_id_test:
        fout_actionid_test.write("%d\n" % id)

#==============================================================================
# Output action_ids_in_trainset
#==============================================================================
with open("../LinYishi_git/flixster_data/actions_in_training.txt", "w") as fout_actionid_train:
    movie_id_train = set()
    for line in train_actions:
        movie_id_train.add(line[1])
    for id in movie_id_train:
        fout_actionid_train.write("%d\n" % id)
        
#==============================================================================
#  Split action_logs into actions_in_training and anctions_in_testing     
#==============================================================================
#actions_in_training = action_logs[0::5] 
#actions_in_testing = [x for x in action_logs if x not in actions_in_training] # too long time :(

      
        
        
        
        
        
        
        
        
        
        
        