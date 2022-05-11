# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:48:38 2022

@author: Sai Prathap
"""

def check(num):
    global it
    while(num != 1):
        if num %2 == 0:
            num = int(num/2)
        else:
            num = 3*num + 1
        print(num)
        it += 1
    print(num,it)
it = 0
check(256)