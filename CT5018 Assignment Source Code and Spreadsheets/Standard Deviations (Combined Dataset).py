#Importing libraries
import pandas as pd

#Opening CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Reading standard deviation of homicide
HomicideSDev = DataFrame["Homicide"].std()

#Printing standard deviation of homicide
print("Standard deviation of homicide:",HomicideSDev)

#Reading standard deviation of violence with injury
ViolenceWithInjurySDev = DataFrame["Violence with injury"].std()

#Printing standard deviation of violence with injury
print("Standard deviation of violence with injury: ",ViolenceWithInjurySDev)

#Reading standard deviation of violence without injury
ViolenceWithoutInjurySDev = DataFrame["Violence without injury"].std()

#Printing standard deviation of violence without injury
print("Standard deviation of violence without injury: ",ViolenceWithoutInjurySDev)

#Reading standard deviation of stalking and harassment
StalkingSDev = DataFrame["Stalking and harassment"].std()

#Printing standard deviation of stalking and harassment
print("Standard deviation of stalking and harassment: ",StalkingSDev)

#Reading standard deviation of death or serious injury through unlawful driving
UnlawfulDrivingSDev = DataFrame["Death or serious injury - unlawful driving"].std()

#Printing standard deviation of death or serious injury through unlawful driving
print("Standard deviation of unlawful driving: ",UnlawfulDrivingSDev)
