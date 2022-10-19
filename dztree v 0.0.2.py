#!/usr/bin/env python

# 10192022

import os
import tkinter as tk
from datetime import datetime
from operator import itemgetter#, attrgetter
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
