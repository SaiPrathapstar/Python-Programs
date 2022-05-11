import os
import numpy as np
import pandas as pd
os.chdir('C:\\Users\\Sai Prathap\\Downloads')
df = pd.read_excel('ASS.xlsx')
df
df.columns
df['Sbal'].value_counts()
df['Chist'].value_counts()
np.mean([5,6])
aa = np.where(df['Chist'] == 'dues not paid earlier').age
df['age'].where(df[])
aa = df[(df['Chist'] == 'dues not paid earlier')]['age']
np.mean(aa)
df2 = pd.get_dummies(df,drop_first = True)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x = df2.drop(['creditScore'] ,axis = 1, inplace = False)
y = df['creditScore']
x_train , x_test ,y_train,y_test = train_test_split(x,y,test_size = 0.25 , random_state = 1)
model = LinearRegression()
model.fit(x_train,y_train)
