import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

# Checking for Null Values
df.isnull().sum()

# HANDLE OUTLIERS FOR ADULT MORTALITY COL
import matplotlib.pyplot as plt
# Creating dataset
data=df['Adult Mortality']

fig = plt.figure(figsize =(10, 7))
# Creating plot
plt.boxplot(data)
# show plot
plt.show()
st.ppyplot(plt.gcf())
# Now you can use plt to create figures and plots:
fig = plt.figure(figsize=(10, 7))


