import statistics
import numpy as np
from scipy.stats import linregress, pearsonr, shapiro, norm, boxcox
import math

def get_W(Y):
    W = []
    W.append(Y)
    
    if any(e == 0 for e in Y):
        W.append([0 for i in range(len(Y))])
    else:
        W.append([1/x for x in Y])
    
    if any(e == 0 for e in Y):
        W.append([0 for i in range(len(Y))])
    else:
        W.append([math.log(x) for x in Y])
    
    if any(e == 0 for e in Y):
        W.append([0 for i in range(len(Y))])
    else:
        W.append([math.log(1/x) for x in Y])
    
    if any(e == 0 or e == 1 for e in Y):
        W.append([0 for i in range(len(Y))])
    else:
        W.append([1/math.log(x) for x in Y])
    
    if any((e - min(Y) - 1) == 0 for e in Y):
        W.append([0 for i in range(len(Y))])
    else:
        W.append([(max(Y) + 1 - x) / (x - min(Y) - 1) for x in Y])
        
    return W
    
def get_Z(X):
    Z = []
    Z.append(X)
    
    Z.append([x**2 for x in X])
    
    Z.append([x**3 for x in X])
    
    if any(e < 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([math.sqrt(x) for x in X])
        
    if any(e == 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([1/x for x in X])
    
    if any(e == 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([1/x**2 for x in X])
    
    if any(e == 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([1/x**3 for x in X])
        
    if any(e <= 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([1/math.sqrt(x) for x in X])
    
    if any(e <= 0 for e in X):
        Z.append([0 for x in X])
    else:
        Z.append([math.log(x) for x in X])
        
    return Z
models = {1 : 'Y = a * X + b',
          2 : 'Y = a * X^2 + b',
          3 : 'Y = a * X^3 + b',
          4 : 'Y = a * sqr(X) + b',
          5 : 'Y = a * 1/X + b',
          6 : 'Y = a * 1/X^2 + b',
          7 : 'Y = a * 1/X^3 + b',
          8 : 'Y = a * 1/sqr(X) + b',
          9 : 'Y = a * 1/X^b',
          10 : 'Y = a * X^b',
          11 : 'Y = exp{ a * X + b}',
          12 : 'Y = exp{ a * X^2 + b}',
          13 : 'Y = exp{ a * X^3 + b}',
          14 : 'Y = exp{ a * sqr(X) + b}',
          15 : 'Y = exp{ a * 1/X + b}',
          16 : 'Y = exp{ a * 1/X^2 + b}',
          17 : 'Y = exp{ a * 1/X^3 + b}',
          18 : 'Y = exp{ a * 1/sqr(X) + b}',
          19 : 'Y = 1/(a * X + b)',
          20 : 'Y = 1/(a * X^2 + b)',
          21 : 'Y = 1/(a * X^3 + b)',
          22 : 'Y = 1/(a * sqr(X) + b)',
          23 : 'Y = 1/(a * 1/X + b)',
          24 : 'Y = 1/(a * 1/X^2 + b)',
          25 : 'Y = 1/(a * 1/X^3 + b)',
          26 : 'Y = 1/(a * 1/sqr(X) + b)',
          27 : 'Y = 1/exp{ a * X + b}',
          28 : 'Y = 1/exp{ a * X^2 + b}',
          29 : 'Y = 1/exp{ a * X^3 + b}',
          30 : 'Y = 1/exp{ a * sqr(X) + b}',
          31 : 'Y = 1/exp{ a * 1/X + b}',
          32 : 'Y = 1/exp{ a * 1/X^2 + b}',
          33 : 'Y = 1/exp{ a * 1/X^3 + b}',
          34 : 'Y = 1/exp{ a * 1/sqr(X) + b}',
          35 : 'Y = exp{1/(a * X + b)}',
          36 : 'Y = exp{1/(a * X^2 + b)}',
          37 : 'Y = exp{1/(a * X^3 + b)}',
          38 : 'Y = exp{1/(a * sqr(X) + b)}',
          39 : 'Y = exp{1/(a * 1/X + b)}',
          40 : 'Y = exp{1/(a * 1/X^2 + b)}',
          41 : 'Y = exp{1/(a * 1/X^3 + b)}',
          42 : 'Y = exp{1/(a * 1/sqr(X) + b)}',
          43 : 'Y = Y_min + (Y_max - Y_min) / (1 + exp{ a * X + b})',          
         }
def get_pearson_corr_vect(Y, X):
    p_corr_vect = []
    W = get_W(Y)
    Z = get_Z(X)
    
    # 1 to 8
    p_corr_vect.append(pearsonr(W[0], Z[0])[0])
    p_corr_vect.append(pearsonr(W[0], Z[1])[0])
    p_corr_vect.append(pearsonr(W[0], Z[2])[0])
    p_corr_vect.append(pearsonr(W[0], Z[3])[0])
    p_corr_vect.append(pearsonr(W[0], Z[4])[0])
    p_corr_vect.append(pearsonr(W[0], Z[5])[0])
    p_corr_vect.append(pearsonr(W[0], Z[6])[0])
    p_corr_vect.append(pearsonr(W[0], Z[7])[0])
    
    # 9
    p_corr_vect.append(pearsonr(W[3], Z[8])[0])
    
    # 10 to 18
    p_corr_vect.append(pearsonr(W[2], Z[8])[0])
    p_corr_vect.append(pearsonr(W[2], Z[0])[0])
    p_corr_vect.append(pearsonr(W[2], Z[1])[0])
    p_corr_vect.append(pearsonr(W[2], Z[2])[0])
    p_corr_vect.append(pearsonr(W[2], Z[3])[0])
    p_corr_vect.append(pearsonr(W[2], Z[4])[0])
    p_corr_vect.append(pearsonr(W[2], Z[5])[0])
    p_corr_vect.append(pearsonr(W[2], Z[6])[0])
    p_corr_vect.append(pearsonr(W[2], Z[7])[0])
    
    # 19 to 26
    p_corr_vect.append(pearsonr(W[1], Z[0])[0])
    p_corr_vect.append(pearsonr(W[1], Z[1])[0])
    p_corr_vect.append(pearsonr(W[1], Z[2])[0])
    p_corr_vect.append(pearsonr(W[1], Z[3])[0])
    p_corr_vect.append(pearsonr(W[1], Z[4])[0])
    p_corr_vect.append(pearsonr(W[1], Z[5])[0])
    p_corr_vect.append(pearsonr(W[1], Z[6])[0])
    p_corr_vect.append(pearsonr(W[1], Z[7])[0])
    
    # 27 to 34
    p_corr_vect.append(pearsonr(W[3], Z[0])[0])
    p_corr_vect.append(pearsonr(W[3], Z[1])[0])
    p_corr_vect.append(pearsonr(W[3], Z[2])[0])
    p_corr_vect.append(pearsonr(W[3], Z[3])[0])
    p_corr_vect.append(pearsonr(W[3], Z[4])[0])
    p_corr_vect.append(pearsonr(W[3], Z[5])[0])
    p_corr_vect.append(pearsonr(W[3], Z[6])[0])
    p_corr_vect.append(pearsonr(W[3], Z[7])[0])
    
    # 35 to 42
    p_corr_vect.append(pearsonr(W[4], Z[0])[0])
    p_corr_vect.append(pearsonr(W[4], Z[1])[0])
    p_corr_vect.append(pearsonr(W[4], Z[2])[0])
    p_corr_vect.append(pearsonr(W[4], Z[3])[0])
    p_corr_vect.append(pearsonr(W[4], Z[4])[0])
    p_corr_vect.append(pearsonr(W[4], Z[5])[0])
    p_corr_vect.append(pearsonr(W[4], Z[6])[0])
    p_corr_vect.append(pearsonr(W[4], Z[7])[0])
    
    # 43
    p_corr_vect.append(pearsonr(W[5], Z[0])[0])
    
    p_corr_vect = [abs(x) for x in p_corr_vect]
    m = max(p_corr_vect)
    return p_corr_vect #models[p_corr_vect.index(m) + 1]
def get_spearman_corr_vect(Y, X):
    p_corr_vect = []
    W = get_W(Y)
    Z = get_Z(X)
    
    # 1 to 8
    p_corr_vect.append(spearmanr(W[0], Z[0])[0])
    p_corr_vect.append(spearmanr(W[0], Z[1])[0])
    p_corr_vect.append(spearmanr(W[0], Z[2])[0])
    p_corr_vect.append(spearmanr(W[0], Z[3])[0])
    p_corr_vect.append(spearmanr(W[0], Z[4])[0])
    p_corr_vect.append(spearmanr(W[0], Z[5])[0])
    p_corr_vect.append(spearmanr(W[0], Z[6])[0])
    p_corr_vect.append(spearmanr(W[0], Z[7])[0])
    
    # 9
    p_corr_vect.append(spearmanr(W[3], Z[8])[0])
    
    # 10 to 18
    p_corr_vect.append(spearmanr(W[2], Z[8])[0])
    p_corr_vect.append(spearmanr(W[2], Z[0])[0])
    p_corr_vect.append(spearmanr(W[2], Z[1])[0])
    p_corr_vect.append(spearmanr(W[2], Z[2])[0])
    p_corr_vect.append(spearmanr(W[2], Z[3])[0])
    p_corr_vect.append(spearmanr(W[2], Z[4])[0])
    p_corr_vect.append(spearmanr(W[2], Z[5])[0])
    p_corr_vect.append(spearmanr(W[2], Z[6])[0])
    p_corr_vect.append(spearmanr(W[2], Z[7])[0])
    
    # 19 to 26
    p_corr_vect.append(spearmanr(W[1], Z[0])[0])
    p_corr_vect.append(spearmanr(W[1], Z[1])[0])
    p_corr_vect.append(spearmanr(W[1], Z[2])[0])
    p_corr_vect.append(spearmanr(W[1], Z[3])[0])
    p_corr_vect.append(spearmanr(W[1], Z[4])[0])
    p_corr_vect.append(spearmanr(W[1], Z[5])[0])
    p_corr_vect.append(spearmanr(W[1], Z[6])[0])
    p_corr_vect.append(spearmanr(W[1], Z[7])[0])
    
    # 27 to 34
    p_corr_vect.append(spearmanr(W[3], Z[0])[0])
    p_corr_vect.append(spearmanr(W[3], Z[1])[0])
    p_corr_vect.append(spearmanr(W[3], Z[2])[0])
    p_corr_vect.append(spearmanr(W[3], Z[3])[0])
    p_corr_vect.append(spearmanr(W[3], Z[4])[0])
    p_corr_vect.append(spearmanr(W[3], Z[5])[0])
    p_corr_vect.append(spearmanr(W[3], Z[6])[0])
    p_corr_vect.append(spearmanr(W[3], Z[7])[0])
    
    # 35 to 42
    p_corr_vect.append(spearmanr(W[4], Z[0])[0])
    p_corr_vect.append(spearmanr(W[4], Z[1])[0])
    p_corr_vect.append(spearmanr(W[4], Z[2])[0])
    p_corr_vect.append(spearmanr(W[4], Z[3])[0])
    p_corr_vect.append(spearmanr(W[4], Z[4])[0])
    p_corr_vect.append(spearmanr(W[4], Z[5])[0])
    p_corr_vect.append(spearmanr(W[4], Z[6])[0])
    p_corr_vect.append(spearmanr(W[4], Z[7])[0])
    
    # 43
    p_corr_vect.append(spearmanr(W[5], Z[0])[0])
    
    p_corr_vect = [abs(x) for x in p_corr_vect]
    m = max(p_corr_vect)
    return p_corr_vect #models[p_corr_vect.index(m) + 1]
def get_b_vect(Y, X):
    b_vect = []
    W = get_W(Y)
    Z = get_Z(X)
    
    # 1 to 8
    b_vect.append(linregress(Z[0], W[0])[1])
    b_vect.append(linregress(Z[1], W[0])[1])
    b_vect.append(linregress(Z[2], W[0])[1])
    b_vect.append(linregress(Z[3], W[0])[1])
    b_vect.append(linregress(Z[4], W[0])[1])
    b_vect.append(linregress(Z[5], W[0])[1])
    b_vect.append(linregress(Z[6], W[0])[1])
    b_vect.append(linregress(Z[7], W[0])[1])
    b_vect.append(linregress(Z[8], W[3])[1])
    
    # 10 to 18
    b_vect.append(linregress(Z[8], W[2])[1])
    b_vect.append(linregress(Z[0], W[2])[1])
    b_vect.append(linregress(Z[1], W[2])[1])
    b_vect.append(linregress(Z[2], W[2])[1])
    b_vect.append(linregress(Z[3], W[2])[1])
    b_vect.append(linregress(Z[4], W[2])[1])
    b_vect.append(linregress(Z[5], W[2])[1])
    b_vect.append(linregress(Z[6], W[2])[1])
    b_vect.append(linregress(Z[7], W[2])[1])
    
    # 19 to 26
    b_vect.append(linregress(Z[0], W[1])[1])
    b_vect.append(linregress(Z[1], W[1])[1])
    b_vect.append(linregress(Z[2], W[1])[1])
    b_vect.append(linregress(Z[3], W[1])[1])
    b_vect.append(linregress(Z[4], W[1])[1])
    b_vect.append(linregress(Z[5], W[1])[1])
    b_vect.append(linregress(Z[6], W[1])[1])
    b_vect.append(linregress(Z[7], W[1])[1])
    
    # 27 to 34
    b_vect.append(linregress(Z[0], W[3])[1])
    b_vect.append(linregress(Z[1], W[3])[1])
    b_vect.append(linregress(Z[2], W[3])[1])
    b_vect.append(linregress(Z[3], W[3])[1])
    b_vect.append(linregress(Z[4], W[3])[1])
    b_vect.append(linregress(Z[5], W[3])[1])
    b_vect.append(linregress(Z[6], W[3])[1])
    b_vect.append(linregress(Z[7], W[3])[1])
    
    # 35 to 42
    b_vect.append(linregress(Z[0], W[4])[1])
    b_vect.append(linregress(Z[1], W[4])[1])
    b_vect.append(linregress(Z[2], W[4])[1])
    b_vect.append(linregress(Z[3], W[4])[1])
    b_vect.append(linregress(Z[4], W[4])[1])
    b_vect.append(linregress(Z[5], W[4])[1])
    b_vect.append(linregress(Z[6], W[4])[1])
    b_vect.append(linregress(Z[7], W[4])[1])
    
    # 43
    b_vect.append(linregress(Z[0], W[5])[1])
    
    #b_vect = [abs(x) for x in b_vect]
    m = max(b_vect)
    return b_vect #models[b_vect.index(m) + 1]
def get_a_vect(Y, X):
    a_vect = []
    W = get_W(Y)
    Z = get_Z(X)
    
    # 1 to 8
    a_vect.append(linregress(Z[0], W[0])[0])
    a_vect.append(linregress(Z[1], W[0])[0])
    a_vect.append(linregress(Z[2], W[0])[0])
    a_vect.append(linregress(Z[3], W[0])[0])
    a_vect.append(linregress(Z[4], W[0])[0])
    a_vect.append(linregress(Z[5], W[0])[0])
    a_vect.append(linregress(Z[6], W[0])[0])
    a_vect.append(linregress(Z[7], W[0])[0])
    a_vect.append(linregress(Z[8], W[3])[0])
    
    # 10 to 18
    a_vect.append(linregress(Z[8], W[2])[0])
    a_vect.append(linregress(Z[0], W[2])[0])
    a_vect.append(linregress(Z[1], W[2])[0])
    a_vect.append(linregress(Z[2], W[2])[0])
    a_vect.append(linregress(Z[3], W[2])[0])
    a_vect.append(linregress(Z[4], W[2])[0])
    a_vect.append(linregress(Z[5], W[2])[0])
    a_vect.append(linregress(Z[6], W[2])[0])
    a_vect.append(linregress(Z[7], W[2])[0])
    
    # 19 to 26
    a_vect.append(linregress(Z[0], W[1])[0])
    a_vect.append(linregress(Z[1], W[1])[0])
    a_vect.append(linregress(Z[2], W[1])[0])
    a_vect.append(linregress(Z[3], W[1])[0])
    a_vect.append(linregress(Z[4], W[1])[0])
    a_vect.append(linregress(Z[5], W[1])[0])
    a_vect.append(linregress(Z[6], W[1])[0])
    a_vect.append(linregress(Z[7], W[1])[0])
    
    # 27 to 34
    a_vect.append(linregress(Z[0], W[3])[0])
    a_vect.append(linregress(Z[1], W[3])[0])
    a_vect.append(linregress(Z[2], W[3])[0])
    a_vect.append(linregress(Z[3], W[3])[0])
    a_vect.append(linregress(Z[4], W[3])[0])
    a_vect.append(linregress(Z[5], W[3])[0])
    a_vect.append(linregress(Z[6], W[3])[0])
    a_vect.append(linregress(Z[7], W[3])[0])
    
    # 35 to 42
    a_vect.append(linregress(Z[0], W[4])[0])
    a_vect.append(linregress(Z[1], W[4])[0])
    a_vect.append(linregress(Z[2], W[4])[0])
    a_vect.append(linregress(Z[3], W[4])[0])
    a_vect.append(linregress(Z[4], W[4])[0])
    a_vect.append(linregress(Z[5], W[4])[0])
    a_vect.append(linregress(Z[6], W[4])[0])
    a_vect.append(linregress(Z[7], W[4])[0])
    
    # 43
    a_vect.append(linregress(Z[0], W[5])[0])
    
    #a_vect = [abs(x) for x in a_vect]
    m = max(a_vect)
    return a_vect #models[a_vect.index(m) + 1]
def get_model(Y, X):
    models = {1 : 'Y = {a} * X + {b}',
          2 : 'Y = {a} * X^2 + {b}',
          3 : 'Y = {a} * X^3 + {b}',
          4 : 'Y = {a} * sqr(X) + {b}',
          5 : 'Y = {a} * 1/X + {b}',
          6 : 'Y = {a} * 1/X^2 + {b}',
          7 : 'Y = {a} * 1/X^3 + {b}',
          8 : 'Y = {a} * 1/sqr(X) + {b}',
          9 : 'Y = {a} * 1/X^{b}',
          10 : 'Y = {a} * X^{b}',
          11 : 'Y = exp( {a} * X + {b})',
          12 : 'Y = exp( {a} * X^2 + {b})',
          13 : 'Y = exp( {a} * X^3 + {b})',
          14 : 'Y = exp( {a} * sqr(X) + {b})',
          15 : 'Y = exp( {a} * 1/X + {b})',
          16 : 'Y = exp( {a} * 1/X^2 + {b})',
          17 : 'Y = exp( {a} * 1/X^3 + {b})',
          18 : 'Y = exp( {a} * 1/sqr(X) + {b})',
          19 : 'Y = 1/({a} * X + {b})',
          20 : 'Y = 1/({a} * X^2 + {b})',
          21 : 'Y = 1/({a} * X^3 + {b})',
          22 : 'Y = 1/({a} * sqr(X) + {b})',
          23 : 'Y = 1/({a} * 1/X + {b})',
          24 : 'Y = 1/({a} * 1/X^2 + {b})',
          25 : 'Y = 1/({a} * 1/X^3 + {b})',
          26 : 'Y = 1/({a} * 1/sqr(X) + {b})',
          27 : 'Y = 1/exp( {a} * X + {b})',
          28 : 'Y = 1/exp( {a} * X^2 + {b})',
          29 : 'Y = 1/exp( {a} * X^3 + {b})',
          30 : 'Y = 1/exp( {a} * sqr(X) + {b})',
          31 : 'Y = 1/exp( {a} * 1/X + {b})',
          32 : 'Y = 1/exp( {a} * 1/X^2 + {b})',
          33 : 'Y = 1/exp( {a} * 1/X^3 + {b})',
          34 : 'Y = 1/exp( {a} * 1/sqr(X) + {b})',
          35 : 'Y = exp(1/({a} * X + {b}))',
          36 : 'Y = exp(1/({a} * X^2 + {b}))',
          37 : 'Y = exp(1/({a} * X^3 + {b}))',
          38 : 'Y = exp(1/({a} * sqr(X) + {b}))',
          39 : 'Y = exp(1/({a} * 1/X + {b}))',
          40 : 'Y = exp(1/({a} * 1/X^2 + {b}))',
          41 : 'Y = exp(1/({a} * 1/X^3 + {b}))',
          42 : 'Y = exp(1/({a} * 1/sqr(X) + {b}))',
          43 : 'Y = Y_min + (Y_max - Y_min) / (1 + exp( {a} * X + {b}))'}
    
    p_corr_vect = get_pearson_corr_vect(Y, X)
    a_vect = get_a_vect(Y, X)
    b_vect = get_b_vect(Y, X)
    m = max(p_corr_vect)
    return (models[p_corr_vect.index(m) + 1].format(a = a_vect[p_corr_vect.index(m)], b = b_vect[p_corr_vect.index(m)]), p_corr_vect[0], m)

class TimeSeriesForecast(list):
    """
    A class that inherits from a list and provides a forecast method
    based on the simple mean of the historical data.
    """
    def __init__(self, data, data_type='list'):
        """
        Initializes the TimeSeriesForecast object with an array-like data.

        Args:
            data: An iterable (e.g., list, tuple) of numeric data points.
            data_type: Can be either list or numpy
        """
        if data_type == 'list':
            super().__init__(data)  # Initialize the list base class
        elif data_type == 'numpy':
           super().__init__(list(data)) #convert the numpy to list and initialize the list base class
        else:
          raise ValueError("data_type should be either 'list' or 'numpy' ")

    def forecast(self, future_points, method="mean"):
       """
       Calculates a forecast for a given number of future points using the mean of historical data.

       Args:
           future_points: The number of future time points to forecast.

       Returns:
            A list containing the forecast values. The length of the
           list is equal to future_points.
       """
       if not self:
         return [None] * future_points # Handle empty list, return list of None values
       if future_points < 0:
         raise ValueError("future_points should be greater than or equal to 0.")

       if method == "mean":
          mean = statistics.mean(self)
          return [mean] * future_points
       else:
          raise ValueError("Method is not available")

    def add_data(self, new_data):
      """
      Adds new data to the time series

      Args:
          new_data: The data that needs to be added
      """
      if isinstance(new_data, list):
          self.extend(new_data)
      elif isinstance(new_data,(int, float)):
          self.append(new_data)
      else:
        raise ValueError("The provided data should be a list, int or float")
    
    def get_lambda_coef(self):
        x=[self[i] for i in range(len(self))]
        for i in range(len(x)-1):
            for j in range(len(x)-1):
                if x[j]>=x[j+1]:
                    z=x[j]
                    x[j]=x[j+1]
                    x[j+1]=z
        i=[j for j in range(1,len(x)+1)]
        f=[(i[j]-0.375)/(len(x)+0.25) for j in range(len(x))]
        u=[norm.ppf(f[i]) for i in range(len(x))]
            
        lambda_coef=0
        width=3
        step=width/6
        k=lambda_coef-width
        iteration=1
        while iteration<=15:
            r_vector=[]
            lambda_vect=[]
            while k<=lambda_coef+width:
                if k==0:
                    y=[np.log(i) for i in x]
                else:
                    y=[(i**k-1)/k for i in x]
                r_vector.append(pearsonr(y, u)[0])
                k+=step
            k=lambda_coef-width
            while k<=lambda_coef+width:
                lambda_vect.append(k)
                k+=step
            lambda_coef=lambda_vect[r_vector.index(max(r_vector))]
            width/=2
            step/=3
            k=lambda_coef-width
            iteration+=1
        return lambda_coef

if __name__ == '__main__':
    # Example usage
    data = [10, 12, 15, 13, 16, 18, 17]
    ts = TimeSeriesForecast(data)
    print(f"Original data: {ts}")

    forecast_steps = 3
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points using mean: {forecast}")

    forecast_steps = 5
    forecast = ts.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points using mean: {forecast}")

    # Example with an empty dataset
    ts_empty = TimeSeriesForecast([])
    forecast_steps = 2
    forecast = ts_empty.forecast(forecast_steps)
    print(f"Forecast for empty dataset for {forecast_steps} points: {forecast}")


    # Example Usage with numpy array
    data_np = np.array([20, 22, 25, 23, 26, 28, 27])
    ts_np = TimeSeriesForecast(data_np, data_type='numpy')
    print(f"Original data (numpy): {ts_np}")

    forecast_steps = 4
    forecast_np = ts_np.forecast(forecast_steps)
    print(f"Forecast for next {forecast_steps} points from numpy data: {forecast_np}")

    ts_np.add_data(29)
    print(f"New data is added: {ts_np}")
    ts_np.add_data([30,31,32])
    print(f"New data is added: {ts_np}")
