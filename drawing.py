#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:25:07 2017

@author: macgx
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

#==============================================================================
# spread achieved
#==============================================================================
print('spread achieved')
df21 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flixster/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_1 = df21['seed_number'].values
influence_sp_1 = df21['influence_sp'].values

df22 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flickr/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_2 = df22['seed_number'].values
influence_sp_2 = df22['influence_sp'].values

df23 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_digg/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_3 = df23['seed_number'].values
influence_sp_3 = df23['influence_sp'].values

df24 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_twitter/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_4 = df24['seed_number'].values
influence_sp_4 = df24['influence_sp'].values

plt.figure(1)
flixster, = plt.plot(seed_number_1, influence_sp_1, 'bo', label='Flixster')
flickr, = plt.plot(seed_number_2, influence_sp_2, 'r*', label='Flickr')
digg, = plt.plot(seed_number_3, influence_sp_3, 'gs', label='Digg')
twitter, = plt.plot(seed_number_4, influence_sp_4, 'y+', label='Twitter')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")
plt.legend(handles=[flixster, flickr, digg, twitter])

plt.figure(3)
flixster, = plt.plot(seed_number_1, influence_sp_1, 'bo', label='Flixster')
flickr, = plt.plot(seed_number_2, influence_sp_2, 'r*', label='Flickr')
digg, = plt.plot(seed_number_3, influence_sp_3, 'gs', label='Digg')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")
plt.legend(handles=[flixster, flickr, digg])
plt.savefig('spread_3.png')

plt.figure(4)
flixster, = plt.plot(seed_number_1, influence_sp_1, 'bo', label='Flixster')
flickr, = plt.plot(seed_number_2, influence_sp_2, 'r*', label='Flickr')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")
plt.legend(handles=[flixster, flickr])
plt.savefig('spread_2.png')

#==============================================================================
# accuracy of spread prediction
#==============================================================================
df1 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flixster/PC_0.txt",
                   sep=' ', header=None,index_col = None, 
                   names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_1 = df1['actual_spread'].values
predicted_spread_1 = df1['predicted_spread'].values
RE1 = np.array(abs(actual_spread_1 - predicted_spread_1),dtype=float) / actual_spread_1

df2 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flickr/PC_0.txt",
                  sep=' ', header=None,index_col = None,
                  names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_2 = df2['actual_spread'].values
predicted_spread_2 = df2['predicted_spread'].values 
RE2 = np.array(abs(actual_spread_2 - predicted_spread_2),dtype=float) / actual_spread_2

df3 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_digg/PC_0.txt",
                  sep=' ', header=None,index_col = None,
                  names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_3 = df3['actual_spread'].values
predicted_spread_3 = df3['predicted_spread'].values 
RE3 = np.array(abs(actual_spread_3 - predicted_spread_3),dtype=float) / actual_spread_3

df4 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_twitter/PC_0.txt",
                  sep=' ', header=None,index_col = None,
                  names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_4 = df4['actual_spread'].values
predicted_spread_4 = df4['predicted_spread'].values 
RE4 = np.array(abs(actual_spread_4 - predicted_spread_4),dtype=float) / actual_spread_4

#### total time taken : 672.417 minutes for digg prediction under 10 data in actions_in_testing.txt
#RMSE = mean_squared_error(df1['actual_spread'].values, df1['predicted_spread'].values)
print('accuracy of spread prediction')
plt.figure(2)
flixster, = plt.plot(actual_spread_1, RE1, 'bo', label='Flixster')
flickr, = plt.plot(actual_spread_2, RE2, 'r*', label='Flickr')
digg, = plt.plot(actual_spread_3, RE3, 'gs', label='Digg')
twitter, = plt.plot(actual_spread_4, RE4, 'y+', label='Twitter')
plt.xlabel("Actual spread")
plt.ylabel("Relative error")
plt.legend(handles=[flixster, flickr, digg, twitter])

#print('accuracy of spread prediction (2)')
#plt.figure(31)
#plt.plot(actual_spread_1, predicted_spread_1, 'bo')
#plt.xlabel("Actual spread")
#plt.ylabel("Predicted spread")
#plt.figure(32)
#plt.plot(actual_spread_2, predicted_spread_2, 'r*')
#plt.xlabel("Actual spread")
#plt.ylabel("Predicted spread")
#plt.figure(33)
#plt.plot(actual_spread_3, predicted_spread_3, 'gs')
#plt.xlabel("Actual spread")
#plt.ylabel("Predicted spread")
#plt.figure(34)
#plt.plot(actual_spread_4, predicted_spread_4, 'y+')
#plt.xlabel("Actual spread")
#plt.ylabel("Predicted spread")

