import json
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# urlretrieve(
#     'https://api.census.gov/data/2022/acs/acs1?get=NAME,B01003_001E,B06011_001E,B98001_001E,B01001_002E,B01001_026E&for=state:*', 'census.json')

census_df_raw = pd.read_json('census.json')


# Rename columns directly and create a copy of the DataFrame
census_df = census_df_raw.rename(columns={
    0: 'Name',
    1: 'Total Population',
    2: 'Median Income',
    3: 'Housing Unit',
    4: 'Total Male',
    5: 'Total Female'
}).copy()

# Drop the first row as it contains column names
census_df = census_df.iloc[1:]

# Reset index after dropping the first row
census_df = census_df.reset_index(drop=True)

# Drop the last column
census_df = census_df.iloc[:, :-1]

# print(census_df)

# Total Population by state
# plt.figure(figsize=(15, 8))
# sns.barplot(x='Total Population', y='Name', data=census_df, palette='viridis')
# plt.title('Total Population by State')
# plt.xlabel('Total Population')
# plt.ylabel('State')
# plt.xticks(rotation=45, ha='right')
# plt.show()

#Median Income across State 
# plt.figure(figsize=(15,8))
# sns.histplot(census_df['Median Income'], bins=30, kde=True,  color='skyblue')
# plt.xlabel('Median Income')
# plt.ylabel('Frequency')
# plt.title('Distribution of Median Income across States')
# plt.show()

#Relation bw population and median income
plt.figure(figsize=(12,6))
sns.scatterplot(data= census_df, x='Total Population', y='Median Income')
plt.title('Population vs Median Income by State')
plt.xlabel('Total Population')
plt.ylabel('Median Income')
plt.show()

# correlation_matrix = census_df[[
#     'Total Population', 'Median Income', 'Housing Unit']].astype(float).corr()
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Matrix')
# plt.show()

# print(census_df.info())

census_df['Total Male'] = pd.to_numeric(
    census_df['Total Male'], errors='coerce')
census_df['Total Female'] = pd.to_numeric(
    census_df['Total Female'], errors='coerce')
census_df['Name'] = census_df['Name'].astype(str)

# population distribution by gender
plt.figure(figsize=(15, 12))
plt.barh(census_df['Name'], census_df['Total Male'], label='Male', alpha=0.7)
plt.barh(census_df['Name'], census_df['Total Female'],
         left=census_df['Total Male'], label='Female', alpha=0.7)
plt.title('Population Distribution by Gender')
plt.xlabel('Population')
plt.ylabel('State')
plt.legend()
plt.show()

# gender ratio
census_df['Gender Ratio'] = census_df['Total Male'] / census_df['Total Female']
plt.figure(figsize=(15, 8))
plt.bar(census_df['Name'], census_df['Gender Ratio'], alpha=0.7)
plt.axhline(y=1, linestyle='--', label='Equal Gender Ratio', color= 'red')
plt.xlabel('State')
plt.ylabel('Gender Ratio')
plt.title('Gender Ratio(From Male to Female)')
plt.legend()
plt.show()

# Identify the state with the highest and lowest male and female populations
max_male_state = census_df.loc[census_df['Total Male'].idxmax(), 'Name']
min_male_state = census_df.loc[census_df['Total Male'].idxmin(), 'Name']

max_female_state = census_df.loc[census_df['Total Female'].idxmax(), 'Name']
min_female_state = census_df.loc[census_df['Total Female'].idxmin(), 'Name']

print(f"State with The Highest Male Population: {max_male_state}")
print(f"State with The Lowest Male Population: {min_male_state}")

print(f"State with The Highest Female Population: {max_female_state}")
print(f"State with The Lowest Female Population: {min_female_state}")


