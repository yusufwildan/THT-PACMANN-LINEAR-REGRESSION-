# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:41:37 2021

@author: My Laptop
"""
import model
import numpy as np

from sklearn import datasets #USED DATA FROM BENCHMARK AS A SAMPLE

diabetes_X,diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-20]
diabetes_y_train = diabetes_y[:-20]

model = model.LinearReg()
model.fit(diabetes_X_train,diabetes_y_train)


#OUTPUT SAMPLE
print("Coefficients : ",model.coef)
print("Intercept : ", model.intercept)
print("Mean squared error : ", model.MSE)
print("Coefficient of determination : ", model.Coefdet)

print ("PREDICTION")
Y = model.predict(diabetes_X_train)
print(Y) # predict data when x2=1