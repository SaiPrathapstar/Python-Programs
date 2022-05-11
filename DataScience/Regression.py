import pandas as pd
import numpy as np
import seaborn as sns
sns.set(rc= {'figure.figsize' : (11.7,8.27)})
cars_data = pd.read_csv('C:\\Users\\Sai Prathap\\Downloads\\cars_sampled.csv')
cars = cars_data.copy()
cars.info()
cars.describe()
pd.set_option('display.float_format',lambda x: '%3f'%x)
cars.describe()
pd.set_option('display.max_columns',500)
cars.describe()
col = ['name' ,'dateCrawled','dateCreated','postalCode','lastSeen']
cars.drop_duplicates(keep='first',inplace=True)
cars.isnull().sum()
yearwise_count = cars['yearOfRegistration'].value_counts().sort_index()
sum(cars['yearOfRegistration'] > 2018) + sum(cars['yearOfRegistration'] < 1950)
sns.regplot(x = 'yearOfRegistration' , y = 'price',scatter = True , fit_reg=False , data = cars)
price_count = cars['price'].value_counts().sort_index()
sns.distplot(cars['price'])
cars['price'].describe()
sns.boxplot(y=cars['price'])
sum(cars['price'] > 150000) + sum(cars['price'] < 100)
power_count=cars['powerPS'].value_counts().sort_index()
sns.distplot(cars['powerPS'])
sns.regplot(x='powerPS',y = 'price',scatter = True , fit_reg = False , data = cars)
sum(cars['powerPS'] > 500) + sum(cars['powerPS'] < 10)
cars = cars[
    (cars.yearOfRegistration <= 2018)
   &(cars.yearOfRegistration >= 1950)
   &(cars.price >= 100)
   &(cars.price <= 150000)
   &(cars.powerPS >= 10)
   &(cars.powerPS <= 500)
    ]
cars['monthOfRegistration']/=12
cars['monthOfRegistration']
cars['Age'] =2018 -cars['yearOfRegistration'] + cars['monthOfRegistration']
cars.columns
cars['Age'] = round(cars['Age'] ,2)
cars['Age'].describe()
sns.distplot(cars['Age'])
sns.boxplot(y=cars['Age'])
sns.regplot(x = 'Age',y='price',scatter = True ,fit_reg = False , data = cars)
cars['seller'].value_counts()
pd.crosstab(cars['seller'] , columns = 'count' , normalize = True)
cars['offerType'].value_counts()
sns.countplot(x = 'offerType',data = cars)
cars['abtest'].value_counts()
sns.countplot(x = 'abtest',data = cars)
pd.crosstab(cars['abtest'] , columns = 'count',normalize = True)
sns.boxplot(x='abtest' , y = 'price' , data = cars)
cars['model'].value_counts()
pd.crosstab(cars['model'],columns='count',normalize= True)
sns.countplot(x='model',data = cars)
sns.boxplot(x='model',y='price',data=cars)
cars['kilometer'].value_counts().sort_index()
pd.crosstab(cars['kilometer'],'count',normalize=True)
sns.countplot(x='brand',data=cars)
sns.boxplot(x='brand',y='price',data=cars)
cars['notRepairedDamage'].value_counts()
sns.boxplot(x = 'notRepairedDamage', y = 'price' ,data = cars)
col = ['seller','offerType','abtest']
cars = cars.drop(col,axis=1)
cars_copy = cars.copy()
cars_select1 = cars.select_dtypes(exclude = [object])
correlation = cars_select1.corr()
round(correlation,3)
cars_select1.corr().loc[:,'price'].abs().sort_values(ascending = False)[1:]





from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error



cars_omit = cars.dropna(axis = 0)
cars_omit = pd.get_dummies(cars_omit,drop_first=True)
x1=cars_omit.drop(['price'],axis='columns',inplace=False)
