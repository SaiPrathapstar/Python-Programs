# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 12:27:47 2022

@author: Sai Prathap
"""

import os
import pandas as pd
os.chdir("C:\\Users\\Sai Prathap\\Downloads")
df = pd.read_csv("Toyota.csv" , index_col = 0 , na_values=['??','????'])