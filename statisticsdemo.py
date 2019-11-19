# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 19:58:28 2018

@author: Balasubramaniam
"""

import statistics
print(statistics.mean([1, 2, 3, 4, 4]))
print(statistics.mean([-1.0, 2.5, 3.25, 5.75]))


from fractions import Fraction as F
print(statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(F(3,67))



from decimal import Decimal as D
print(statistics.mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")]))


from scipy.stats.mstats import gmean
print("Geometric Mean") 
print(gmean([1,9,5,6,6,7]))
print(gmean([0.5,0.25,0.125,0.125,1.75]))

# =============================================================================
# Input : arr[] = {2.0, 1.0}
# Output : 1.3333
# Harmonic mean = 2/(1/2.0 + 1/1.0)
#              = (2 * 2)/3
#              = 1.333
# 
# Input : arr[] = {13.5, 14.5, 14.8, 15.2, 16.1}
# Output : 14.7707
# =============================================================================

#harmonic mean
print("Harmonic Mean")
print(statistics.harmonic_mean([2.5, 3, 10]))
print("Median")
#median
print(statistics.median([1, 3,4, 5]))

#median high
print(statistics.median_high([1, 3, 5, 7]))

#median high
print(statistics.median_low([1, 3, 5, 7]))

print("Statistics Grouped Median...")
print( statistics.median_grouped([52, 52, 53, 54]))

#mode
print(statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"]))
print(statistics.mode([1,1,2,2,2]))

data=[4,5,7,1,3,6,7]
print(statistics.stdev(data))
print(statistics.variance(data))


import numpy as np
#std
a = np.array([[0.10,0.14,0.18], [0.01,0.112,0.018]])
print(np.std(a))
#variance
print(np.var(a))
  
var = np.array([12,11,10, 7, 4, 3, 2, 1]) # input array
#percentile
a = np.array([1,2,3,4,5])
p = np.percentile(a, 50) # return 50th percentile, e.g median.
print("50th percentile")
print (p)
a = np.array([1,2,3,4,5])
p = np.percentile(a, 25) # return 50th percentile, e.g median.
print("25th percentile")
print (p)
print("Quartiles...",'',np.percentile(var, 25,
                                      interpolation='midpoint')) #1,2|3,4|7,10|11,12
#then Q1=2+3/2, Q2=4+7/2,Q3=10+11/2,Q4=12

var=np.array([400,500,550,600,625,650,725,750,800,800,850,925]) 
print(np.percentile(var, np.arange(0, 100, 10),interpolation='midpoint')) # deciles
#d1=12+1/10=1.3=>500+550/2,d2=2*(12+1)/10=2.6=>550+600/2=575,d3=3*(12+1)/10=3.9=>600+625/2=>612.5

import numpy as np
import pandas as pd
data = pd.read_excel('diabetes.xlsx')
#print(data)
df = data[0:10]
#print(df)
mean = np.mean(data['Glucose'])
st_dev = np.std(data['Glucose'])

print("The mean is %r" %(mean))
print("The standard deviation is %r" %(st_dev))
median = np.median(data['Glucose'])
maximum = np.max(data['Glucose'])
minimum = np.min(data['Glucose'])
a = [15, 20, 35, 40, 50]
perc =  np.percentile(a,100)

print("The median is %r" %(median))
print("The maximum is %r" %(maximum))
print("The minimum is %r" %(minimum))
print("The percentile is %r" %(perc))





