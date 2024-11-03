import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

# Checking for Null Values
df.isnull().sum()

# HANDLE OUTLIERS FOR ADULT MORTALITY COL
plt.scatter(y_test, y_pred, label='Actual vs Predicted')
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values in Linear Regression")

# Plot the regression line in red
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2, label='Regression Line')

# Customize plot
plt.legend()
plt.show()
st.pyplot(plt.gcf())



