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
# accuracy of spread prediction
#==============================================================================
df1 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flixster/sample_dataset/prediction/PC_0.txt",
                   sep=' ', header=None,index_col = None, 
                   names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_1 = df1['actual_spread'].values
predicted_spread_1 = df1['predicted_spread'].values
AE1 = np.array(abs(actual_spread_1 - predicted_spread_1),dtype=float)

df2 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flickr/sample_dataset/prediction/PC_0.txt",
                  sep=' ', header=None,index_col = None,
                  names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_2 = df2['actual_spread'].values
predicted_spread_2 = df2['predicted_spread'].values 
AE2 = np.array(abs(actual_spread_2 - predicted_spread_2),dtype=float)

df3 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_digg/sample_dataset/prediction/PC_0.txt",
                  sep=' ', header=None,index_col = None,
                  names=['action_id','num_initiators','actual_spread','predicted_spread'])
actual_spread_3 = df3['actual_spread'].values
predicted_spread_3 = df3['predicted_spread'].values 
AE3 = np.array(abs(actual_spread_3 - predicted_spread_3),dtype=float)

#### total time taken : 672.417 for digg prediction under 10 data in actions_in_testing.txt
#RMSE = mean_squared_error(df1['actual_spread'].values, df1['predicted_spread'].values)
print('accuracy of spread prediction (1)')
plt.figure(21)
plt.plot(actual_spread_1, AE1, 'bo')
plt.xlabel("Actual spread")
plt.ylabel("Absolute error")
plt.figure(22)
plt.plot(actual_spread_2, AE2, 'r*')
plt.xlabel("Actual spread")
plt.ylabel("Absolute error")
plt.figure(23)
plt.plot(actual_spread_3, AE3, 'gs')
plt.xlabel("Actual spread")
plt.ylabel("Absolute error")

print('accuracy of spread prediction (2)')
plt.figure(31)
plt.plot(actual_spread_1, predicted_spread_1, 'bo')
plt.xlabel("Actual spread")
plt.ylabel("Predicted spread")
plt.figure(32)
plt.plot(actual_spread_2, predicted_spread_2, 'r*')
plt.xlabel("Actual spread")
plt.ylabel("Predicted spread")
plt.figure(33)
plt.plot(actual_spread_3, predicted_spread_3, 'gs')
plt.xlabel("Actual spread")
plt.ylabel("Predicted spread")

#==============================================================================
# spread achieved
#==============================================================================
print('spread achieved')
df21 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flixster/sample_dataset/maxinf_CD/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_1 = df21['seed_number'].values
influence_sp_1 = df21['influence_sp'].values

df22 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_flickr/sample_dataset/maxinf_CD/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_2 = df22['seed_number'].values
influence_sp_2 = df22['influence_sp'].values

df23 = pd.read_csv("/Users/macgx/Desktop/our-project/exp_digg/sample_dataset/maxinf_CD/PCCov_0_0.001.txt_PCCov.txt",
            sep=' ', header=None,index_col = None, 
            names=['seed_number','g1','g2','influence_sp']) 
seed_number_3 = df23['seed_number'].values
influence_sp_3 = df23['influence_sp'].values

plt.figure(41)
plt.plot(seed_number_1, influence_sp_1, 'bo')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")
plt.figure(42)
plt.plot(seed_number_2, influence_sp_2, 'r*')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")
plt.figure(43)
plt.plot(seed_number_3, influence_sp_3, 'gs')
plt.xlabel("Seed set size")
plt.ylabel("Influence spread achieved")