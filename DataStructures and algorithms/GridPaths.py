# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:25:45 2022

@author: Sai Prathap
"""
#GridPaths with no hole naive recursion
def Paths(i,j):
    if i == 0 and j ==0:
        return(1)
    elif i == 0:
        return Paths(0,j-1)
    elif j == 0:
        return Paths(i-1,0)
    else:
        return Paths(i-1,j) + Paths(i,j-1)
ptable = {}
#Grid Paths with no hole using memoization
def MPaths(i,j):
    if str(i)+','+str(j) in ptable:
        return ptable[str(i)+","+str(j)]
    else:
        if i == 0 and j ==0:
            value = 1
        elif i == 0:
            value = MPaths(0,j-1)
        elif j == 0:
            value = MPaths(i-1,0)
        else:
            value = MPaths(i-1,j) + MPaths(i,j-1)
        ptable[str(i)+","+str(j)] = value
        return value