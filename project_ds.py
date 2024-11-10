import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

from sklearn.metrics import mean_squared_error, mean_absolute_error,  r2_score
print("mse: ", mean_squared_error(y_test, y_pred))
print("mae: ", mean_absolute_error(y_test, y_pred))

# r2 score for model performance
r2 = r2_score(y_test, y_pred)
print(f'R-squared(model performance): {r2}')

