import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

df=pd.read_csv('data/startup_cleaned.csv')

#data cleaning
df['date']=pd.to_datetime(df['date'].astype(str).str.strip(),format='mixed',errors='coerce')
df['year']=df['date'].dt.year
df['month']=df['date'].dt.month


def load_overall_analysis():
     st.title('Overall Analysis')

     #total invesed amount
     total=round(df['amount'].sum())
     #maximum invested amount
     max=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
     #avg_funding
     avg_funding=round(df.groupby('startup')['amount'].sum().mean())
     #total funded stratups
     total_startups=df['startup'].nunique()

     col1,col2,col3,col4=st.columns(4)

     with col1:
        st.metric('Total',str(total)+' CR' )
     with col2:
        st.metric('Maximum',str(max)+' CR' )
     with col3:
        st.metric('Average',str(avg_funding)+' CR' )
     with col4:
        st.metric('Total Funded Starups',str(total_startups) )

     #sector analysis pie
     sector=df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)

     st.header('MoM Graph')
     selected_options=st.selectbox('Select Type',['Total','Count'])
     if selected_options=='Total':
        temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
     else:
        temp_df=df.groupby(['year','month'])['amount'].count().reset_index()  

     temp_df['x_axis']=temp_df['month'].astype(str)+'-'+temp_df['year'].astype(str)

     fig0,ax0= plt.subplots()
     ax0.plot(temp_df['x_axis'],temp_df['amount'])
     st.pyplot(fig0)

     #city wise funding
     city_wise_funding=df.groupby('city')['amount'].sum().sort_values(ascending=False).head(10)
     st.subheader('City Wise Funding')
     fig2,ax2 = plt.subplots()
     ax2.pie(city_wise_funding,labels=city_wise_funding.index,autopct='%0.01f')
     st.pyplot(fig2)

     st.header('Top StartUps')

     selected_options=st.selectbox('Select Type',['Overall','Year-Wise'])
     if selected_options=='Overall':
             temp_df=df.groupby('startup')['amount'].sum().reset_index()
             temp_df=temp_df.sort_values(by='amount',ascending=False).reset_index()
             temp_df.drop(columns=['index'],inplace=True)
             temp_df['amount']=round(temp_df['amount'],2)
             st.dataframe(temp_df.head(10))
     else:
          year=st.selectbox('Year', sorted(df['year'].unique().tolist()))
          temp_df=df
          temp_df=temp_df[temp_df['year']==year]
          temp_df=temp_df.groupby('startup')['amount'].sum().reset_index()
          temp_df=temp_df.sort_values(by='amount',ascending=False).reset_index()
          temp_df.drop(columns=['index'],inplace=True)
          temp_df['amount']=round(temp_df['amount'],2)
          st.dataframe(temp_df.head(10))

     st.header('Top Investors')

     temp_df=df.groupby('investors')['amount'].sum()
     temp_df=temp_df.sort_values(ascending=False)
     st.dataframe(temp_df.head(10))
            

def load_startup_details(company_name):
     st.header(company_name)

     col1,col2=st.columns(2)
     with col1:
             st.metric('Industry',df[df['startup']==company_name]['vertical'].unique()[0] )
     with col2:
             st.metric('Location', df[df['startup']==company_name]['city'].iloc[0] )

    
     st.header('Funding Rounds')

     rounds_df=df[df['startup']==company_name][['date','round','investors','amount']]
     rounds_df=rounds_df.sort_values('date').reset_index(drop=True)
     rounds_df.rename(columns={
          'date':'Date',
          'round':'Round',
          'investors':'Investors',
          'amount':'Amount (CR)'
     },inplace=True)

     st.metric('Total Raised',str(round(rounds_df['Amount (CR)'].sum()))+' CR')

     st.dataframe(
          rounds_df,
          hide_index=True,
          use_container_width=True,
     )
     
     

         
def load_investor_details(investor):
    st.title(investor)

    #load recent 5 investments
    last_5df=df[df['investors'].str.contains(investor)].head(5)[['date','startup','vertical','city','round','amount']]
    st.subheader('Recent Investments')
    st.dataframe(last_5df)

    col1,col2=st.columns(2)
    #biggest investment
    with col1:
        big_series=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader(f'Biggest Investment')
        fig0,ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig0)

    #investment in sectors
    with col2:
        vertical_series=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader(f'Sectors Invested In')
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct='%0.01f')
        st.pyplot(fig1)

    col3,col4=st.columns(2)

    #investment in stage
    with col3:
            stage_series=df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
            st.subheader(f'Stage Invested In')
            fig2,ax2 = plt.subplots()
            ax2.pie(stage_series,labels=stage_series.index,autopct='%0.01f')
            st.pyplot(fig2)

    #investment city wise
    with col4:
                cities_series=df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
                st.subheader(f'Cities Invested In')
                fig3,ax3 = plt.subplots()
                ax3.pie(cities_series,labels=cities_series.index,autopct='%0.01f')
                st.pyplot(fig3)

    col5,col6=st.columns(2)

    #investment city wise
    with col5:
        
        year_series=df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader(f'Year Wise Investment')
        fig4,ax4 = plt.subplots()
        ax4.plot(year_series.index,year_series.values)
        st.pyplot(fig4)


    
st.sidebar.title('Startup Funding Analysis')

option=st.sidebar.selectbox('Select on',['Overall Analysis','StartUp','Investor'])

if option=='Overall Analysis':
    
    btn0=st.sidebar.button('Show Overall Analysis')

    load_overall_analysis()
    
    
elif option=='StartUp':
    company_name=st.sidebar.selectbox('Select StartUP',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis',text_alignment='center')
    load_startup_details(company_name)


else:
    selected_investor= st.sidebar.selectbox('Select Investors',sorted(set(df['investors'].str.split(',').sum())))
    btn2=st.sidebar.button('Find Investor Details')
    st.title('Investor Analysis')
    if btn2:
        load_investor_details(selected_investor)
    
