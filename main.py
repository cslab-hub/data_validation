import streamlit as st
# st.set_page_config(layout="wide")
import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
from PIL import Image 

from home import *
from fileformat import *
from columnnames import *
from introduction import *
from number_of_variables import *
from sample_rate import *
from descriptives import *
from outliers import *
from missingvalues import *
from feature_selection import *
from endresult import *
from interactive_test import *

# from streamlit_option_menu import option_menu

st.set_page_config(
     page_title="Data Validation",
    #  page_icon="🧊",
    #  layout="wide",
    layout='centered'
    #  initial_sidebar_state="expanded",
)

st.sidebar.image("images/logo.jpeg", use_column_width=True)

st.sidebar.title("Select Chapter")
st.sidebar.markdown("Each chapter explains a different aspect of validating your dataset.")


add_selectbox = st.sidebar.radio(
    "Choose a chapter:",
    ("Home","Introduction","Chapter 1: File Format","Chapter 2: Column Names", "Chapter 3: Amount of Variables","Chapter 4: Sample Rate","Chapter 5: Descriptives","Chapter 6: Outliers","Chapter 7: Missing Values & Data Imputation","Chapter 8: Feature Selection","Chapter 9: End Result"),format_func= lambda x: 'Home' if x == 'Home' else f"{x}"
    
)  



#! Home page
if add_selectbox == 'Home':
    return_homepage()
    
    
#! Page for the file format
if add_selectbox == 'Chapter 1: File Format':
    return_file_format()
  
if add_selectbox == 'Introduction':
    return_introduction()
        
if add_selectbox == 'Chapter 2: Column Names':
    return_column_names()

if add_selectbox == 'Chapter 3: Amount of Variables':
    return_number_of_variables()
        
if add_selectbox == 'Chapter 4: Sample Rate':
    return_sample_rate()
    
    
    
if add_selectbox == 'Chapter 5: Descriptives':
    return_descriptives()
    
if add_selectbox == 'Chapter 6: Outliers':
    return_outliers()

if add_selectbox == 'Chapter 7: Missing Values & Data Imputation':
    return_missing_values()

if add_selectbox == 'Chapter 8: Feature Selection':
    return_feature_selection()

if add_selectbox == 'Chapter 9: End Result':
    return_endresult()

# if add_selectbox == 'Interactive Test':
#     return_interactive()
# This removes the copyright of how the page is made
hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.sidebar.image("images/jadslogo.png", use_column_width=True)

st.sidebar.caption("[Bug reports and suggestions welcome ](mailto:s.d.bloemheuvel@jads.nl)")
