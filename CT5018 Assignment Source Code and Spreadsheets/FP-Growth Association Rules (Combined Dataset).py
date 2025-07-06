#Importing modules
import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules

#Reading CSV
DataFrame = pd.read_csv('CT5018 Association Rules Dataset.csv')

#Building the association rules model
FrequentItems = fpgrowth(DataFrame, min_support = 0.1, use_colnames = True)

#Collecting the association rules
AssociationRules = association_rules(FrequentItems, metric ="lift", min_threshold = 1)
AssociationRules = AssociationRules.sort_values(['confidence', 'lift'], ascending =[False, False])

#Filtering the association rules so that only those with a confidence of more than 60% and a lift of more than 1 show
FilteredRules = AssociationRules[(AssociationRules['confidence']>0.60) & (AssociationRules['lift']>1)]

#Ensuring that all columns are shown when association rules are printed
pd.pandas.set_option('display.max_columns', None)

#Cleaning the results
print(FilteredRules[['antecedents', 'consequents', 'lift']])
