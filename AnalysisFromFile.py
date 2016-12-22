# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:23:12 2016

@author: jhan
"""
import numpy as np
import pandas as pd

def import_stats_file(filename):
    df = pd.read_csv(filename, sep=',')
    return df
    
df1 = import_stats_file('stats_type0_8_5.csv')  
#print df1
print  df1[0:3]
    
#    # init output virales
#    patternID = ''
#    endDate = ''
#    actualReturn = 0
#    mean = 0
#    variance = 0
#    median = 0
#    upside = 0
#    downside = 0
#    num_results = 0
#    
#    # pearson correlation
#    r_mean = np.corrcoef(df)