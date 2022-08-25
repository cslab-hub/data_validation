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
                15. Disclaimer of Warranty.
                THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. 
                EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, 
                INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. 
                THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. 
                SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

                16. Limitation of Liability.
                IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, 
                BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, 
                INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), 
                EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

                """)

    st.markdown("""
        Credits to all visuals used in this tool:
    <div>Icons made by <a href="https://www.flaticon.com/authors/roundicons-premium" title="Roundicons Premium">Roundicons Premium</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
    """,  unsafe_allow_html=True)

    # st.write("""<p style=" position: absolute; bottom: 0; left: 0; width: 100%; text-align: center;">Please wait a moment and you will be redirected to the forums.</p>""", unsafe_allow_html=True)
    st.write("""<footer>  The Text which we want to insert in footer.  </footer>   """, unsafe_allow_html=True)

    
