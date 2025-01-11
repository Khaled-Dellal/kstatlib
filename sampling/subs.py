import numpy as np 
import pandas as pd 

from scipy.stats import normaltest, shapiro
import matplotlib.pyplot as plt

def get_closest_values_to_mean(large_variable, size):
    
    m = np.mean(large_variable)
    distance = [abs(x - m) for x in large_variable]
    min_d=np.min(distance)
    min_d_idx = distance.index(min_d)
    first_nearest = large_variable[min_d_idx]
    
    our_sub_sample=[first_nearest]
    large_variable = large_variable[large_variable!=first_nearest]
    
    for i in range(1, size):
        m = np.mean(large_variable)
        distance = [abs(x - m) for x in large_variable[large_variable!=first_nearest]]
        min_d=np.min(distance)
        min_d_idx = distance.index(min_d)
        first_nearest = large_variable[min_d_idx]
        
        our_sub_sample.append(first_nearest)
        large_variable = large_variable[large_variable!=first_nearest]   
        
    return our_sub_sample

def ith_value_closest_mean_no_longer_normal(large_variable):
    
    p_v = []
    
    for i in range(3, 50):
        sample = get_closest_values_to_mean(large_variable, i)
        p_v.append(shapiro(sample)[1])
        
    del sample
    
    for i in range(len(p_v)):
        if p_v[i] < 0.1:
            ith = i
            break  
    
    return ith

def get_subsample_nearest_normal(large_variable):
    i = ith_value_closest_mean_no_longer_normal(large_variable)
    sample = get_closest_values_to_mean(large_variable, i)
    
    return sample

def _normalize_by_adding_one_value_from_larger(sub_sample, large_variable):
    
    sample = sub_sample
    
    large = [x for x in large_variable if (x in large_variable) & (x not in sample)]
    
    sample.append(None)
    
    shap = []
    
    for i in range(len(large)):
        
        sample[len(sample)-1] = large[i]
        
        shap.append(shapiro(sample)[1])
        
    del sample[len(sample) - 1] 
    distance = [x - 0.1 for x in shap]
    mx = np.max(distance)
    idx_max = distance.index(mx)
    result = large[idx_max]
    return result

def _normalize_by_adding_one_value_from_larger_2(sub_sample, large_variable):
    
    sample = sub_sample
    
    large = [x for x in large_variable if (x in large_variable) & (x not in sample)]
    
    sample.append(None)
    
    shap = []
    
    for i in range(len(large)):
        
        sample[len(sample)-1] = large[i]
        
        shap.append(normaltest(sample)[1])
        
    del sample[len(sample) - 1] 
    distance = [x - 0.05 for x in shap]
    mx = np.max(distance)
    idx_max = distance.index(mx)
    result = large[idx_max]
    return result

def get_subsample_not_mean_close_normal(sub_sample, large_variable, size):
    sample = sub_sample
    large = [x for x in large_variable if (x in large_variable) & (x not in sample)]

    for i in range(min(size, 50)):
        sample.append(_normalize_by_adding_one_value_from_larger(sample, large))
        large = [x for x in large if (x in large) & (x not in sample)]
    if size > 50:
        s = size-50
        for i in range(s):
            sample.append(_normalize_by_adding_one_value_from_larger_2(sample, large))
            large = [x for x in large if (x in large) & (x not in sample)]
    return sample

def get_normal_sample(large_variable, size):
    max_size = len(set(large_variable)) - 1
    assert max_size < size, f"Sub-sample max size cannot exceed {max_size}"
    sub_sample = get_subsample_nearest_normal(large_variable)
    s = size - len(sub_sample)
    if s == 0:
        sample = sub_sample
    else:
        sample = get_subsample_not_mean_close_normal(sub_sample, large_variable, s)
    return sample


