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



 plt.scatter(y_test, y_pred, label='Actual vs Predicted')
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Actual vs Predicted Values in Linear Regression")

    # Menambahkan garis regresi
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], linestyle='--', color='red', linewidth=2, label='Regression Line')
    plt.legend()
    st.pyplot(plt)  # Menampilkan plot di Streamlit
    plt.clf()  # Bersihkan plot setelah menampilkan

except NameError as e:
    print(f"Error: {e}. Pastikan 'y_test' dan 'y_pred' sudah didefinisikan.")



