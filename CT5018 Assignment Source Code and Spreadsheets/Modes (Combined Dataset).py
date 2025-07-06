#Importing Pandas
import pandas as pd

#Opening CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Reading mode of homicide
HomicideMode = DataFrame["Homicide"].mode()

#Printing mode of homicide
print("Mode of homicide:",HomicideMode)

#Reading mode of violence with injury
ViolenceWithInjuryMode = DataFrame["Violence with injury"].mode()

#Printing mode of violence with injury
print("Mode of violence with injury: ",ViolenceWithInjuryMode)

#Reading mode of violence without injury
ViolenceWithoutInjuryMode = DataFrame["Violence without injury"].mode()

#Printing mode of violence without injury
print("Mode of violence without injury: ",ViolenceWithoutInjuryMode)

#Reading mode of stalking and harassment
StalkingMode = DataFrame["Stalking and harassment"].mode()

#Printing mode of stalking and harassment
print("Mode of stalking and harassment: ",StalkingMode)

#Reading mode of death or serious injury through unlawful driving
UnlawfulDrivingMode = DataFrame["Death or serious injury - unlawful driving"].mode()

#Printing mode of death or serious injury through unlawful driving
print("Mode of unlawful driving: ",UnlawfulDrivingMode)
