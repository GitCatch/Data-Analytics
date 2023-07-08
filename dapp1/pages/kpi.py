import streamlit as st
import pandas as pd # for data analysis
import numpy as np # for numerical functions
import plotly.express as px #for interactive plots

@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df = pd.read_csv(path)
    return df

# call the load data function
with st.spinner('Loading Dat..'):
    df = load_data()

#create title for your app
st.title('House Price Data Analysis')
st.subheader('Key Performance Indicators')

#get the list of all columns
cols = df.columns.tolist()
selected_cols = st.multiselect('Select Columns',cols)
st.write(f'You selected:{len(selected_cols)} columns')

for col in selected_cols:
    try:
        st.subheader(f'Column:{col}')
        st.metric(label=f'Mean {col}',
              value=round(df[col].mean()),
              delta=round(df[col].std()))
        st.line_chart(df[col], use_container_width=True)
    except:
        st.error(f'Cannot Display{col} Numeric Data')
