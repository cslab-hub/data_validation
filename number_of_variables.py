import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_number_of_variables():
    
    st.title('How many variables are in your dataset?')
    st.markdown("""
    Most often, you do not need 2 million datasets from hundreds of variables to achieve your goals.
    Therefore, it is critical to think about the goal that you are pursuing. 
    For example, which variables should reasonably affect your response?

    Therefore, it is critical the reduce the number of variables in your dataset if there are too many available.
    Since most readers of this tool will have data originating from industry, most likely your dataset is big!
    Therefore, here select the number of variables in your dataset:
    """)
    option = st.selectbox(
        'Select the number of variables in your dataset',
        ['','<10','10-30','31+'], format_func=lambda x: 'Select an option' if x == '' else x)
    
    
    if option == '<10':
        st.success('You have an ideal number of variables!')
        st.markdown("""
        First, you have to check if all the variables that you want to investigate are in your dataset.
        If that is the case, you can go to the next chapter.
        If not, then that means that you have to check with your IT department why some specific variables are not aparant in your dataset.
        """)
        
    if option == '10-30':
        st.warning('You are in the safe zone, but keep in mind that the number of variables can be reduced further')
        st.markdown("""
        If your dataset contains in the range of 10-30 variables there is a good chance that you have just enough variables to perform an analysis, but not too many which will make it hard to determine which variables to use.
        Therefore, we advice to reduce your dataset to less variables if your dataset is closer to 30 than 10 variables. 
        After all, the less variables the better (if they are meaningfull and unique).
        """)
    if option == '31+':
        st.error('Too many variables!')
        st.markdown("""
        If your dataset consists of more than 30 variables then you have to reconsider which variables are important.
        From experience, we know that in almost 99\% of all cases, having more than 30 predictors only makes everything chaotic and perform less optimal.
        Therefore, we have the following tips:
        """)
        st.success('Tip 1: Try finding variables that do not contain any deviation')
        st.markdown('''Most likely, quite a lot of your variables are set variables.
                    What we mean by set variables are variables that monitor the settings of a machine.
                    For example, the set variable of temperature can be 90 degrees, and the variables that measures temperature has the actual readings 90.1, 90.0, 89.9, 90 etc.
                    ''')
        st.success('Tip 2: Remove variables that only measured parts of your process')
        st.markdown('''
        
        ''')

    st.markdown('### What if your desired variables are not recorded?')
    st.markdown('''
    It could occur that while performing this step on your own computer, you notice that specific variables you are interested in are not visible.
    If this occurs, we advice to ask for help with another tool in our Di-Plast project, called the [Sensoring tool](https://share.streamlit.io/skz-digi/diplastsensorselection/updated/main.py).
    ''')
    
    
    
    