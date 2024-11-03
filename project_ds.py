import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

# Checking for Null Values
df.isnull().sum()


