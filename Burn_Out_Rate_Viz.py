import pandas as pd
import streamlit as st
import numpy as np
import chart_studio
import chart_studio.plotly as py
import plotly.express as px

chart_studio.tools.set_credentials_file(username='nhc11', api_key='JfKd8qsoY3BSR7APxPML')

#load data and clean from N/a

df = pd.read_csv("C:/Users/nohra/OneDrive/Documents/AUB/Courses/MSBA 325/Assignments/Assignment 2/archive/Employee Burn Out Rate.csv")

# df = df.drop(df.index[15001:25000],0)
df = df.dropna()

st.title('Burn Out Rate Analysis')

st.write("Our dataframe is seggregated into 5 designations Assistant Executive, Junior Executive, Account Executive, Senior Executive and Manager")

df

Designation_Resource_Allocation = df.groupby('Designation', as_index=False)['Resource Allocation'].mean()

st.write('Based on the below, we notice that as the employees position increases,the average resources allocated (i.e. the working time) also increases')
gapminder = px.data.gapminder()
fig = px.scatter(Designation_Resource_Allocation, x='Designation', y='Resource Allocation')
st.plotly_chart(fig)

if st.checkbox('Show dataframe'):
    chart_data = Designation_Resource_Allocation
    chart_data

st.write('Although the distribution of burn rate is slightly different beween male and female, we notice that burn rate has the same distribution between Service and Product. This means that no matter what the company type is, employees are getting burnt out more or less the same')
fig2 = px.violin(df, y="Burn Rate",x="Company Type", color = "Gender"  ,box = True)
st.plotly_chart(fig2)

Gender_Company_Allocation = df.groupby(['Company Type', 'Gender'], as_index=False)['Burn Rate'].mean()

selected_sex = st.selectbox("Select Sex", df['Gender'].unique())
selected_company = st.selectbox("Select Company", df['Company Type'].unique())
st.write(f"Selected Option: {selected_sex!r}")
st.write(f"Selected Option: {selected_company!r}")
#st.write('The average burn out rate for a',selected_sex, 'in a ', selected_company, ' company',' is: ', Gender_Company_Allocation.loc[selected_sex,selected_company])

#i tried including the above function but it keeps showing a traceback error; was not able to fix the error



if st.checkbox('Show Gender Dataframe'):
    gender_data = Gender_Company_Allocation
    gender_data


st.write('Based on the below, we notice that the higher the designation of the employee at the company, the higher the burn out rate. This can be seen from the below graphs showing details or using a simplified scatter plot to show the average increase in burn rate.')
fig3 = px.strip(df, x='Designation', y='Burn Rate', color = 'Gender', facet_col = 'Company Type')
st.plotly_chart(fig3)


Designation_Burn_Rate = df.groupby('Designation', as_index=False)['Burn Rate'].mean()
gapminder = px.data.gapminder()
fig4 = px.scatter(Designation_Burn_Rate, x='Designation', y='Burn Rate')
st.plotly_chart(fig4)

selected_class = st.radio("Select Class", Designation_Burn_Rate['Designation'].unique())
st.write("Selected Class:", selected_class)
st.write("Selected Class Type:", type(selected_class))
st.write('The average burn out rate for class ',selected_class,'is: ', Designation_Burn_Rate['Burn Rate'][selected_class])

st.write('Finally, by plotting the average burn out rate in comparison to the resource allocation (working hours), we could see that the more the employee works the more they feel like they are burnt out.')

Resource_Burn_Rate = df.groupby('Resource Allocation', as_index=False)['Burn Rate'].mean()
gapminder = px.data.gapminder()
fig5 = px.scatter(Resource_Burn_Rate, x='Resource Allocation', y='Burn Rate')

st.plotly_chart(fig5)