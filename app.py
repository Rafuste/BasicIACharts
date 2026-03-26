import streamlit as st
import pandas as pd
from plotly import express as px

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('regional_sales_forecast.csv')
    return data

data = load_data()

# Sidebar filters
year = st.sidebar.selectbox('Select Year', data['Year'].unique())
region = st.sidebar.selectbox('Select Region', data['Region'].unique())

# Filter data
filtered_data = data[(data['Year'] == year) & (data['Region'] == region)]

# Summary statistics
st.write('### Summary Statistics')
st.write(filtered_data.describe())

# Plot
fig = px.bar(filtered_data, x='Product', y='Sales', title='Sales Forecast')
st.write(fig)
