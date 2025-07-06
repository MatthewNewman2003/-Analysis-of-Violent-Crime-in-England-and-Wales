#Importing Pandas
import pandas as pd

#Reading CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Determining mean value of homicide
HomicideMean = DataFrame["Homicide"].mean()

#Printing mean value of homicide
print("Mean of homicide:",HomicideMean)

#Determining mean value of violence with injury
ViolenceWithInjuryMean = DataFrame["Violence with injury"].mean()

#Printing mean value of violence with injury
print("Mean of violence with injury: ",ViolenceWithInjuryMean)

#Determining mean value of violence without injury
ViolenceWithoutInjuryMean = DataFrame["Violence without injury"].mean()

#Printing mean value of violence without injury
print("Mean of violence without injury: ",ViolenceWithoutInjuryMean)

#Determining mean value of stalking and harassment
StalkingMean = DataFrame["Stalking and harassment"].mean()

#Printing mean value of stalking and harassment
print("Mean of stalking and harassment: ",StalkingMean)

#Determining mean value of unlawful driving
UnlawfulDrivingMean = DataFrame["Death or serious injury - unlawful driving"].mean()

#Printing mean value of unlawful driving
print("Mean of unlawful driving: ",UnlawfulDrivingMean)
