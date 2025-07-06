#Importing modules
import pandas as pd

#Specifying datasets to be merged
Dataset1 = pd.read_csv("March 2018 Cleaned Dataset.csv")
Dataset2 = pd.read_csv("March 2019 Cleaned Dataset.csv")

#Merging datasets together
CombinedDataset = pd.concat([Dataset1,Dataset2])

#Dropping unnamed column at the beginning
CombinedDataset.drop(["Unnamed: 0"], inplace=True, axis=1)

#Writing merged dataset to new CSV
CombinedDataset.to_csv("CT5018 Combined Assignment Dataset.csv")
