import json
from urllib.request import urlretrieve
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

urlretrieve(
    'https://api.census.gov/data/2022/acs/acs1?get=NAME,B01003_001E,B06011_001E,B98001_001E&for=state:*', 'census.json')

census_df_raw = pd.read_json('census.json')

# Rename columns directly and create a copy of the DataFrame
census_df = census_df_raw.rename(columns={
    0: 'Name',
    1: 'Total Population',
    2: 'Median Income',
    3: 'Housing Unit'
}).copy()

# Drop the first row as it contains column names
census_df = census_df.iloc[1:]

# Reset index after dropping the first row
census_df = census_df.reset_index(drop=True)

# Drop the last column
census_df = census_df.iloc[:, :-1]

# print(census_df)

plt.figure(figsize=(15, 8))
sns.barplot(x='Total Population', y='Name', data=census_df, palette='viridis')
plt.title('Total Population by State')
plt.xlabel('Total Population')
plt.ylabel('State')
plt.xticks(rotation=45, ha='right')
plt.show()