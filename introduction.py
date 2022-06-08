import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_introduction():
    
    st.title('Why Data Validation?')
    st.markdown("""
    Welcome to the Data Validation tool, where you will learn alot about all the steps needed before doing any analysis at all.
    One might ask the question why validating your data matters.
    Well, it turns out that data workflows today are a huge mess.
    
    To start, (1) data pipelines are fragile and fail often, which can cause problems later on in the analysis steps.
    Look back at all the steps needed to get the data from your machines or IT systems in the first place.
    All that effort only included retrieving the data in its raw form, now we also need to validate it.

    (2) second, there is a lot of tacit knowledge scattered among domain experts in your organisation, making it hard for a single person to understand the entire process.

    Lastly, (3) maintenance and documentation can be challenging.
    """)

    st.title('Goal of the tool')
    st.markdown("""
    As we have learned from our pilot phase, every company has widely different data formats retrieved from their machines/systems.
    The goal of the Data Validation tool is to help you prepare your data for the Data Analytics tool.
    """)
    st.title('Find a Text Editor.')
    st.markdown("""
            Before you start reading the chapters, we advice to install a text editor to examine your data.
             After you have collected your data in either .csv or .txt, we have to inspect our data.
             Most likely you are used to Excel, however, for data analysis purposes, there are better options!
             
             We recommend [Sublime Text](https://www.sublimetext.com/), which can open almost any file format.
             Another great advantage of Sublime Text is that it open files significantly faster.
             """)
    image = Image.open('images/sublime.png')
    st.image(image, caption='Figure 1: Example of Sublime Text', use_column_width=True)
    