import streamlit as st
import pandas as pd

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])

btn = st.button('Login karo')


if btn:
    if email =='pranavkumarverma26@gmail.com' and password =='1234':
        st.balloons()
        st.write(gender)
    else:
        st.error('Login Failed')



