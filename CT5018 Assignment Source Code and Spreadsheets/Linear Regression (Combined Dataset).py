#Importing modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

#Reading the CSV
DataFrame = pd.read_csv('CT5018 Combined Assignment Dataset.csv', index_col=0)

#Plotting a scatter plot, with Violence with injury on the x axis and Violence without injury on the y axis
DataFrame.plot(kind='scatter', x='Violence with injury', y='Violence without injury')

#Showing scatter plot
plt.show()

#Defining x axis of linear regression model and reshaping to fit model
ViolenceWithInjury = DataFrame["Violence with injury"].values.reshape(-1,1)

#Defining y axis of linear regression model
ViolenceWithoutInjury = DataFrame["Violence without injury"]

#Creating fitted linear regression model
LinearRegressionModel = LinearRegression().fit(ViolenceWithInjury,ViolenceWithoutInjury)

#Printing gradient of linear regression line
Gradient = LinearRegressionModel.coef_
print("The gradient is:",Gradient)

#Printing y intercept of linear regression line
YIntercept = LinearRegressionModel.intercept_
print("The y intercept is:",YIntercept)

#Generating a MatPlotLib figure to visualise the quantile regression model
Figure, Axes = plt.subplots(figsize=(10,8))

#Fitting the regression line onto the figure
YLine = lambda a, b: a + ViolenceWithInjury
y = YLine(YIntercept, Gradient)

#Adding the dataset values for violence with injury and violence without injury onto the figure
Axes.plot(ViolenceWithInjury, y, color="black")
Axes.scatter(ViolenceWithInjury, ViolenceWithoutInjury, alpha=.3)
Axes.set_xlabel("Violence with injury", fontsize=20)
Axes.set_ylabel("Violence without injury", fontsize=20)

#Showing the figure
plt.show()

#Taking violence with injury value to predict from user
UserValue = int(input("What violence with injury value would you like to predict the violence without injury value for?: "))

#Predicting value of violence without injury for given user value
Prediction = (Gradient*UserValue)+YIntercept

#Printing prediction
print("For a violence with injury value of",UserValue,", the expected violence without injury value is",Prediction)
