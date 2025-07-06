#Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import seaborn as sns

#Reading CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Calculating covariance between data categories
Covariance = DataFrame.cov()

#Defining labels
Labels = ["Homicide", "Violence with injury", "Violence without injury", "Stalking and harassment", "Death and serious injury - Unlawful driving"]

#Constructing heatmap
sns.heatmap(Covariance, annot=True, fmt="g", xticklabels=Labels, yticklabels=Labels)

#Showing heatmap
plt.show()
