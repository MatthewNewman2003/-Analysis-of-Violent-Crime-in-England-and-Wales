#Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns

#Reading CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Constructing heatmap
sns.heatmap(DataFrame.corr(), cmap="RdYlGn", linewidths=0.30)

#Showing heatmap
plt.show()
