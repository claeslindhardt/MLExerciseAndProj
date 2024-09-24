#==========================================
###     DATA CLEANING
#==========================================
#TODO: use mini-conda
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

#Path to data

df_original = pd.read_csv('./water_potability.csv')
df = df_original.copy()

#-----------------
##Data summary:

#df.head()
#df.info()
#df.describe()


#-----------------
### Data Cleaning

df.isna().sum()

#Finding the most relevant part of the data
df[(df['ph'].isna() == True)
& (df['Sulfate'].isna() == True)
& (df['Trihalomethanes'].isna() == True)]

#drop all values which have 3 datapoints missing
idx = df[(df['ph'].isna() == True)
& (df['Sulfate'].isna() == True)
& (df['Trihalomethanes'].isna() == True)].index

df.drop(idx)

#print(idx)

#drop all values which have 2 datapoints missing
idx2 = df[((df['ph'].isna() == True)
& (df['Sulfate'].isna() == True))
| ((df['Trihalomethanes'].isna() == True)
& (df['Sulfate'].isna() == True))
| ((df['Trihalomethanes'].isna() == True)
& (df['ph'].isna() == True))].index


df.drop(idx2)

#print(idx2)

#-----------------
##Simulating/filling missing data

#print(df.describe())
#pH NaN
values = {'ph' : df['ph'].mean()}
df = df.fillna(value=values)
df.isna().sum()

#Sulfate NaN
values = {'Sulfate' : df['Sulfate'].mean()}
df = df.fillna(value=values)
df.isna().sum()

#Trihalomethanes NaN
values = {'Trihalomethanes' : df['Trihalomethanes'].mean()}
df = df.fillna(value=values)
df.isna().sum()
#print('Any Changes?')
#print(df.describe())

#-----------------
##Outliers

#to get a general overview of the data,
#We made a scatterplot
"""import matplotlib.pyplot as plt

x = np.arange(df.shape[0])
for attribute in df:
    plt.scatter(x, df[attribute], s=1)
    plt.xlabel('Number of the data record')
    plt.ylabel(attribute)
    plt.show()"""

"""
sns.boxplot(y='ph', data=df)
plt.title('Boxplot of pH')
#plt.show()

sns.boxplot(y='Hardness', data=df)
plt.title('Boxplot of Hardness')
#plt.show()

sns.boxplot(y='Solids', data=df)
plt.title('Boxplot of Solids')
#plt.show()

sns.boxplot(y='Chloramines', data=df)
plt.title('Boxplot of Chloramines')
#plt.show()

sns.boxplot(y='Sulfate', data=df)
plt.title('Boxplot of Sulfate')
#plt.show()

sns.boxplot(y='Conductivity', data=df)
plt.title('Boxplot of Conductivity')
#plt.show()

sns.boxplot(y='Organic_carbon', data=df)
plt.title('Boxplot of Organic_carbon')
#plt.show()

sns.boxplot(y='Trihalomethanes', data=df)
plt.title('Boxplot of Trihalomethanes')
#plt.show()

sns.boxplot(y='Turbidity', data=df)
plt.title('Boxplot of Turbidity')
#plt.show()
"""
# List of the attributes for which you want to create boxplots
attributes = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
              'Organic_carbon', 'Trihalomethanes', 'Turbidity']

# Loop through each attribute in the list and generate the boxplot
for attribute in attributes:
    sns.boxplot(y=attribute, data=df)
    plt.title(f'Boxplot of {attribute}')
    plt.show()


#in our boxplots we do see outliers,
#however these values where collected in a very controlled enviroment
#suggesting that these outliers does
#not represent unrepresentative meassures

#-----------------
##Standardisation

scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df_standardized)
