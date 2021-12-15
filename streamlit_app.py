"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
st.write("Equity Mix Election")
st.write("Plans")
st.write(df=pd.DataFrame({
    'RSU %': [100, 75, 50],
    'Option %': [0, 25, 50], 'Plan':['Plan 1','Plan 2', 'Plan 3']
}))
option = st.selectbox(
   'Which number do you like best?',
     df['Plan'])

'You selected: ', option
