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

# split dataset to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)




