# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 10:59:10 2022

@author: Sai Prathap
"""
#GridPaths with holes using memoization
ptable = {}
def HMPaths(i,j,h):
    if str(i)+','+str(j) in ptable:
        return ptable[str(i)+","+str(j)]
    else:
        if i == 0 and j ==0:
            value = 1
        elif str(i)+","+str(j) == h:
            value = 0
        elif i == 0:
            value = HMPaths(0,j-1,h)
        elif j == 0:
            value = HMPaths(i-1,0,h)
        else:
            value = HMPaths(i-1,j,h) + HMPaths(i,j-1,h)
        ptable[str(i)+","+str(j)] = value
        return value