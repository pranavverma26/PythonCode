import streamlit as st
import pandas as pd
import time

# Title
st.title('Startup Dashboard')

# Header
st.header('I am learning Streamlit')
st.subheader('I am loving it')

# To wrire a paragraph
st.write('My name is Pranav Kumar Verma')

# Markdown
st.markdown("""
### My favourite movies
- Race 3
- Humsakals
- Housefull
""")

# code
st.code("""
def foo(input):
        return foo*2
x = foo(2)
""")
st.latex('x^2 + y^2 = 0')


# dataframe
df = pd.DataFrame({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})
st.dataframe(df)

# metric
st.metric('Revenue','Rs 3L','3%')

# json
st.json({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})
st.image('D:\Coding Language\Python\ImageInfo.jpg')
st.video(r'C:\Users\prana\Videos\Mee1.mp4')

# Creating Layouts

# sidebar
st.sidebar.title('Sidebar ka Title')

# What if apko ak he row mai multiple chija add krni hai..previous column wise write hoa rha tha.

col1,col2,col3 = st.columns(3)

with col1:
    st.image(r"C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-15 120516.png")

with col2:
    st.image(r"C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-15 120516.png")

with col3:
    st.image(r"C:\Users\prana\OneDrive\Pictures\Screenshots\Screenshot 2026-07-15 120516.png")

# Error messages
st.error('Login Failed')
st.success('Login Success')
st.warning('Login Successful')

# Progress Bar
bar = st.progress(0)      # Create progress bar starting at 0%

for i in range(1, 101):   # Loop from 1 to 100
    time.sleep(0.1)        # Wait for 0.1 seconds
    bar.progress(i)        # Update the same progress bar

# Input
email = st.text_input('Enter email')
number = st.number_input('Enter age')
st.date_input('Enter regis date')