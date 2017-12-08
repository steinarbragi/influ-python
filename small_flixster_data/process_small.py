#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:25:47 2017

@author: macgx
"""

#hey whats up

import time
from datetime import date, datetime
from igraph import *
import calendar
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

with open("../small_flixster_data/small_action_logs.txt") as fin:
    small_action_logs = []
    for line in fin:
        arr = line.split()
        small_action_logs.append([int(arr[0]),int(arr[1]),int(arr[2])])

# Split action_logs into train and test set
train_actions, test_actions = train_test_split(small_action_logs, test_size=0.2)

# Sort action logs in the training set and output
print("Sorting train_actions...")
train_actions = sorted(train_actions, key = lambda t:(t[1],t[2]))
#train_actions.sort(lambda t:(t[1],t[2])) ## not chronologically ?

print("Writing train_actions...")
with open("../small_flixster_data/actionlog.txt", "w") as fout_action:
    for line in train_actions:
        if line[2] > 1000000000:
            fout_action.write("%d %d %d\n" % (line[0], line[1], line[2]))

print("Writing action_ids_in_testset...")
with open("../small_flixster_data/actions_in_testing.txt", "w") as fout_actionid_test:
    movie_id_test = set()
    for line in test_actions:
        movie_id_test.add(line[1])
    for id in movie_id_test:
        fout_actionid_test.write("%d\n" % id)

#==============================================================================
# Output action_ids_in_trainset
#==============================================================================
with open("../small_flixster_data/actions_in_training.txt", "w") as fout_actionid_train:
    movie_id_train = set()
    for line in train_actions:
        movie_id_train.add(line[1])
    for id in movie_id_train:
        fout_actionid_train.write("%d\n" % id)
















#
