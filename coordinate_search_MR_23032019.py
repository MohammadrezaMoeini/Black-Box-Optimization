#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:47:11 2019
@author: Mohammad Reza Moeini

Coordinate Search
For More information see DFO lectures:
    https://www.gerad.ca/Sebastien.Le.Digabel/MTH8418/

"""

import numpy as np


# =============================================================================
# Write or import your function - Here
# =============================================================================
def f(x):
    """The sphere function"""
    res = sum(x**2)
    return res

'For more functions'
from funcs_def import*
#f= beale 'a function from "funcs_def"
# =============================================================================
# Write or import your constraints - Here
# =============================================================================
def g(x):
    c =True
    return c


# =============================================================================
# Give all directions
# =============================================================================
def direction_P(n):
    '''
    n: number of variable
    P: a set includes all directions
    '''
    P=np.zeros((2*n,n))
    sp=np.eye(n)
    for i in range(0,n):
        P[i,:]=sp[i,:]
        P[i+n,:]=-sp[i,:]
    return P


# =============================================================================
# Coordinate search Algorithm
# =============================================================================

def coordinate_search(x0,delta0,ne_max):
    '''
    Returns f(x*) and x*
    x0: initial point
    delta0: initial delta (step)
    ne_max: maximum number of evaluation
    '''
    x=x0                        # initial point
    delta = delta0              # initial step
    n=len(x0)                   # number of variables
    P = direction_P(n)          # Set includes 2n directions
    Pft = np.zeros((2*n,n+1))   # Set includes 2n directions plus f(t)
    n_eval = 0
    for k in range(0,ne_max):
        n_eval +=1
        for i in range(0,2*n):
            t = x + delta*P[i]
            for j in range(0,n):
                Pft[i,j]=t[j]
            if g(t):
                Pft[i,-1]=f(t)
            else:               # Violated the conditions
                Pft[i,-1]=+10**20
        index_min=np.argmin(Pft[:,-1])
        if Pft[index_min,0]<f(x):
            x=Pft[index_min,0:n]
            
        else: #Local min
            delta=delta/2.0
    
    print('x0=',x0)
    print('delta0=',delta0)
    print('last delta_x=',delta)
    print('n_eval=', n_eval)
    print('x*=',x)
    print('f(x*)=',f(x))
    
    return x, f(x)


# =============================================================================
# Example
# =============================================================================
x0=np.array([5,5]);delta0=0.5;ne_max=100
coordinate_search(x0,delta0,ne_max)













