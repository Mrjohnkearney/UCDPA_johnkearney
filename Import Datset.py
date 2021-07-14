# Import pandas and Numpy
import pandas as pd

import os
os.getcwd()
import pandas as pd



# Read CSV file
Gender_Stats = pd.read_csv('Gender_StatsData.csv')
# Creating a data frame
df = pd.DataFrame(Gender_Stats)

# Itering over the data frame rows
# using df.iterrows()
itr = next(df.iterrows())[1]
itr

# Print FIle
print(Gender_Stats)

# To display any top 10 rows
Gender_Stats.head(1000)

# To check the shape of the dataset
Gender_Stats.shape

# To show the columns of the dataset
Gender_Stats.columns

# To check the data type  of the dataset
Gender_Stats.dtypes

Gender_Stats.loc[:10, ["Country Name", "Indicator Name", "2019"]]

# Sort by Indicator Name
Gender_Stats.sort_values("Indicator Name")

# list unique values for indicators
Gender_Stats['Indicator Name'].unique()

# import numpy as np
df = pd.DataFrame

Gender_Stats

# Show top 500 values
Gender_Stats.head(500)

# Describe the data based on the Indicator Code Column
Gender_Stats['Indicator Code'].describe()

# Show the unique values on the indicator code Column
Gender_Stats['Indicator Code'].unique()
# Show the Country , country code, Indicator name , Indicator code and data for 2019
var = Gender_Stats[['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code', '2019']]
# Create a new Dataset called Gender_Stats_2019
Gender_Stats_2019 = Gender_Stats[['Country Name', 'Country Code', 'Indicator Name','Indicator Code', '2019']]

# Print Gender_Stats_2019
print(Gender_Stats_2019)
# Filter Gender_Stats_2019 to show rows for 'Cause of Death by Injury (% of total)
Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']

# Create a dataFrame
df =pd.DataFrame(Gender_Stats_2019)
# Drop rows where values on column '2019' is equal to NaN
df.dropna(subset = ["2019"],inplace=True)

# Filter the dataframe to show all rows with values for 'Cause of death, by injury (% of total)
Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']
# Generate  CSV file for export
Gender_Stats_2019.to_csv("Gender_Stats_2019.csv", index=False, encoding='utf8')

# Create a new Dataset

Gender_Stats_2019_Full =Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']

# Drop all NaN values
death_by_injury = Gender_Stats_2019_Full.dropna()

import matplotlib.pyplot as plt
# select Data to plot in chart
plot_data = Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']
plot_data = plot_data.groupby('Country Name')['2019'].sum()
plot_data.sort_values()[-25:].plot(kind='bar')
plt.title('Countries with greatest Death by Injury(% of total)')
plt.ylabel('% Deaths by Injury')

# select Data to plot in chart
plot_data = Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Cause of death, by injury (% of total)']
plot_data = plot_data.groupby('Country Name')['2019'].sum()
plot_data.sort_values()[34:59].plot(kind='bar')
plt.title('Countries with Lowest Death by Injury(% of total)')
plt.ylabel('% Deaths by Injury')

# sort the data for Daeath by Injury  and display
death_by_injury.sort_values(["2019"])

# View Death by Injury DataFrame
death_by_injury


# New Dataset GDP_Per_Capita
GDP_Per_Capita =Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'GDP per capita (constant 2010 US$)']

# Drop NaN values
GDP = GDP_Per_Capita.dropna()

# Create new file called GDP without NaN values
GDP = GDP_Per_Capita.dropna()

# Sort based on 2019 GDP per capita
GDP.sort_values(["2019"])

# Merge GDP and Death by Injury  using an innor join using country code as the key
import pandas as pd

pd.merge(GDP, death_by_injury, on='Country Code', how='inner')

# Create a new dataframe called GDP_Death by Injury
GDP_Death_By_Injury = pd.merge(GDP, death_by_injury, on='Country Code', how='inner')

# Create a CSV file from the GDP_Death_by_Injury dataframe
GDP_Death_By_Injury.to_csv("GDP_Death_By_Injury.csv", index=False, encoding='utf8')

# Import Seaborn
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading Dataset:
Death = pd.read_csv(r"C:\Users\jkearney\OneDrive - MyComplianceOffice\Documents\GitHub\UCDPA_johnkearney\GDP_Death_By_injury.csv")

# previewing the Dataset
Death.head(10)


# Obtaining dataset  details:
Death.describe()


# Creating a Death csv file
Death.to_csv("Death.csv", index=False, encoding='utf8')

# Defining Color Ref https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-6-additional-linear-data-regression-plots-7a6fd469cea6

tableau_20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
         (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
         (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
         (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
         (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scaling avove RGB values to [0, 1] range, which is Matplotlib acceptable format:
for i in range(len(tableau_20)):
    r, g, b = tableau_20[i]
    tableau_20[i] = (r / 255., g / 255., b / 255.)

tableau_20[4]
# Renameing the 2019_X and 2019_y Columns
Death.rename(columns={ '2019_y':'% Death by Injury', '2019_x': 'GDP per Capita'})

# Create new Dataset called Death New
Death_New= Death.rename(columns={ '2019_y':'% Death by Injury', '2019_x': 'GDP per Capita'})



# Plot Death new using Seaborn
sns.lmplot(x='GDP per Capita', y= '% Death by Injury', data=Death_New, scatter_kws={'color':tableau_20[2], 'alpha':0.75})

# Switch the X and Y axis
sns.lmplot(x= '% Death by Injury', y = 'GDP per Capita', data=Death_New, scatter_kws={'color':tableau_20[2], 'alpha':0.75})

# Use Iterrows to get Iterations
import pandas as pd

# Creating a data frame
df = pd.DataFrame(Gender_Stats)

# Itering over the data frame rows
# using df.iterrows()
itr = next(df.iterrows())[1]
itr

# Creating a data frame for Number of years Female Schooling  per Country
Female_Schooling =Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Expected years of schooling, female']

# Show the Female Schooling Dataset
Female_Schooling

# Drop NaN values from Female Schooling
Female_Schooling.dropna()

# Create a new Dataset called FSchool
FSchool=Female_Schooling.dropna()

# Create a Male Schooling Dataset
Male_Schooling =Gender_Stats_2019[Gender_Stats_2019["Indicator Name"] == 'Expected years of schooling, male']

# Create a MSchooling Dataset without NaN values
MSchooling = Male_Schooling.dropna()

# Create a new dataset by merging GDP and School
GDP_Female_schooling = pd.merge(GDP, FSchool, on='Country Code', how='inner')

# Update the COLUMN NAMES ON THE DATASET
GDP_Female_schooling_New = GDP_Female_schooling.rename(columns={ '2019_y':'Years Female Schooling', '2019_x': 'GDP per Capita'})

# Create a new dataset by merging GDP and School
sns.lmplot(x="Years Female Schooling", y="GDP per Capita", data=GDP_Female_schooling_New, scatter_kws={'color':tableau_20[2], 'alpha':0.75})

# Merge GDP and Make Schooling
GDP_male_schooling = pd.merge(GDP, Male_Schooling, on='Country Code', how='inner')

# Update the Column Names
GDP_Male_Schooling_New = GDP_male_schooling.rename(columns={ '2019_y':'Years Male Schooling', '2019_x': 'GDP per Capita'})

# Plot Male Schooling vs GDP
sns.lmplot(x="Years Male Schooling", y="GDP per Capita", data=GDP_Male_Schooling_New, scatter_kws={'color':tableau_20[2], 'alpha':0.75})

# Get Pearsons correlation of Male Schooling to GDP per Person
GDP_Male_Schooling_New.corr(method='pearson')

# Get Pearsons correlation of Female Schooling to GDP per Person
GDP_Female_schooling_New.corr(method='pearson')

# Describe the Years Female Schooling Column
GDP_Female_schooling_New['Years Female Schooling'].describe()

# Describe the Years Male Schooling Column
GDP_Male_Schooling_New['Years Male Schooling'].describe()

# Generate a CSV file for GDP_Female_schooling_New
GDP_Female_schooling_New.to_csv("GDP_Female_schooling_New.csv", index=False, encoding='utf8')

# Generate a CSV file for MSchooling
MSchooling.to_csv("MSchooling.csv", index=False, encoding='utf8')