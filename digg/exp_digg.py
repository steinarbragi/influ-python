#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: macgx
"""

from sklearn.model_selection import train_test_split
import pandas as pd

#==============================================================================
#      input: digg_friends.csv
#      output: graph.txt
#==============================================================================

print("get graph.txt...")
sample_df = pd.read_csv("/Users/macgx/Desktop/exp_digg/raw_data_and_preprocess/digg_friends.csv", 
                        sep=',', names=['mutual','time','u1','u2'],header=None,index_col = None)
## no need to sample here 
#sample_df = df.sample(frac=0.0001, replace=True) # proper 0.05 test 0.0001
sample_df['time'] = 0
mutual_df = sample_df[sample_df['mutual']==1]
mutual_df = mutual_df.drop('mutual', axis=1)
small_df = mutual_df[['u1','u2','time']]

small_df.to_csv("/Users/macgx/Desktop/exp_digg/raw_data_and_preprocess/graph.txt", 
                sep=' ', index=False,header=False)
col_0 = set(small_df['u1'])
col_1 = set(small_df['u2'])
user_set = col_0.union(col_1)
print("number of nodes:", len(user_set))
print("number of directed edges:", small_df.shape[0])

#==============================================================================
#     input: digg_votes1.csv
#     output: actionlog  & 
#             actions_in_training  &
#             actions_in_testing 
#==============================================================================

print('get three files associated with action log...')
sample_actionlogs = pd.read_csv("/Users/macgx/Desktop/exp_digg/raw_data_and_preprocess/digg_votes1.csv", 
                        names=['vote_time','voter','story'],sep=',', header=None)
## no need to sample here 
#sample_actionlogs = df_action.sample(frac=0.0001, replace=True) #proper 0.01 test 0.0001

sample_actionlogs = sample_actionlogs[['voter','story','vote_time']]
story_set = set(sample_actionlogs['story'])
print("number of action logs:", sample_actionlogs.shape[0])
print("number of action ids:", len(story_set))

""" split to train and test """
train_actions, test_actions = train_test_split(sample_actionlogs, test_size=0.2)
train_sorted = train_actions.sort_values(by=['story','vote_time'])
train_sorted.to_csv("actionlog.txt", sep=' ', index=False, header=False)

id_train = pd.DataFrame(train_sorted['story'].unique())
id_train.to_csv("actions_in_training.txt",index=False, header=False)

id_test = pd.DataFrame(test_actions['story'].unique())
id_test.to_csv("actions_in_testing.txt",index=False, header=False)






