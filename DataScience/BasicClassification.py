import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
os.chdir('C:\\Users\\Sai Prathap\\Downloads')
data = pd.read_csv('income(1).csv',na_values=[' ?'])
data2 = data.copy()
data2 = data2.dropna(axis = 0)
cols = ['gender','race','JobType','nativecountry']
data2 = data2.drop(cols,axis = 1)
data2['SalStat'] = data2['SalStat'].map({' less than or equal to 50,000' : 0 , ' greater than 50,000' : 1})
data2 = pd.get_dummies(data2,drop_first=True)
features = list(set(list(data2.columns)) - set(['SalStat']))
y = data2['SalStat'].values
x = data2[features].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy_score(y_test,y_pred)
(y_pred != y_test).sum()
