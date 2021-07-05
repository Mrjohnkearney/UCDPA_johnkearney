## Import pandas and Numpy
import pandas as pd

import os
os.getcwd()

## Read CSV file
Gender_Stats =pd.read_csv('Gender_StatsData.csv')

## Print FIle
print(Gender_Stats)

## To display any top 10 rows
Gender_Stats.head(1000)

## To check the shape of the dataset
Gender_Stats.shape

## To check the data type  of the dataset
Gender_Stats.dtypes

Gender_Stats.loc[:10, ["Country Name", "Indicator Name", "2019"]]

## Sort by Indicator Name
Gender_Stats.sort_values("Indicator Name")

## list unique values for indicators
Gender_Stats['Indicator Name'].unique()

import numpy as np
df = pd.DataFrame

Gender_Stats

## Show top 500 values
Gender_Stats.head(500)

## Describe the data based on the Indicator Code Column
Gender_Stats['Indicator Code'].describe()

##Show the unique values on the indicator code Column
Gender_Stats['Indicator Code'].unique()
##Show the Country , country code, Indicator name , Indicator code and data for 2019
Gender_Stats[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code','2019']]
##Create a new Dataset called Gender_Stats_2019
Gender_Stats_2019 = Gender_Stats[['Country Name', 'Country Code', 'Indicator Name','Indicator Code', '2019']]

##Print Gender_Stats_2019
print(Gender_Stats_2019)
##Filter Gender_Stats_2019 to show rowsfor 'Cause of Death by Injury (% of total)
Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']

##Create a dataFrame
df =pd.DataFrame(Gender_Stats_2019)
##Drop rows where values on column '2019' is equal to NaN
df.dropna(subset = ["2019"], inplace=True)

##Filter the dataframe to show all rows with values for 'Cause of death, by injury (% of total)
Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']
##Generate  CSV file for export
Gender_Stats_2019.to_csv("Gender_Stats_2019.csv", index=False, encoding='utf8')