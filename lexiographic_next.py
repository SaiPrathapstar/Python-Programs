# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 11:05:38 2022

@author: Sai Prathap
"""

def nex(word):
    ind = -1
    l = [ord(ch) for ch in word]
    for i in range(len(l) - 1):
        if l[i] < l[i+1]:
            ind = i
        else:
            continue
    if ind == -1:
        return "this is already max string"
    for j in range(len(l) -1 , ind , -1):
        if l[j] > l[ind]:
            l[j],l[ind] = l[ind] , l[j]
            break
    l[ind + 1:] = l[len(l) -1 : ind :-1]
    y = []
    for x in l:
        y.append(chr(x))
    ans = "".join(y)
    return ans