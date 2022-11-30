import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_endresult():
    
    st.title('End result')

    st.markdown('''
    The end result of your dataset should look like the following: \n
    (1) There should be one variable that determines the time for all variables, please call this variable 'Time'. \n
    (2) All variables in your dataset should have a measurement at each moment in time of this "Time" variable, there are no missing values.
    ''')

    st.write(pd.DataFrame({
            'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
            'Sensor1': [10, 10, 11, 10],
            'Sensor2': [14,15,14,14],
            'Sensor3': [100.1,100.3,100.2,100.0],
            'Sensor4': [90.1,89.4,88.3,90]
        }).style.set_table_styles([
                    {"selector":"caption",
                    "props":[("text-align","center"),("caption-side","top")],
                    },                
                    {"selector":"td",
                    "props":[("text-align","center")],
                    },
                    {"selector":"",
                    "props":[("margin-left","auto"),("margin-right","auto")],
                    }

                    ]).set_caption("Table 1: The Dataset.")\
                    .format(precision=2)\
                    .hide(axis='index')\
                    .to_html()           
                    , unsafe_allow_html=True)
    st.text('')


    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #fef4d5; border-color: #fef4d5;">
                The [Data Analytics tool](https://github.com/cslab-hub/DataAnalytics_Diplast) expects this data format, in order to make it general for multiple companies to use.
                </div>""", unsafe_allow_html=True)
    
    col1,col2,col3 = st.columns([1,5,1])
    with col2:
        st.image('images/data_in_excel.png', caption='How Table 1 looks like in Excel')
    
        st.image('images/exportcsv.png', caption='How to export from Excel to CSV')