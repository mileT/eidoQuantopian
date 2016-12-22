# -*- coding: utf-8 -*-
"""
Hitrate calculation
outputs: 
    tp: number of true positives, predict up and actual is up
    tn: number of true negatives, predict down and actual is down
    fp: number of false positives, predict up, actual is down
    fn: number of false negatives, predict down, actual is up
    hr: (tp+tn)/(tp+tn+fp+fn)
@author: jhan

"""
import numpy as np

def HitRate1( forecast, actual):  
    i = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(forecast)):
        if forecast[i] > 0 and actual[i] > 0:
             tp = tp +1
        elif forecast[i] < 0 and actual[i] < 0:
             tn = tn + 1
        elif forecast[i] > 0 and actual[i] < 0:
             fp = fp + 1
        elif forecast[i] < 0 and actual[i] > 0:
             fn = fn + 1
    hr = 1.0*(tp+tn)/(tp+tn+fn+fp)
    return tp,tn,fp,fn,hr
    
def HitRate2( forecast, actual):  
    i = 0
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(forecast)):
        if forecast[i] >= 0 and actual[i] >= 0:
             tp = tp +1
        elif forecast[i] < 0 and actual[i] < 0:
             tn = tn + 1
        elif forecast[i] >= 0 and actual[i] < 0:
             fp = fp + 1
        elif forecast[i] < 0 and actual[i] >= 0:
             fn = fn + 1
    hr = 1.0*(tp+tn)/(tp+tn+fn+fp)
    return tp,tn,fp,fn,hr
 
def HitRate( forecast, actual, types):
    if types == 1:
        tp,tn,fp,fn,hr = HitRate1( forecast, actual)
    if types == 2:
        tp,tn,fp,fn,hr = HitRate2( forecast, actual)
    return tp,tn,fp,fn,hr

# Test staff
#f = np.array([1.3,2.0,-1.3,3.0,5.0, -0.3])
#a = np.array([1.0,-2.0,-1.1,3.2,-5.5, -0.4])
#tp1,tn1,fp1,fn1,hr1= HitRate(f, a, 1)
#tp2,tn2,fp2,fn2,hr2 = HitRate(f, a, 2)
#output1 = np.array([tp1,tn1,fp1,fn1,hr1])
#output2 = np.array([tp2,tn2,fp2,fn2,hr2])
#print output1
#print output2