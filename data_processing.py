
# coding: utf-8

# In[82]:


import csv
import pandas as pd
import numpy as np
from math import *


# In[158]:


filename = 'OD_EU_Cellular_100m.csv'
with open(filename, 'r') as f:
    raw_data_100m = csv.reader(f)
    raw_data_100m_list = list(raw_data_100m)
    raw_data_100m_list = np.array(raw_data_100m_list)
    
sample_num = len(raw_data_100m_list)
    
raw_data_100m_dict = {'Cell grid code': np.array(raw_data_100m_list[:,0]),
                      'X coordinate (int)': np.array(raw_data_100m_list[:,1]),
                      'Y coordinate (int)': np.array(raw_data_100m_list[:,2]),
                      'Technology of connection': np.array(raw_data_100m_list[:,3]),
                      'Signal strength (dBm)': np.array(map(float,raw_data_100m_list[:,4])),
                      'Standard deviation': np.array(raw_data_100m_list[:,5]),
                      'Measurements': np.array(raw_data_100m_list[:,6])
                     }


# In[142]:


def dB2Linear( snr_in_dB ):
    snr_in_linear = np.power( 10, snr_in_dB/10 )
    return snr_in_linear


# In[183]:


# band = 900 * 1e3
# noise = 1000 * 1e-15

# def user_rate(sample_index):
#     signal = raw_data_100m_dict['Signal strength (dBm)'][sample_index]
#     return ( band * log(1+dB2Linear(signal)/noise, 2.0) ) / 1e6 # Mbps

# sample_rate_list = np.array([user_rate(i) for i in range(sample_num)])


# In[207]:


user_num = 10
per_user_sample_num = sample_num / user_num
user_signal_list_dB = np.array( [ [ raw_data_100m_dict['Signal strength (dBm)'][i*per_user_sample_num + j ] 
                                for j in range(per_user_sample_num) ] for i in range(user_num) ] )


# In[208]:


user_signal_list = map(dB2Linear, user_signal_list_dB) 
# row is for each user, and there is 10 rows in total (i.e. 10 users in total)
# column is for sample, and for each user there is 15950 samples in total

