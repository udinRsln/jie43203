import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/udinRsln/jie43203/refs/heads/main/Life%20Expectancy%20Data.csv')
st.write(df)

try:
    print("MSE: ", mean_squared_error(y_test, y_pred))
    print("MAE: ", mean_absolute_error(y_test, y_pred))
    
    # r2 score for model performance
    r2 = r2_score(y_test, y_pred)
    print(f'R-squared (model performance): {r2}')
except NameError as e:
    print(f"Error: {e}. Pastikan 'y_test' dan 'y_pred' sudah didefinisikan.")

