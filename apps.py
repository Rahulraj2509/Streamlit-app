#1) Full name;                              RAHUL KUMAR SINGH
#2) The degree you’re currently pursuing;   B.TECH CSE 3rd Yr(DATA SCIENCE)
#3) Your college’s name;                    LOVELY PROFESSIONAL UNIVERSITY
#4) Your phone number;                      8851037274




import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import plotly.express as px 

df = pd.read_excel("source1.xlsx")
option = st.multiselect('Choose one or more Item Type', df['Item_Type'].unique())


new_df = df[(df['Item_Type'].isin(option))]

st.write(new_df)