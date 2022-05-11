import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os
os.chdir('C:\\Users\\Sai Prathap\\Downloads')
data = pd.read_csv('income(1).csv',na_values = [' ?'])
data.info()
data.isnull().sum()
summary_num = data.describe()
summary_cat = data.describe(include = 'O')
data2 = data.copy()
print(summary_num)
print(summary_cat)
data2 = data2.dropna(axis = 0)
data2.shape
data2.isnull().sum()
pd.crosstab(index=data2['SalStat'],columns = 'count',normalize = True)
pd.crosstab(index=data2['SalStat'],columns = data2['gender'],normalize = 'columns')
import matplotlib.pyplot as plt
plt.bar(data2['gender'],data2['SalStat'])
import seaborn as sns
sns.distplot(data2['age'],bins = 10)
sns.countplot(data2['gender'])
data2['SalStat'] = data2['SalStat'].map({' less than or equal to 50,000' : 0 , ' greater than 50,000' : 1})
np.unique(data2['SalStat'].values)
new_data = pd.get_dummies(data2,drop_first = True)
col = list(new_data.columns)
col
len(col)
features = list(set(col) - set(['SalStat']))
len(features)
y = new_data['SalStat'].values
x = new_data[features].values
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3,random_state=0)
model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy_score(y_pred,y_test)
confusion_matrix(y_pred,y_test).sum()
(y_pred != y_test).sum()
########Removing variables #############
np.unique(data2['SalStat'].values)
data3 = data.copy()
data3.info()
data3.shape
data3.isnull().sum()
data3 = data3.dropna(axis = 0)
data3.shape
data3['SalStat'] = data3['SalStat'].map({' greater than 50,000' : 1 , ' less than or equal to 50,000' : 0})
data3['SalStat'].values
cols = ['gender','nativecountry','race','JobType']
data3 = data3.drop(cols,axis = 1)
data3 = pd.get_dummies(data3,drop_first  = True)
len(data3.columns)
features = list(set(list(data3.columns)) - set(['SalStat']))
y = data3['SalStat'].values
x = data3[features].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
model2 = LogisticRegression()
model2.fit(x_train,y_train)
y_pred = model2.predict(x_test)
accuracy_score(y_pred , y_test)
(y_pred != y_test).sum()
