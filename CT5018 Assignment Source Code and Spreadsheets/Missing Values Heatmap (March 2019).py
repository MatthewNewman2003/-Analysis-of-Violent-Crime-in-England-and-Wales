#Importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
from matplotlib.pyplot import figure

#Declaring missing values
MissingValues = ["n/a", "na", "?", ".."]

#Opening CSV
DataFrame = pd.read_csv("policeforceareatablesyeendingmarch2019.csv", na_values=MissingValues)

#Declaring columns to be examined
Columns = DataFrame.columns[:27]

#Creating heatmap with colours denoting available data and missing data
Colours = ["#000099", "#ffff00"]
sns.heatmap(DataFrame[Columns].isnull(), cmap=sns.color_palette(Colours))

#Showing heatmap
plt.show()
