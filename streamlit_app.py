"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
st.write("Equity Mix Election")
st.write("Plans")
st.write(pd.DataFrame({
    'RSU %': [100, 75, 50],
    'Option %': [0, 25, 50], 'Plan':['Plan 1','Plan 2', 'Plan 3']
}))
option = st.selectbox(
    'Which number do you like best?',
     df['Plan'])

'You selected: ', option

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
