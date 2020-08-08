"""
Event:IBM Hack challenge 2020
@team members: Barathkumar G  id:191cs138
               Ajay S         id:191cs110
               Dhanush s      id:191cs156
Guide name: Ms Malathi T AP/CSE
Mentor name : Mr Hemant Kumar Gahlot   AI Developer/IBM
              Ms Gayatri   AI Developer/IBM
"""#!/usr/bin/env python



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
dataset =pd.read_csv('finalpro.csv')
dataset
dataset.iloc[:,-2]
dataset.head()
dataset.head(10)
x= dataset.iloc[:,:2]
x
x.iloc[:,-1]
def convert_to_int(word):
    word_dict = {'E':1, 'W':2, 'N':3, 'S':4, 'NE':5, 'NW':6, 'SE':7, 'SW':8
                }
    return word_dict[word]
x.iloc[:,-1] = x.iloc[:,-1].apply(lambda a:convert_to_int(a))
x.iloc[:,-1]
dataset.iloc[:,-2] = dataset.iloc[:,-2].apply(lambda a:convert_to_int(a))
dataset.iloc[:,-2]
dataset
x
x= dataset.iloc[:,:2].values
y= dataset.iloc[:,2:].values
y
dataset.corr()
from sklearn.model_selection import train_test_split                #previously cros_validation was used in sklearn
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=10)
x_test
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict=lr.predict(x_test)
print(y_predict)
x_train
x_test
pickle.dump(lr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))

