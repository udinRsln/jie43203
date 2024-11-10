import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

# Checking for Null Values
df.isnull().sum()

from sklearn.model_selection import train_test_split

# DEFINE FEATURES AND TARGET VAR
X = new_df.drop(columns=['Life expectancy ', 'Country','Status'])
y = new_df['Life expectancy ']

import numpy as np
# Identify and remove outliers using the IQR method
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = (df < lower_bound) | (df > upper_bound)

# Print the indices of the outliers
print("Indices of outliers:", np.where(outliers))

# Remove outliers from the dataset
cleaned_df = df[~outliers]

# Creating a new boxplot without outliers
fig, ax = plt.subplots(figsize=(10, 7))
ax.boxplot(cleaned_df)

# Show the updated plot
plt.show()

new_df=df[df['Adult Mortality']<upper_bound]



