
# Import necessary packages
from llama_index import GPTVectorStoreIndex, Document, SimpleDirectoryReader
import os
import pandas as pd
import numpy as ny

url = 'https://raw.githubusercontent.com/nailson/ifood-data-business-analyst-test/master/ml_project1_data.csv'

df = pd.read_csv(url)

df.to_csv('test.csv', index=False)



# Identify missing values
print(df.isnull().sum())

# Impute missing values (replace with mean), excluding AcceptedCmp1, AcceptedCmp2, AcceptedCmp3,
# AcceptedCmp4, AcceptedCmp5, Response and Complain ( in this case set the value to the mode)

# List of exclusded columns to set to mean
exclude_columns = ['ID','AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3',
'AcceptedCmp4', 'AcceptedCmp5', 'Response' and 'Complain']

filled_df = df.copy()

# Iterate through all cells
def find_mean_mode(df, exclude_columns):
  for column in df.columns:
    if column not in exclude_columns and df[column].isnull().any() and pd.api.types.is_numeric_dtype(df[column]):
      # Calculate the mean of the column and fill missing values with the mean
      mean_value = df[column].mean()
      filled_df[column].fillna(mean_value, inplace=True)
    elif column in exclude_columns and df[column].isnull().any() and pd.api.types.is_numeric_dtype(df[column]):
      mode_value = df[column].mode()[0]
      dfilled_df[column].fillna(mode_value, inplace=True)
  return filled_df


#Identify and remove outliers:
def identify_outliers(filled_df, z_score_threshold=2):
  df_no_outliers = filled_df.copy()
  for column in filled_df.columns:
    if column not in exclude_columns and pd.api.types.is_numeric_dtype(filled_df[column]):
        z_scores = np.abs(stats.zscore(filled_df[column]))
        outliers = z_scores <= z_score_threshold  # Ensure boolean values
        mean_value = df[column].mean()

        # Replace outliers with the mean
        df_no_outliers.loc[outliers, column] = mean_value
    return df_no_outliers

populated_data = find_mean_mode(df, exclude_columns)
cleaned_data = identify_outliers(populated_data, 3)

populated_data.to_csv('populated.csv', index=False)
cleaned_data.to_csv('ifood_cleaned_data.csv', index=False)
