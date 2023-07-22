import streamlit as st
import pandas as pd # for data analysis
import numpy as np # for numerical functions
import plotly.express as px #for interactive plots

@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

with st.spinner('Loading Dat..'):
    df = load_data()

st.title('House Price Data Analysis')

if st.checkbox('Show Dataset', True):
    st.subheader('Dataset')
    st.dataframe(df)