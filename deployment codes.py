#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

#st.write("slider number:", x)
# In[2]:




# In[6]:


import pandas as pd
import numpy as np
df=pd.read_csv('Forecast_df.csv')
column_to_drop=0
#df.drop(df.columns[column_to_drop], axis=1, inplace=True)

df['Date'] = pd.to_datetime(df['Date'],errors='coerce')

def main():
    st.title('Predicted Close')

    # Create a slider for date selection
    start_date = st.date_input('Select Start Date', min_value=df['Date'].min().date(), max_value=df['Date'].max().date())
    end_date = st.date_input('Select End Date', min_value=df['Date'].min().date(), max_value=df['Date'].max().date())

    # Convert date input values to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the dataset based on the selected date range
    filtered_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    st.subheader('Selected Data')
    st.write(filtered_data)

    # Create a line chart to display the selected data
    st.subheader('Price Over Time')
    #import plotly.express as px
    #px.lineplot(filtered_data.set_index('Date')['Price'])
    st.line_chart(filtered_data.set_index('Date')['Close'])

if __name__ == '__main__':
    main()








# In[ ]:





# In[ ]:





# In[ ]:






# In[ ]:





# In[ ]:




