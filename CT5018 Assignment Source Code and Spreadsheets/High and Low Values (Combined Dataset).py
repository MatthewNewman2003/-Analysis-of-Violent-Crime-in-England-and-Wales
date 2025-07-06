#Importing libraries
import numpy as np
import pandas as pd

#Reading CSV
DataFrame = pd.read_csv("CT5018 Combined Assignment Dataset.csv")

#Determining and printing homicide high value
HomicideHigh = (DataFrame["Homicide"].mean() + DataFrame["Homicide"].std())
print("High value of homicide:",HomicideHigh)

#Determining and printing homicide low value
HomicideLow = (DataFrame["Homicide"].mean() - DataFrame["Homicide"].std())
print("Low value of homicide:",HomicideLow)

#Determining and printing violence with injury high value
ViolenceWithInjuryHigh = (DataFrame["Violence with injury"].mean() + DataFrame["Violence with injury"].std())
print("High value of violence with injury:",ViolenceWithInjuryHigh)

#Determining and printing violence with injury low value
ViolenceWithInjuryLow = (DataFrame["Violence with injury"].mean() - DataFrame["Violence with injury"].std())
print("Low value of violence with injury:",ViolenceWithInjuryLow)

#Determining and printing violence without injury high value
ViolenceWithoutInjuryHigh = (DataFrame["Violence without injury"].mean() + DataFrame["Violence without injury"].std())
print("High value of violence without injury:",ViolenceWithoutInjuryHigh)

#Determining and printing violence without injury low value
ViolenceWithoutInjuryLow = (DataFrame["Violence without injury"].mean() - DataFrame["Violence without injury"].std())
print("Low value of violence without injury:",ViolenceWithoutInjuryLow)

#Determining and printing stalking and harassment high value
StalkingHigh = (DataFrame["Stalking and harassment"].mean() + DataFrame["Stalking and harassment"].std())
print("High value of stalking and harassment:",StalkingHigh)

#Determining and printing stalking and harassment low value
StalkingLow = (DataFrame["Stalking and harassment"].mean() - DataFrame["Stalking and harassment"].std())
print("Low value of stalking and harassment:",StalkingLow)

#Determining and printing unlawful driving high value
UnlawfulDrivingHigh = (DataFrame["Death or serious injury - unlawful driving"].mean() + DataFrame["Death or serious injury - unlawful driving"].std())
print("High value of unlawful driving:",UnlawfulDrivingHigh)

#Determining and printing unlawful driving low value
UnlawfulDrivingLow = (DataFrame["Death or serious injury - unlawful driving"].mean() - DataFrame["Death or serious injury - unlawful driving"].std())
print("Low value of unlawful driving:",UnlawfulDrivingLow)
