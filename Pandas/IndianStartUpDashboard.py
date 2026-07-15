import streamlit as st
import pandas as pd

df = pd.read_csv(r"D:\Coding Language\Python\DataSet\IndianStartUp\startup_funding.csv")

st.sidebar.title('Startup Funding Analysis')

# data cleaning
df['Investors Name']=df['Investors Name'].fillna('Undisclosed')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['Startup Name'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    st.sidebar.selectbox('Select StartUp',sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')

