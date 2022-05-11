# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:09:41 2022

@author: Sai Prathap
"""

def mostActive(customers):
    # Write your code here
    active = []
    total = len(customers)
    customers_set = set(customers)
    for i in customers_set:
        if total / customers.count(i) >= 5:
            active.append(i)
    active = list(set(active))
    active.sort();
    return active;