#Importing Pandas
import pandas as pd

#Opening CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Reading variance of homicide
HomicideVariance = DataFrame["Homicide"].var()

#Printing variance of homicide
print("Variance of homicide:",HomicideVariance)

#Reading variance of violence with injury
ViolenceWithInjuryVariance = DataFrame["Violence with injury"].var()

#Printing variance of violence with injury
print("Variance of violence with injury: ",ViolenceWithInjuryVariance)

#Reading variance of violence without injury
ViolenceWithoutInjuryVariance = DataFrame["Violence without injury"].var()

#Printing variance of violence without injury
print("Variance of violence without injury: ",ViolenceWithoutInjuryVariance)

#Reading variance of stalking and harassment
StalkingVariance = DataFrame["Stalking and harassment"].var()

#Printing variance of stalking and harassment
print("Variance of stalking and harassment: ",StalkingVariance)

#Reading variance of death or serious injury through unlawful driving
UnlawfulDrivingVariance = DataFrame["Death or serious injury - unlawful driving"].var()

#Printing variance of death or serious injury through unlawful driving
print("Variance of unlawful driving: ",UnlawfulDrivingVariance)
