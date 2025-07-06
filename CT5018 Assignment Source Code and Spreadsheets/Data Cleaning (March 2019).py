#Importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
from matplotlib.pyplot import figure

#Defining missing values
MissingValues = ["n/a", "na", "?", ".."]

#Opening and reading CSV
DataFrame = pd.read_csv("policeforceareatablesyeendingmarch2019.csv", na_values=MissingValues)

#Displaying number of rows and columns within CSV
print("Shape: ",DataFrame.shape)

#Specifying empty columns to drop
ColumnsToDrop = ["Unnamed: 3","Unnamed: 22"]

#Dropping empty columns
DataFrame = DataFrame.drop(ColumnsToDrop, axis=1)

#Displaying number of rows and columns within CSV after cleaning for confirmation of successful missing data deletion
print("Shape: ",DataFrame.shape)

#Identifying amalgamated rows for wider areas to be dropped, as keeping these would make each area's data be counted twice and skew the spread of data
RowsToDrop = [0,1,2,6,12,17,23,28,35,38,44,50]

#Dropping amalgamated rows
DataFrame = DataFrame.drop(RowsToDrop, axis=0)

#Displaying number of rows and columns within CSV after cleaning for confirmation of successful amalgamated row deletion
print("Shape: ",DataFrame.shape)

#Creating boxplot of homicide
DataFrame.boxplot(column=["Homicide"])

#Showing boxplot
plt.show()

#Creating boxplot of violence with injury
DataFrame.boxplot(column=["Violence with injury"])

#Showing boxplot
plt.show()

#Creating boxplot of violence without injury
DataFrame.boxplot(column=["Violence without injury"])

#Showing boxplot
plt.show()

#Creating boxplot of stalking and harassment
DataFrame.boxplot(column=["Stalking and harassment"])

#Showing boxplot
plt.show()

#Creating boxplot of death and injury via unlawful driving
DataFrame.boxplot(column=["Death or serious injury - unlawful driving"])

#Showing boxplot
plt.show()

#Showing median value of homicide
print(DataFrame["Homicide"].quantile(0.50))

#Replacing outliers with median value of homicide
DataFrame["Homicide"] = np.where(DataFrame["Homicide"] > 38, 11, DataFrame["Homicide"])

#Creating new boxplot of homicide to confirm removal of original outliers
DataFrame.boxplot(column=["Homicide"])

#Showing new boxplot
plt.show()

#Showing median value of violence with injury
print(DataFrame["Violence with injury"].quantile(0.50))

#Replacing outliers with median value of violence with injury
DataFrame["Violence with injury"] = np.where(DataFrame["Violence with injury"] > 28828, 9207, DataFrame["Violence with injury"])

#Creating new boxplot of violence with injury to confirm removal of original outliers
DataFrame.boxplot(column=["Violence with injury"])

#Showing new boxplot
plt.show()

#Showing median value of violence with injury
print(DataFrame["Violence without injury"].quantile(0.50))

#Replacing outliers with median value of violence with injury
DataFrame["Violence without injury"] = np.where(DataFrame["Violence without injury"] > 36917, 10804, DataFrame["Violence without injury"])

#Creating new boxplot of violence with injury to confirm removal of original outliers
DataFrame.boxplot(column=["Violence without injury"])

#Showing new boxplot
plt.show()

#Showing median value of violence with injury
print(DataFrame["Stalking and harassment"].quantile(0.50))

#Replacing outliers with median value of violence with injury
DataFrame["Stalking and harassment"] = np.where(DataFrame["Stalking and harassment"] > 33095, 7925, DataFrame["Stalking and harassment"])

#Creating new boxplot of violence with injury to confirm removal of original outliers
DataFrame.boxplot(column=["Stalking and harassment"])

#Showing new boxplot
plt.show()

#Showing median value of violence with injury
print(DataFrame["Death or serious injury - unlawful driving"].quantile(0.50))

#Replacing outliers with median value of violence with injury
DataFrame["Death or serious injury - unlawful driving"] = np.where(DataFrame["Death or serious injury - unlawful driving"] > 61, 14, DataFrame["Death or serious injury - unlawful driving"])

#Creating new boxplot of violence with injury to confirm removal of original outliers
DataFrame.boxplot(column=["Death or serious injury - unlawful driving"])

#Showing new boxplot
plt.show()

#Confirming rows and columns before dropping irrelevant data
print("Shape: ",DataFrame.shape)

#Identifying irrelevant columns to drop
IrrelevantColumns = ["Area Code", "Area Name", "Unnamed: 2", "Violence against the person", "Sexual offences", "Robbery", "Theft offences", "Burglary", "Residential burglary", "Non-residential burglary", "Vehicle offences", "Theft from the person", "Bicycle theft", "Shoplifting", "Other theft offences", "Criminal damage and arson", "Drug offences", "Possession of weapons offences", "Public order offences", "Miscellaneous crimes"]

#Dropping irrelevant columns
DataFrame = DataFrame.drop(IrrelevantColumns, axis=1)

#Confirming rows and columns to confirm that irrelevant data has been removed
print("Shape: ",DataFrame.shape)

#Writing cleaned dataset to new CSV
DataFrame.to_csv("March 2019 Cleaned Dataset.csv")
