import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
os.chdir('C:\\Users\\Sai Prathap\\Downloads')
df = pd.read_csv('income(1).csv',na_values = [' ?'])
df = df.dropna(axis = 0)
df = df.drop(['gender','nativecountry','race','JobType'] , axis = 1)
df['SalStat'] = df['SalStat'].map({' less than or equal to 50,000' : 0 , ' greater than 50,000' : 1})
df = pd.get_dummies(df,drop_first = True)
x = df.iloc[:,0:-1].values
y = df.iloc[:,-1].values
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
model = KNeighborsClassifier(n_neighbors = 5)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy_score(y_pred,y_test)