## Import pandas and Numpy
import pandas as pd
import numpy as ny
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

