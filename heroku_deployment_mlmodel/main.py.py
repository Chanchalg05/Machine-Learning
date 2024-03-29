# pip install matplotlib


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pickle

df=pd.read_csv(r"C:\Users\chanc\python projects\Machine_learning\Salary_analysis\hiring.csv")


df["experience"].fillna(0,inplace=True)
df["test_score(out of 10)"].fillna(df["test_score(out of 10)"].mean(),inplace=True)

X=df.iloc[:,:3]

def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X["experience"]=X["experience"].apply(lambda x:convert_to_int(x))

y=df.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X,y)


#saving model to disk
import pickle
pickle.dump(regressor,open("model.pkl","wb"))

model=pickle.load(open("model.pkl","rb"))
print(model.predict([[2,9,6]]))