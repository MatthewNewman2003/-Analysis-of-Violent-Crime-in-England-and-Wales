#Importing modules
from scipy.stats import pearsonr
import pandas as pd

#Opening CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Reading data for violence with injury
WithInjury = DataFrame["Violence with injury"]

#Reading data for violence without injury
WithoutInjury = DataFrame["Violence without injury"]

#Conducting test upon data
TestStatistic, PValue = pearsonr(WithInjury, WithoutInjury)

#Outputting test statistic and p-value
print("Test statistic is: %.3f, P-value is: %.3f"%(TestStatistic, PValue))

#Outcome if confidence in alternative hypothesis is 90-95%
if 0.05 < PValue < 0.1:
    #Outputting that variables are somewhat likely to be correlated
    print("Marginally significant evidence to reject null hypothesis; variables are somewhat likely to be correlated.")
#Outcome if confidence in alternative hypothesis is 95-99%
elif 0.01 < PValue < 0.05:
    #Outputting that variables are likely to be correlated
    print("Significant evidence to reject null hypothesis; variables are likely to be correlated.")
#Outcome if confidence in alternative hypothesis is above 99%
elif PValue < 0.01:
    #Outputting that variables are very likely to be correlated
    print("Extremely significant evidence to reject null hypothesis; variables are very likely to be correlated.")
#Outcome if confidence in alternative hypothesis is below 90%
else:
    #Outputting that variables are unlikely to be correlated
    print("Insufficient evidence to reject null hypothesis; variables are unlikely to be correlated.")
    
