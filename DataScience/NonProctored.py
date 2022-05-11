# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:01:07 2022

@author: Sai Prathap
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('C:\\Users\\Sai Prathap\\Downloads\\bank_marketing.csv',na_values = ['unknown'] , index_col=0)
df.dropna(axis = 0 , inplace = True)
df.isnull().sum()
df.drop_duplicates(inplace = True)
df['deposit'] = df['deposit'].map({'yes' : 1} , {'no' : 0)
y = df['deposit'].values
df = pd.get_dummies(data = df[:-1],drop_first = True)
features = list(set(df.columns) - set(['deposit']))

x = df[features].values
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3 ,random_state=0)
model = LogisticRegression()
model.fit(x_train , y_train)
y_pred = model.predict(y_test)
accuracy_score(y_test, y_pred)