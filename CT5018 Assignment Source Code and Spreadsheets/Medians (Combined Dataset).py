#Importing Pandas
import pandas as pd

#Opening CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Reading median of homicide
HomicideMedian = DataFrame["Homicide"].median()

#Printing median of homicide
print("Median of homicide:",HomicideMedian)

#Reading median of violence with injury
ViolenceWithInjuryMedian = DataFrame["Violence with injury"].median()

#Printing median of violence with injury
print("Median of violence with injury: ",ViolenceWithInjuryMedian)

#Reading median of violence without injury
ViolenceWithoutInjuryMedian = DataFrame["Violence without injury"].median()

#Printing median of violence without injury
print("Median of violence without injury: ",ViolenceWithoutInjuryMedian)

#Reading median of stalking and harassment
StalkingMedian = DataFrame["Stalking and harassment"].median()

#Printing median of stalking and harassment
print("Median of stalking and harassment: ",StalkingMedian)

#Reading median of death or serious injury through unlawful driving
UnlawfulDrivingMedian = DataFrame["Death or serious injury - unlawful driving"].median()

#Printing median of death or serious injury through unlawful driving
print("Median of unlawful driving: ",UnlawfulDrivingMedian)
