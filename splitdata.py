# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:23:20 2018

@author: Balasubramaniam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
# Importing the dataset
dataset = pd.read_csv('MSFT_Stocks.csv')
stock_group = dataset.groupby('Company')


pinfy_size=len(stock_group.groups['INFY'])*.4
ptcs_size=len(stock_group.groups['TCS'])*.4
pril_size=len(stock_group.groups['RIL'])*.2
infyDataX,infyDataY=stock_group.get_group('INFY')['Open'],stock_group.get_group('INFY')['Close']
tcsDataX,tcsDataY=stock_group.get_group('TCS')['Open'],stock_group.get_group('TCS')['Close']
rilDataX,rilDataY=stock_group.get_group('RIL')['Open'],stock_group.get_group('RIL')['Close']

#frame=[infyDataX.sample(n=int(pinfy_size)),tcsDataX.sample(n=int(ptcs_size)),rilDataX.sample(n=int(pril_size))]
frameX=[infyDataX.head(int(pinfy_size)),tcsDataX.head(int(ptcs_size)),rilDataX.head(int(pril_size))]
frameY=[infyDataY.head(int(pinfy_size)),tcsDataY.head(int(ptcs_size)),rilDataY.head(int(pril_size))]
#print(frameX)
#print(frameY)
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(frameX, frameY, test_size = 0.2, random_state = 0)
print(X_test)

