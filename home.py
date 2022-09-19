import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_homepage():
    # image = Image.open('images/logo.jpeg')
    # st.image(image, use_column_width=True)

    st.markdown('## Welcome to the Data Validation Tool!')
    st.markdown(
        """
        ### The Data Validation tool consists of several chapters that each discuss a different aspect of validating your data.\n
        """)
        
    st.markdown("""
    - The Introduction page explains the goals of the tool, and some initial tips to get started
    - The file format chapter will ask you several questions about your data format, which is crucial in data science.
    - Chapter 2: Column names. This chapter will give tips on giving your variables correct names.
    - Chapter 3: Amount of Variables: This chapter gives tips on determining an ideal dataset size.
    - Chapter 4: Sample Rate: This chapter gives insight in diffferent types of samples rates, i.e., the time between observations in your dataset.
    - Chapter 5: Descriptives: Provides tips for quickly investigating data, and also knowing what kind of data types are present in your dataset.
    - Chapter 6: Outliers: Explains various kinds of outliers which could exist in your dataset, and how to handle them.
    - Chapter 7: Missing Values and Data Imputation: This chapter explains how to handle missing values or missing variables.
    - Chapter 8: Feature Selection: This chapter explains two techniques to reduce the number of variables in your dataset.
    - Chapter 9: Shows the data format that is needed to usage in the Data Analytics tool.
    """) 
        
    st.markdown("""**👈 Select a Chapter from the dropdown menu on the left**""")
    
    # st.error("DISCLAIMER")
    with st.expander("See Disclaimer"):

        st.write("""
                Disclaimer of Warranty.
                
                There is no warranty for the program, to the extent permitted by applicable law. 
                except when otherwise stated in writing the copyright holders and/or other parties provide the program “as is” without warranty of any kind, either expressed or implied, 
                including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. 
                the entire risk as to the quality and performance of the program is with you. 
                should the program prove defective, you assume the cost of all necessary servicing, repair or correction.

                Limitation of Liability.
                
                In no event unless required by applicable law or agreed to in writing will any copyright holder, or any other party who modifies and/or conveys the program as permitted above, 
                be liable to you for damages, including any general, special, 
                incidental or consequential damages arising out of the use or inability to use the program (including but not limited to loss of data or data being rendered inaccurate or losses sustained by you or third parties or a failure of the program to operate with any other programs), 
                even if such holder or other party has been advised of the possibility of such damages.

                """)

    st.markdown("""
        Credits to all visuals used in this tool:
    <div>Icons made by <a href="https://www.flaticon.com/authors/roundicons-premium" title="Roundicons Premium">Roundicons Premium</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    """,  unsafe_allow_html=True)

    # st.write("""<p style=" position: absolute; bottom: 0; left: 0; width: 100%; text-align: center;">Please wait a moment and you will be redirected to the forums.</p>""", unsafe_allow_html=True)
    st.write("""<footer>  The Text which we want to insert in footer.  </footer>   """, unsafe_allow_html=True)

    
