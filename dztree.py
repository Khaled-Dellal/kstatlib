#!/usr/bin/env python

# 10192022

import os
from datetime import datetime
from operator import itemgetter#, attrgetter

import pandas as pd
import numpy as np
from scipy.stats import f

start=datetime.now()

def rgb_back(rgb):
 return "#%02x%02x%02x" % rgb

def time_till_now():
 print(datetime.now()-start)

def read_txt(file_name):
 """This function assigns values found in the file 'file_name.txt' to a variable"""
 my_file=open(file_name+".txt", "r")
 y=my_file.read()
 y=y.split("\n")
 return y

def _drop_cols_too_nan(df, percent=50):
    """ Drop colums with too many missing values
    
    Parameters
    ----------
    
    df      : The name of pandas dataframe
    percent : Excessive percentage of missing values per column, default value = 50%
    
    Returns
    -------
    The dataframe itself but without columns whose number of missing values exceeds the \
    defined percentage in the parameter : 'percent'
    
    """
    for y in list(df.columns):
        if df[y].isnull().sum()>=(len(df)*(percent/100)):
            df.drop(columns=y)

def print_list(vector):
    """
    This function will display values of a list on the console

    Parameters:
    ----------
    vector : A list as argument
    
    Returns : 
    ---------
    Display the list value by value with line breaks
    
    """
    list(map(lambda x: print(x), vector))

def sort_series_up(w):
    """Sort a variable (list of digits) from min to max

    Parameters:
    ----------
    w : A list as argument
    
    Returns : 
    ---------
    Make w sorted from min to max
    
    """
    for i in range(len(w)-1):
           for j in range(len(w)-1):
                if w[j]>=w[j+1]:
                    v=w[j]
                    w[j]=w[j+1]
                    w[j+1]=v
                    del v

def min_value(series):
    """
    This function calculates the min value for a series
    """
    y=[]
    for i in range(len(series)):
        y.append(series[i])
    sort_series_up(y)
    x=y[0]
    del y
    return x
 
def rank_of_min_value(series):
    """
    This function returns the order min value of a series
    """
    return series.index(min(series))+1

  
def _convert_cols_float(df):
    """Converting columns from string into float"""
    for y in df.columns:
        if df[y].dtypes==object:
            df[y]=pd.to_numeric(df[y], errors='coerce')


def _drop_cols_too_nan(df, percent=50):
    """ Drop colums with too many missing values
    
    Parameters
    ----------
    
    df      : The name of pandas dataframe
    percent : Excessive percentage of missing values per column, default value = 50%
    
    Returns
    -------
    The dataframe itself but without columns whose number of missing values exceeds the \
    defined percentage in the parameter : 'percent'
    
    """
    for y in list(df.columns):
        if df[y].isnull().sum()>=(len(df)*(percent/100)):
            df.drop(columns=y)
 
 def _neta_correlation(b_v, c_v):
    """ Correlation quotient between a binary variable and continuous variable
    
    Parameters
    ----------
    
    b_v : Binary variable
    c_v : Continuous variable
    
    Returns
    -------
    
    Correlation value between the two variables
    """
    N=len(b_v)
    c_v_0=[c_v[i] for i in range(N) if b_v[i]==0]
    c_v_1=[c_v[i] for i in range(N) if b_v[i]==1]
    
    n0, n1 = len(c_v_0), len(c_v_1)
    m0, m1, m = np.mean(c_v_0), np.mean(c_v_1), np.mean(c_v)
    
    
    var0=n0*(m0-m)**2
    var1=n1*(m1-m)**2
    var_inter=(var0+var1)/N
    var_intra=np.var(c_v)
    
    rap_corr=var_inter/var_intra
    
    return rap_corr

def _F_statistic(b_v, c_v):
    """ docsring # to do 
    Parameters
    ----------
    
    Returns
    -------
    
    """
    N=len(c_v)
    corr = _neta_correlation(b_v, c_v)
    F = corr/((1-corr)/(N-2))
    
    return F

def _F_p_value(b_v, c_v):
    """
    """
    F = _F_statistic(b_v, c_v)
    p_value = 1-f.cdf(F, 1, N-2)
    
    return p_value

def _replace_nan_values(df, class_variable):
    """ Replaces nan values for the continuous variables by means of corresponding buckets within \
        default variable
    """
    if df.isnull().values.any():
        cols_with_nan=[]

        for y in df.columns:
            if df[y].isnull().values.any():
                cols_with_nan.append(y)

        dic={cols_with_nan[i] : 'mean' for i in range(len(cols_with_nan))}

        new_df=df.groupby(class_variable).agg(dict(dic))

        for col in cols_with_nan:
            for i in range(len(df)):
                if np.isnan(df[col][i]):
                    df[col][i]=new_df[col][df[class_variable][i]]
    return df


