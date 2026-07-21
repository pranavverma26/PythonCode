import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')
df = pd.read_csv(r"D:\Coding Language\Python\DataSet\IndianStartUp\textFile.csv")
df['date']=pd.to_datetime(df['date'],errors='coerce')
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month


def load_overall_analysis():
    st.title("Overall Analysis")

    col1,col2,col3,col4=st.columns(4)
    
    # total invested amount
    total=round(df['amount'].sum())
    
    # max_amount infused in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]

    # avg ticket size
    avg_funding=df.groupby('startup')['amount'].sum().mean()

    # Total funded startups
    nums_startup=df['startup'].nunique()



    with col1:
        st.metric('Total Investment',str(total)+' Cr')
    with col2:
        st.metric('Max Investment',str(max_funding)+' Cr')
    with col3:
        st.metric('Avg Investment',str(round(avg_funding))+' Cr')
    with col4:
        st.metric('Funded Startups',nums_startup)

    st.header("MoM graph")
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
         temp_df = df.groupby(['year','month'])['amount'].count().reset_index()
        
    temp_df['x_axis']=temp_df['month'].astype('str')+'-'+temp_df['year'].astype('str')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig5)


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    last5_df=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1,col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    with col2:
        vertical_series= df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        vertical_series = vertical_series[vertical_series > 0]
        st.subheader('sectors invested in')
        if vertical_series.empty:
            st.warning("No investment data available for pie chart.")
        else:
            fig1, ax1 = plt.subplots()
            ax1.pie(vertical_series,
                    labels=vertical_series.index,
                    autopct="%0.1f%%")
            st.pyplot(fig1)
    col3,col4=st.columns(2)
    with col3:
        round_series= df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader("Funding Distribution by Round")
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct="%0.1f%%")
        st.pyplot(fig2)
    with col4:
        city_series=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum().sort_values(ascending=False)
        st.subheader("City-wise Investments")
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series,labels=city_series.index,autopct="%0.1f%%")
        st.pyplot(fig3)


    year_plot=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader("Year by Year Investment")
    fig4, ax4 = plt.subplots()
    ax4.plot(year_plot.index,year_plot.values)
    st.pyplot(fig4)


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor=st.sidebar.selectbox('Select StartUp',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
    


