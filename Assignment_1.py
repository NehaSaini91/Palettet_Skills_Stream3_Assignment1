# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:18:50 2024

@author: nsain
"""

import pandas as pd
df1 = pd.read_csv('C:/Users/nsain/Downloads/df_1.csv')
df2 = pd.read_csv('C:/Users/nsain/Downloads/df_2.csv')

print('Unique RMs df_2: ', df2['RM'].nunique())
print('Unique RMs df_1: ', df1['RM'].nunique())
print('After Merging',pd.merge(df2, df1, on='RM')['RM'].nunique())

df_merging=pd.merge(df2, df1, on='RM')

# The once are not matching
df_notmatching =pd.DataFrame(set(df2['RM'].unique()) - set(pd.merge(df2, df1, on='RM')))


#trail


df22 = pd.DataFrame()
df11 = pd.DataFrame()

df22['RM'] = df2['RM'].str.capitalize().str.strip()
df11['RM'] = df1['RM'].str.capitalize().str.strip()
df_final = pd.concat([df11,df22]).drop_duplicates().reset_index(drop=True)
df_finals = pd.concat([df11,df22]).drop_duplicates().reset_index(drop=True).nunique()

df22['RM']= df1['RM'].nunique()
print('Unique RMs df_1: ', df1['RM'].nunique())


import pandas as pd

def clean_and_get_unique(df1, df2, RM):
    # Read Excel files into pandas DataFrames
    #df1 = pd.read_excel(file1)
    #df2 = pd.read_excel(file2)
    
    # Concatenate the two DataFrames
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    # Remove duplicates
    cleaned_df = combined_df.drop_duplicates(subset=RM)
    
    # Get unique values
    unique_values = cleaned_df[RM].unique()
    
    return unique_values

# Example usage:
file1 = "file1.xlsx"
file2 = "file2.xlsx"
column_name = "RM"

unique_values = clean_and_get_unique(df1, df2, column_name)
print("Unique values:", unique_values)


#Question 1
import pandas as pd

# Concatenate the two DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)
# Remove duplicates
combined_df['RM'] = combined_df['RM'].str.upper().str.strip()

combined_df.RM = combined_df.RM.str.replace('.', '')
# combined_df.RM = combined_df.RM.str.replace('-', '')
# combined_df.RM = combined_df.RM.str.replace('(', '')
# combined_df.RM = combined_df.RM.str.replace(')', '')

cleaned_df = combined_df.drop_duplicates()

cleaned_df['RM'] = cleaned_df['RM'].unique()

df_notmatching =pd.DataFrame(set(df_merging['RM'].unique()) - set(cleaned_df['RM']))

    # Get unique values
unique_values = cleaned_df['RM'].unique()
print("Unique values:", unique_values)

#Question 2

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Read the shapefile
shapefile = "C:/Users/nsain/Downloads/RM_shapefile/RuralMunicipality.shp"
gdf = gpd.read_file(shapefile)

# Read the cleaned rural management data into a DataFrame
rural_management_data = pd.read_csv("C:/Users/nsain/Downloads/df_1.csv")

# Merge the shapefile DataFrame (gdf) with the rural management data
merged = gdf.merge(rural_management_data, how='left', left_on='RMNO', right_on='RM')
merged=merged.dropna(subset=["RM"])

# Plot the map
ax = merged.plot(column='RMNM', cmap='viridis', figsize=(60, 56), legend=True)

# Add title and labels
plt.title("Map of Rural Management Data")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Show the plot
plt.show()
