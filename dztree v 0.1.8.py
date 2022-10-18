#!/usr/bin/env python
# This is the first version of my work 

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

def split_value(binary_series, c_series):
 """This function returns the value at which the series will be split"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 x=w1[rank_min-1]
 d='%'+str(6/10)+'f'
 x=float(d%x)
 return x

def rank_of_sv(binary_series, c_series):
 """This function returns the rank of the split value"""
 l=len(c_series)
 w=binary_series
 w1=[]
 for i in range(l):
  w1.append(float(c_series[i]))
 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]
 
 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,len(c_series)):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,len(c_series)):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1

 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1

 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 
 return rank_min

def number_inf_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_inf[rank_min-1]
 return x

def number_sup_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]

 rank_min=rank_of_min_value(GiNi_total)
 x=number_sup_or_equal[rank_min-1]
 
 return x

def number_1_inf_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_1_inf[rank_min-1]
 return x

def number_0_inf_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_0_inf[rank_min-1]
 
 return x

def number_1_sup_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 rank_min=rank_of_min_value(GiNi_total)
 x=number_1_sup_or_equal[rank_min-1]
 return x

def number_0_sup_to_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
  
 rank_min=rank_of_min_value(GiNi_total)
 x=number_0_sup_or_equal[rank_min-1]
 return x

def GiNi_of_split_value(binary_series, c_series):
 """Function"""
 l=len(c_series)
 w=binary_series
 w1 = []
 for i in range(l):
  w1.append(float(c_series[i]))

 z=list(map(lambda x,y:(x,y), w,w1))
 zz=sorted(z, key=itemgetter(1))
 w=[zz[i][0] for i in range(l)]
 w1=[zz[i][1] for i in range(l)]

 number_inf=[]
 
 number_inf.append(1)
 for i in range(1,l):
  number_inf.append(i)
 
 number_sup_or_equal=[l-i for i in range(l)]
 
 number_1_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='1':
    number_1_inf[i]+=1
 
 number_0_inf=[0 for i in range(l)]
 for i in range(1,l):
  for j in range(i):
   if w[j]=='0':
    number_0_inf[i]+=1
 
 number_1_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='1':
    number_1_sup_or_equal[i]+=1
 
 number_0_sup_or_equal=[0 for i in range(l)]
 for i in range(l):
  for j in range(i, len(number_sup_or_equal)):
   if w[j]=='0':
    number_0_sup_or_equal[i]+=1

 GiNi_1_inf=[(number_1_inf[i]/number_inf[i])*(number_1_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_0_inf=[(number_0_inf[i]/number_inf[i])*(number_0_inf[i]/number_inf[i]) for i in range(l)]
 GiNi_inf=[1-(GiNi_1_inf[i]+GiNi_0_inf[i]) for i in range(l)]
 GiNi_1_sup_or_equal=[(number_1_sup_or_equal[i]/number_sup_or_equal[i])*(number_1_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_0_sup_or_equal=[(number_0_sup_or_equal[i]/number_sup_or_equal[i])*(number_0_sup_or_equal[i]/number_sup_or_equal[i]) for i in range(l)]
 GiNi_sup_or_equal=[1-(GiNi_1_sup_or_equal[i]+GiNi_0_sup_or_equal[i]) for i in range(l)]
 GiNi_total=[(number_inf[i]*GiNi_inf[i]+number_sup_or_equal[i]*GiNi_sup_or_equal[i])/(number_inf[i]+number_sup_or_equal[i]) for i in range(l)]
 
 m=min(GiNi_total) 
 return m

def node(binary_series, c_series):
 """Function"""
 root1=Tk()
 root1.configure(background='white')
 gg=split_value(binary_series, c_series)
 nb_inf=number_inf_to_split_value(binary_series, c_series)
 nb_sup=number_sup_to_split_value(binary_series, c_series)
 nb_1_inf=number_1_inf_to_split_value(binary_series, c_series)
 nb_0_inf=number_0_inf_to_split_value(binary_series, c_series)
 nb_1_sup=number_1_sup_to_split_value(binary_series, c_series)
 nb_0_sup=number_0_sup_to_split_value(binary_series, c_series)
 prob_inf=nb_1_inf/(nb_1_inf+nb_0_inf)
 prob_sup=nb_1_sup/(nb_1_sup+nb_0_sup)
 g=GiNi_of_split_value(binary_series, c_series)
 d='%'+str(6/10)+'f'
 gg=d%gg
 prob_inf=d%prob_inf
 prob_sup=d%prob_sup
 g=d%g
 rank_min=rank_of_sv(binary_series, c_series)
 root1.title("Node")
 Label(root1, text="Split value (sv) = "+str(gg)).pack(pady=0)
 Label(root1, text="sv rank          = "+str(rank_min)).pack(pady=0)
 Label(root1, text="GiNi          = "+str(g)).pack(pady=0)
 Label(root1, text="______________________________________").pack(pady=0)
 Label(root1, text=".                    < sv  ||   >= sv").pack(pady=0)
 Label(root1, text="Binary = 1 :    "+str(nb_1_inf)+"    ||    "+str(nb_1_sup)+"       ").pack(pady=0)
 Label(root1, text="Binary = 0 :    "+str(nb_0_inf)+"    ||    "+str(nb_0_sup)+"       ").pack(pady=0)
 Label(root1, text="Prob(=1) :    "+str(prob_inf)+"    ||    "+str(prob_sup)+"       ").pack(pady=0)
 return root1
 
def G_series_ranked_N(binary_series, ordr, *c_series):
 """Function description"""
 G_values=[]
 for i in range(len(c_series)):
  G_values.append((i+1, GiNi_of_split_value(binary_series, c_series[i])))
 z=sorted(G_values, key=itemgetter(1))
 x=z[ordr-1][0]
 return x

def Series_ranked_N(binary_series, ordr, *c_series):
 """Function description"""
 G_values=[]
 for i in range(len(c_series)):
  G_values.append((i+1, GiNi_of_split_value(binary_series, c_series[i])))
 z=sorted(G_values, key=itemgetter(1))
 new_series=[]   
 new_series=list(map(lambda x: float(x), c_series[z[ordr-1][0]-1]))
 return new_series

def sum_vect(vector):
 vector=list(map(lambda x: float(x), vector))
 s=int(sum(vector))
 return s

def number_1_node_0(binary_series, *c_series):
 """Number of y=1"""
 print("Node____0...")
 return sum_vect(binary_series)

def number_0_node_0(binary_series, *c_series):
 """Number of y=1"""
 print("Node____0...")
 s=len(binary_series)-sum_vect(binary_series)
 return s

def number_1_node_1(binary_series, *c_series):
 """Node of >= sv instances whose y==1"""
 start=datetime.now()
 l=len(binary_series)
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 sv=split_value(binary_series, ranked_1_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if x==0 else 0, binary_series))
 high_to_sv_series=[1 if ranked_1_series[i]>=sv else 0 for i in range(len(binary_series))]
 high_to_sv_and_1=list(map(lambda x,y: int(x)*int(y), high_to_sv_series, binary_series_1))
 ss=sum_vect(high_to_sv_and_1)
 
 print("Node____1...", datetime.now()-start)
 return ss

def number_0_node_1(binary_series, *c_series):
 """Node of >= sv instances whose y==0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 sv=split_value(binary_series, ranked_1_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series=[1 if ranked_1_series[i]>=sv else 0 for i in range(l)]
 high_to_sv_and_0=list(map(lambda x,y: int(x)*int(y), high_to_sv_series, binary_series_0))
 ss=sum_vect(high_to_sv_and_0)
 
 print("Node____1...", datetime.now()-start)
 return ss

def number_1_node_2(binary_series, *c_series):
 """Node of < sv instances whose y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 sv=split_value(binary_series, ranked_1_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 low_to_sv_series=[1 if ranked_1_series[i]<sv else 0 for i in range(l)]
 low_to_sv_and_1=list(map(lambda x,y: int(x)*int(y), low_to_sv_series, binary_series_1))
 ss=sum_vect(low_to_sv_and_1)
 
 print("Node____2...", datetime.now()-start)
 return ss
 
def number_0_node_2(binary_series, *c_series):
 """Node of < sv instances whose y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 sv=split_value(binary_series, ranked_1_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 low_to_sv_series=[1 if ranked_1_series[i]<sv else 0 for i in range(l)]
 low_to_sv_and_0=list(map(lambda x,y: int(x)*int(y), low_to_sv_series, binary_series_0))
 ss=sum_vect(low_to_sv_and_0)
 
 print("Node____2...", datetime.now()-start)
 return ss

def number_1_node_3(binary_series, *c_series):
 """Node of (ranked 1 >= sv) and (ranked 2 >= sv) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_high_to_sv_and_1=list(map(lambda x,y,z: int(x)*int(y)*int(z), high_to_sv_series_1, high_to_sv_series_2, binary_series_1))
 ss=sum_vect(high_high_to_sv_and_1)
 
 print("Node____3...", datetime.now()-start)
 return ss

def number_0_node_3(binary_series, *c_series):
 """Node of (ranked 1 >= sv) and (ranked 2 >= sv) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_high_to_sv_and_0=list(map(lambda x,y,z: int(x)*int(y)*int(z), high_to_sv_series_1, high_to_sv_series_2, binary_series_0))
 ss=sum_vect(high_high_to_sv_and_0)
 
 print("Node____3...", datetime.now()-start)
 return ss

def number_1_node_4(binary_series, *c_series):
 """Node of (ranked 1 >= sv) and (ranked 2 < sv) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 
 high_low_to_sv_and_1=list(map(lambda x,y,z: int(x)*int(y)*int(z), high_to_sv_series_1, low_to_sv_series_2, binary_series_1))
 ss=sum_vect(high_low_to_sv_and_1)
 
 print("Node____4...", datetime.now()-start)
 return ss

def number_0_node_4(binary_series, *c_series):
 """Node of (ranked 1 >= sv) and (ranked 2 < sv) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_low_to_sv_and_0=list(map(lambda x,y,z: int(x)*int(y)*int(z), high_to_sv_series_1, low_to_sv_series_2, binary_series_0))
 ss=sum_vect(high_low_to_sv_and_0)
 
 print("Node____4...", datetime.now()-start)
 return ss

def number_1_node_5(binary_series, *c_series):
 """Node of (ranked 1 < sv) and (ranked 2 >= sv) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_high_to_sv_and_1=list(map(lambda x,y,z: int(x)*int(y)*int(z), low_to_sv_series_1, high_to_sv_series_2, binary_series_1))
 ss=sum_vect(low_high_to_sv_and_1)
 
 print("Node____5...", datetime.now()-start)
 return ss

def number_0_node_5(binary_series, *c_series):
 """Node of (ranked 1 < sv) and (ranked 2 >= sv) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)] 
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_high_to_sv_and_0=list(map(lambda x,y,z: int(x)*int(y)*int(z), low_to_sv_series_1, high_to_sv_series_2, binary_series_0))
 ss=sum_vect(low_high_to_sv_and_0)
 
 print("Node____5...", datetime.now()-start)
 return ss

def number_1_node_6(binary_series, *c_series):
 """Node of (ranked 1 < sv) and (ranked 2 < sv) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series)) 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_low_to_sv_and_1=list(map(lambda x,y,z: int(x)*int(y)*int(z), low_to_sv_series_1, low_to_sv_series_2, binary_series_1))
 ss=sum_vect(low_low_to_sv_and_1)
 
 print("Node____6...", datetime.now()-start)
 return ss

def number_0_node_6(binary_series, *c_series):
 """Node of (ranked 1 < sv) and (ranked 2 < sv) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_low_to_sv_and_0=list(map(lambda x,y,z: int(x)*int(y)*int(z), low_to_sv_series_1, low_to_sv_series_2, binary_series_0))
 ss=sum_vect(low_low_to_sv_and_0)
 
 print("Node____6...", datetime.now()-start)
 return ss

def number_1_node_7(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 2 >= sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 H_H_H_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, binary_series_1))
 ss=sum_vect(H_H_H_to_sv_and_1)
 print("Node____7...", datetime.now()-start)
 return ss

def number_0_node_7(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 2 >= sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))

 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 H_H_H_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, binary_series_0))
 ss=sum_vect(H_H_H_to_sv_and_0)
 print("Node____7...", datetime.now()-start)
 return ss

def number_1_node_8(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 2 <= sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 H_H_L_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, binary_series_1))
 ss=sum_vect(H_H_L_to_sv_and_1)
 print("Node____8...", datetime.now()-start)
 return ss

def number_0_node_8(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 2 <= sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 H_H_L_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, binary_series_0))
 ss=sum_vect(H_H_L_to_sv_and_0)
 print("Node____8...", datetime.now()-start)
 return ss

def number_1_node_9(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))

 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 H_L_H_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, binary_series_1))
 ss=sum_vect(H_L_H_to_sv_and_1)
 print("Node____9...", datetime.now()-start)
 return ss

def number_0_node_9(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 H_L_H_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, binary_series_0))
 ss=sum_vect(H_L_H_to_sv_and_0)
 print("Node____9...", datetime.now()-start)
 return ss

def number_1_node_10(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 H_L_L_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, binary_series_1))
 ss=sum_vect(H_L_L_to_sv_and_1)
 print("Node____10...", datetime.now()-start)
 return ss

def number_0_node_10(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 H_L_L_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, binary_series_0))
 ss=sum_vect(H_L_L_to_sv_and_0)
 print("Node____10...", datetime.now()-start)
 return ss

def number_1_node_11(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 L_H_H_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, binary_series_1))
 ss=sum_vect(L_H_H_to_sv_and_1)
 print("Node____11...", datetime.now()-start)
 return ss

def number_0_node_11(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 L_H_H_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, binary_series_0))
 ss=sum_vect(L_H_H_to_sv_and_0)
 print("Node____11...", datetime.now()-start)
 return ss

def number_1_node_12(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series)) 
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 L_H_L_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, binary_series_1))
 ss=sum_vect(L_H_L_to_sv_and_1)
 print("Node____12...", datetime.now()-start)
 return ss

def number_0_node_12(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 L_H_L_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, binary_series_0))
 ss=sum_vect(L_H_L_to_sv_and_0)
 print("Node____12...", datetime.now()-start)
 return ss

def number_1_node_13(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 L_L_H_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, binary_series_1))
 ss=sum_vect(L_L_H_to_sv_and_1)
 print("Node____13...", datetime.now()-start)
 return ss

def number_0_node_13(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 
 L_L_H_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, binary_series_0))
 ss=sum_vect(L_L_H_to_sv_and_0)
 print("Node____13...", datetime.now()-start)
 return ss

def number_1_node_14(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 L_L_L_to_sv_and_1=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, binary_series_1))
 ss=sum_vect(L_L_L_to_sv_and_1)
 print("Node____14...", datetime.now()-start)
 return ss

def number_0_node_14(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 
 L_L_L_to_sv_and_0=list(map(lambda x,y,z,a: int(x)*int(y)*int(z)*int(a), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, binary_series_0))
 ss=sum_vect(L_L_L_to_sv_and_0)
 print("Node____14...", datetime.now()-start)
 return ss

def number_1_node_15(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_H_H_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_H_H_H_to_sv_and_1)
 print("Node____15...", datetime.now()-start)
 return ss

def number_0_node_15(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_H_H_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_H_H_H_to_sv_and_0)
 print("Node____15...", datetime.now()-start)
 return ss

def number_1_node_16(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_H_H_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_H_H_L_to_sv_and_1)
 print("Node____16...", datetime.now()-start)
 return ss

def number_0_node_16(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_H_H_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_H_H_L_to_sv_and_0)
 print("Node____16...", datetime.now()-start)
 return ss

def number_1_node_17(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_H_L_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_H_L_H_to_sv_and_1)
 print("Node____17...", datetime.now()-start)
 return ss

def number_0_node_17(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_H_L_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_H_L_H_to_sv_and_0)
 print("Node____17...", datetime.now()-start)
 return ss

def number_1_node_18(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_H_L_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_H_L_L_to_sv_and_1)
 print("Node____18...", datetime.now()-start)
 return ss

def number_0_node_18(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_H_L_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_H_L_L_to_sv_and_0)
 print("Node____18...", datetime.now()-start)
 return ss

def number_1_node_19(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_L_H_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_L_H_H_to_sv_and_1)
 print("Node____19...", datetime.now()-start)
 return ss

def number_0_node_19(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_L_H_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_L_H_H_to_sv_and_0)
 print("Node____19...", datetime.now()-start)
 return ss

def number_1_node_20(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_L_H_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_L_H_L_to_sv_and_1)
 print("Node____20...", datetime.now()-start)
 return ss

def number_0_node_20(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_L_H_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_L_H_L_to_sv_and_0)
 print("Node____20...", datetime.now()-start)
 return ss

def number_1_node_21(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_L_L_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_L_L_H_to_sv_and_1)
 print("Node____21...", datetime.now()-start)
 return ss

def number_0_node_21(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 H_L_L_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_L_L_H_to_sv_and_0)
 print("Node____21...", datetime.now()-start)
 return ss

def number_1_node_22(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))

 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_L_L_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(H_L_L_L_to_sv_and_1)
 print("Node____22...", datetime.now()-start)
 return ss

def number_0_node_22(binary_series, *c_series):
 """Node of (ranked 1 >= sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 high_to_sv_series_1=[1 if ranked_1_series[i]>=sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 H_L_L_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), high_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(H_L_L_L_to_sv_and_0)
 print("Node____22...", datetime.now()-start)
 return ss

def number_1_node_23(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_H_H_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_H_H_H_to_sv_and_1)
 print("Node____23...", datetime.now()-start)
 return ss

def number_0_node_23(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series)) 
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv3 else 0 for i in range(l)]
 
 L_H_H_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_H_H_H_to_sv_and_0)
 print("Node____23...", datetime.now()-start)
 return ss

def number_1_node_24(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_H_H_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_H_H_L_to_sv_and_1)
 print("Node____24...", datetime.now()-start)
 return ss

def number_0_node_24(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series)) 
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_H_H_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_H_H_L_to_sv_and_0)
 print("Node____24...", datetime.now()-start)
 return ss

def number_1_node_25(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_H_L_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_H_L_H_to_sv_and_1)
 print("Node____25...", datetime.now()-start)
 return ss

def number_0_node_25(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_H_L_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_H_L_H_to_sv_and_0)
 print("Node____25...", datetime.now()-start)
 return ss

def number_1_node_26(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_H_L_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_H_L_L_to_sv_and_1)
 print("Node____26...", datetime.now()-start)
 return ss

def number_0_node_26(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 >= sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 high_to_sv_series_2=[1 if ranked_2_series[i]>=sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_H_L_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, high_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_H_L_L_to_sv_and_0)
 print("Node____26...", datetime.now()-start)
 return ss

def number_1_node_27(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_L_H_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_L_H_H_to_sv_and_1)
 print("Node____27...", datetime.now()-start)
 return ss

def number_0_node_27(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_L_H_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_L_H_H_to_sv_and_0)
 print("Node____27...", datetime.now()-start)
 return ss

def number_1_node_28(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_L_H_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_L_H_L_to_sv_and_1)
 print("Node____28...", datetime.now()-start)
 return ss

def number_0_node_28(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 >= sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 high_to_sv_series_3=[1 if ranked_3_series[i]>=sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_L_H_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, high_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_L_H_L_to_sv_and_0)
 print("Node____28...", datetime.now()-start)
 return ss

def number_1_node_29(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_L_L_H_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_L_L_H_to_sv_and_1)
 print("Node____29...", datetime.now()-start)
 return ss

def number_0_node_29(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 >= sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 high_to_sv_series_4=[1 if ranked_4_series[i]>=sv4 else 0 for i in range(l)]
 
 L_L_L_H_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, high_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_L_L_H_to_sv_and_0)
 print("Node____29...", datetime.now()-start)
 return ss

def number_1_node_30(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=1"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_L_L_L_to_sv_and_1=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_1))
 ss=sum_vect(L_L_L_L_to_sv_and_1)
 print("Node____30...", datetime.now()-start)
 return ss

def number_0_node_30(binary_series, *c_series):
 """Node of (ranked 1 < sv1) and (ranked 2 < sv2) and (ranked 3 < sv3) and (ranked 4 < sv4) and y=0"""
 start=datetime.now()
 l=len(binary_series)
 
 ranked_1_series=Series_ranked_N(binary_series, 1, *c_series)
 ranked_2_series=Series_ranked_N(binary_series, 2, *c_series)
 ranked_3_series=Series_ranked_N(binary_series, 3, *c_series)
 ranked_4_series=Series_ranked_N(binary_series, 4, *c_series)
 
 sv1=split_value(binary_series, ranked_1_series)
 sv2=split_value(binary_series, ranked_2_series)
 sv3=split_value(binary_series, ranked_3_series)
 sv4=split_value(binary_series, ranked_4_series)
 
 binary_series_1=binary_series
 binary_series_0=list(map(lambda x: 1 if int(x)==0 else 0, binary_series))
 
 low_to_sv_series_1=[1 if ranked_1_series[i]<sv1 else 0 for i in range(l)]
 low_to_sv_series_2=[1 if ranked_2_series[i]<sv2 else 0 for i in range(l)]
 low_to_sv_series_3=[1 if ranked_3_series[i]<sv3 else 0 for i in range(l)]
 low_to_sv_series_4=[1 if ranked_4_series[i]<sv4 else 0 for i in range(l)]
 
 L_L_L_L_to_sv_and_0=list(map(lambda x,y,z,a,b: int(x)*int(y)*int(z)*int(a)*int(b), low_to_sv_series_1, low_to_sv_series_2, low_to_sv_series_3, low_to_sv_series_4, binary_series_0))
 ss=sum_vect(L_L_L_L_to_sv_and_0)
 print("Node____30...", datetime.now()-start)
 return ss

def draw_new_branch(tk_window, right, left):
 """The function does the tree extension with one branch"""

"""
label=tk.Label(text="()------", fg="red", bg="yellow")
label.pack()
btn=tk.Button(text="jhh", state="normal", padx=1, pady=5,  fg="red", bg="yellow")
btn.pack(side="left", padx=30, pady=20)

btn3=tk.Button(text="jhh3", state="normal", padx=1, pady=5, fg="red", bg="yellow")
#bnt3.grid(ticky=south)
#btn3.pack(side="right", padx=30, pady=5)

of=[None]*3
of[0]=tk.Frame(root, borderwidth=0)
of[1]=tk.Frame(root, borderwidth=1)
tk.Label(of[0], text="hhh").pack(side="left")
iff=[]
for relief in ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']:
 tk.Button(of[0], text=relief, state="normal", borderwidth=2, relief=relief).pack(side="left")
 #tk.Label(iff[0], text=relief, width=10).pack(side="left")
 #iff[0].pack(side="left", padx=7, pady=5)

for relief in ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']:
 tk.Button(of[1], text=relief, state="normal", borderwidth=2, relief=relief).pack(side="left")

of[0].pack()
of[0].place(x=50, y=50)
of[1].pack(side="left", padx=5, pady=7)
of[1].place(x=5, y=70)

x=tk.Tk()
btn2=tk.Button(text="BOUTON 2 ", state="normal", padx=1, pady=5, fg="red", bg="yellow", command=node(y, var1))
btn2.pack(side="right", padx=30, pady=20)
btn2.place(x=20, y=10)
"""

"""
G_series_ranked_N(y, 1, variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18], variables[19], variables[20], variables[21], variables[22], variables[23], variables[24], variables[25], variables[26], variables[27], variables[28], variables[29], variables[30], variables[31], variables[32], variables[33], variables[34], variables[35], variables[36], variables[37], variables[38], variables[39], variables[40], variables[41], variables[42], variables[43], variables[44], variables[45], variables[46], variables[47], variables[48], variables[49], variables[50], variables[51], variables[52], variables[53], variables[54], variables[55], variables[56], variables[57], variables[58], variables[59], variables[60], variables[61], variables[62], variables[63], variables[64], variables[65], variables[66], variables[67], variables[68], variables[69], variables[70], variables[71], variables[72], variables[73])
G_series_ranked_N(y, 2, variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18], variables[19], variables[20], variables[21], variables[22], variables[23], variables[24], variables[25], variables[26], variables[27], variables[28], variables[29], variables[30], variables[31], variables[32], variables[33], variables[34], variables[35], variables[36], variables[37], variables[38], variables[39], variables[40], variables[41], variables[42], variables[43], variables[44], variables[45], variables[46], variables[47], variables[48], variables[49], variables[50], variables[51], variables[52], variables[53], variables[54], variables[55], variables[56], variables[57], variables[58], variables[59], variables[60], variables[61], variables[62], variables[63], variables[64], variables[65], variables[66], variables[67], variables[68], variables[69], variables[70], variables[71], variables[72], variables[73])
G_series_ranked_N(y, 3, variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18], variables[19], variables[20], variables[21], variables[22], variables[23], variables[24], variables[25], variables[26], variables[27], variables[28], variables[29], variables[30], variables[31], variables[32], variables[33], variables[34], variables[35], variables[36], variables[37], variables[38], variables[39], variables[40], variables[41], variables[42], variables[43], variables[44], variables[45], variables[46], variables[47], variables[48], variables[49], variables[50], variables[51], variables[52], variables[53], variables[54], variables[55], variables[56], variables[57], variables[58], variables[59], variables[60], variables[61], variables[62], variables[63], variables[64], variables[65], variables[66], variables[67], variables[68], variables[69], variables[70], variables[71], variables[72], variables[73])
G_series_ranked_N(y, 4, variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18], variables[19], variables[20], variables[21], variables[22], variables[23], variables[24], variables[25], variables[26], variables[27], variables[28], variables[29], variables[30], variables[31], variables[32], variables[33], variables[34], variables[35], variables[36], variables[37], variables[38], variables[39], variables[40], variables[41], variables[42], variables[43], variables[44], variables[45], variables[46], variables[47], variables[48], variables[49], variables[50], variables[51], variables[52], variables[53], variables[54], variables[55], variables[56], variables[57], variables[58], variables[59], variables[60], variables[61], variables[62], variables[63], variables[64], variables[65], variables[66], variables[67], variables[68], variables[69], variables[70], variables[71], variables[72], variables[73])
"""
nodes=[None]*2
for i in range(2):
 nodes[i]=tk.LabelFrame(root, text="HiHHiGGGG")

root.grid_propagate(False)
nodes[0].grid(padx=10)
nodes[0].pack()

#of[0]=tk.Frame(root, borderwidth=1)
#x=number_0_node_30(y, variables[31], variables[27], variables[47], variables[33])
#print(x)
#print(GiNi_of_split_value(y, variables[31]))
N_series_ranked_1=G_series_ranked_N(y, 1, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
N_series_ranked_2=G_series_ranked_N(y, 2, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
N_series_ranked_3=G_series_ranked_N(y, 3, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
N_series_ranked_4=G_series_ranked_N(y, 4, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])

series_ranked_1=Series_ranked_N(y, 1, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
series_ranked_2=Series_ranked_N(y, 2, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
series_ranked_3=Series_ranked_N(y, 3, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])
series_ranked_4=Series_ranked_N(y, 4, variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18])

sv_ranked1=split_value(y, series_ranked_1)
sv_ranked2=split_value(y, series_ranked_2)
sv_ranked3=split_value(y, series_ranked_3)
sv_ranked4=split_value(y, series_ranked_4)

#series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4
#variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6], variables[7], variables[8], variables[9], variables[10], variables[11], variables[12], variables[13], variables[14], variables[15], variables[16], variables[17], variables[18]

n_1_nd_0=number_1_node_0(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_0=number_0_node_0(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_1=number_1_node_1(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_1=number_0_node_1(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_2=number_1_node_2(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_2=number_0_node_2(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_3=number_1_node_3(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_3=number_0_node_3(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_4=number_1_node_4(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_4=number_0_node_4(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_5=number_1_node_5(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_5=number_0_node_5(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_6=number_1_node_6(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_6=number_0_node_6(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_7=number_1_node_7(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_7=number_0_node_7(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_8=number_1_node_8(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_8=number_0_node_8(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_9=number_1_node_9(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_9=number_0_node_9(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_10=number_1_node_10(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_10=number_0_node_10(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_11=number_1_node_11(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_11=number_0_node_11(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_12=number_1_node_12(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_12=number_0_node_12(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_13=number_1_node_13(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_13=number_0_node_13(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_14=number_1_node_14(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_14=number_0_node_14(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_15=number_1_node_15(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_15=number_0_node_15(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_16=number_1_node_16(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_16=number_0_node_16(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_17=number_1_node_17(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_17=number_0_node_17(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_18=number_1_node_18(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_18=number_0_node_18(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_19=number_1_node_19(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_19=number_0_node_19(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_20=number_1_node_20(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_20=number_0_node_20(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_21=number_1_node_21(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_21=number_0_node_21(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_22=number_1_node_22(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_22=number_0_node_22(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_23=number_1_node_23(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_23=number_0_node_23(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_24=number_1_node_24(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_24=number_0_node_24(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_25=number_1_node_25(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_25=number_0_node_25(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_26=number_1_node_26(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_26=number_0_node_26(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_27=number_1_node_27(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_27=number_0_node_27(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_28=number_1_node_28(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_28=number_0_node_28(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_29=number_1_node_29(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_29=number_0_node_29(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_1_nd_30=number_1_node_30(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)
n_0_nd_30=number_0_node_30(y, series_ranked_1, series_ranked_2, series_ranked_3, series_ranked_4)

labels=[]

labels.append(tk.Label(root, text="{} = 1 : {}\n {} = 0 : {}".format(clns[0], n_1_nd_0, clns[0], n_0_nd_0), bg=rgb_back((238, 255, 204)), font='Century 14 bold'))
labels[0].pack()
labels[0].place(x=450, y=5)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_1, sv_ranked1, clns[0], n_1_nd_1, clns[0], n_0_nd_1), bg=rgb_back((238, 255, 204)), font='Century 12 bold'))
labels[1].pack()
labels[1].place(x=725, y=50)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_1, sv_ranked1, clns[0], n_1_nd_2, clns[0], n_0_nd_2), bg=rgb_back((238, 255, 204)), font='Century 12 bold'))
labels[2].pack()
labels[2].place(x=225, y=50)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_2, sv_ranked2, clns[0], n_1_nd_3, clns[0], n_0_nd_3), bg=rgb_back((238, 255, 204)), font='Century 10 bold'))
labels[3].pack()
labels[3].place(x=827 , y=120)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_2, sv_ranked2, clns[0], n_1_nd_4, clns[0], n_0_nd_4), bg=rgb_back((238, 255, 204)), font='Century 10 bold'))
labels[4].pack()
labels[4].place(x=612, y=120)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_2, sv_ranked2, clns[0], n_1_nd_5, clns[0], n_0_nd_5), bg=rgb_back((238, 255, 204)), font='Century 10 bold'))
labels[5].pack()
labels[5].place(x=347, y=120)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_2, sv_ranked2, clns[0], n_1_nd_6, clns[0], n_0_nd_6), bg=rgb_back((238, 255, 204)), font='Century 10 bold'))
labels[6].pack()
labels[6].place(x=102, y=120)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_7, clns[0], n_0_nd_7), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[7].pack()
labels[7].place(x=906, y=180)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_8, clns[0], n_0_nd_8), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[8].pack()
labels[8].place(x=794, y=180)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_9, clns[0], n_0_nd_9), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[9].pack()
labels[9].place(x=661, y=180)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_10, clns[0], n_0_nd_10), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[10].pack()
labels[10].place(x=549, y=180)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_11, clns[0], n_0_nd_11), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[11].pack()
labels[11].place(x=406, y=180)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_12, clns[0], n_0_nd_12), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[12].pack()
labels[12].place(x=285, y=180)

labels.append(tk.Label(root, text="N° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_13, clns[0], n_0_nd_13), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[13].pack()
labels[13].place(x=152, y=180)

labels.append(tk.Label(root, text="N° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_3, sv_ranked3, clns[0], n_1_nd_14, clns[0], n_0_nd_14), bg=rgb_back((238, 255, 204)), font='Century 8 bold'))
labels[14].pack()
labels[14].place(x=20, y=180)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_15, clns[0], n_0_nd_15), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[15].pack()
labels[15].place(x=920, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_16, clns[0], n_0_nd_16), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[16].pack()
labels[16].place(x=895, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_17, clns[0], n_0_nd_17), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[17].pack()
labels[17].place(x=800, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_18, clns[0], n_0_nd_18), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[18].pack()
labels[18].place(x=775, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_19, clns[0], n_0_nd_19), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[19].pack()
labels[19].place(x=670, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_20, clns[0], n_0_nd_20), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[20].pack()
labels[20].place(x=635, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_21, clns[0], n_0_nd_21), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[21].pack()
labels[21].place(x=550, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_22, clns[0], n_0_nd_22), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[22].pack()
labels[22].place(x=525, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_23, clns[0], n_0_nd_23), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[23].pack()
labels[23].place(x=420, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_24, clns[0], n_0_nd_24), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[24].pack()
labels[24].place(x=395, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_25, clns[0], n_0_nd_25), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[25].pack()
labels[25].place(x=295, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_26, clns[0], n_0_nd_26), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[26].pack()
labels[26].place(x=270, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_27, clns[0], n_0_nd_27), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[27].pack()
labels[27].place(x=160, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_28, clns[0], n_0_nd_28), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[28].pack()
labels[28].place(x=135, y=320)

labels.append(tk.Label(root, text="__  \n|\n|\nN° {} >= {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_29, clns[0], n_0_nd_29), bg=rgb_back((238, 255, 204)), font='Century 7 bold'))
labels[29].pack()
labels[29].place(x=20, y=225)

labels.append(tk.Label(root, text="  __\n|\n|\nN° {} < {}\n {} = 1 : {}\n {} = 0 : {}".format(N_series_ranked_4, sv_ranked4, clns[0], n_1_nd_30, clns[0], n_0_nd_30), bg=rgb_back((238, 255, 204)), fg=rgb_back((0, 70, 80)),font='Century 7 bold'))
labels[30].pack()
labels[30].place(x=5, y=320)

time_till_now()
root.mainloop()

os.system("pause")
