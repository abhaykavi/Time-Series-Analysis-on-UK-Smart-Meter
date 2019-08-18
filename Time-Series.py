# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:38:48 2019

@author: Abhay K P
"""

import warnings
#import itertools
#import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import pandas as pd
#import statsmodels.api as sm
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'

df = pd.read_csv("Power-Networks-LCL.csv")
data_top = df.head(5)
print(data_top)
print(df.dtypes)
#df.drop(['stdorToU'],axis=1)
data_top = df.head(5)
print(data_top)
print(df.dtypes)