import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_column_names():

    # hide_table_row_index = """
    #         <style>
    #         tbody th {display:none}
    #         .blank {display:none}
    #         </style>
    #         """
    # st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('Open the dataset in your program by choice. What do the variable names look like?')
    
    st.markdown("""
    Notice the black bar highlighting the names of the variables in Table 1.
    Take a look your dataset in your own program (SublimeTexts, Microsoft Excel).
    
    """)

    col1, col2, col3 = st.columns([1,2.5,1])

    with col2:
        st.write(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
            }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"thead",
                        "props":[("text-align","center"),("border","3px solid black")],
                        },                   
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 1: Dataset.")\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)


    option = st.selectbox(
        'How do your variable names look like?',
        ['','Ex1Var1_01','Heat_sensor1','Drehzalh01',"heatsensor,1",'No Variable Names'],format_func=lambda x: 'Select an option' if x == '' else x)
    
    if option == 'Ex1Var1_01':
        st.write(pd.DataFrame({
                'Ex1Var1_01': [1.21, 1.25, 1.31, 1.27],
                'Ex1Var2_02': [10.21, 10.33, 11.12, 10.87],
                'Ex2Var25_i0': [11.21, 11.19, 11.15, 10.99],
                'Ex2Var29_i2': [11.15, 11.10, 10.98, 11.03],
            }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"thead",
                        "props":[("text-align","center")],
                        },                   
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 2: Random Dataset.")\
                        .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)
        
        st.subheader('Here are some tips to improve readability:')
        
        # st.error('Error Message')
        st.success('Tip 1: Only use upper of lowercase letters')
        st.success('Tip 2: Try to only use English variable names for generalizability with international colleagues')
        st.success("""Tip 3: Try to map each variable to a specific process. 
                   For example, perhaps Ex2Var29_i2 means the pressure in a specific instrument in your machinery.
                   The variable could then be named Pressure_instrument_1.""")
        
        
        # Advanced
        # html_temp = """
        # <div style="background-color:tomato;padding:10px">
        # <h2 style="color:white;text-align:center;">Markdown html Example </h2>
        # </div>
        # """
        # st.markdown(html_temp,unsafe_allow_html=True)
        
        
        # st.markdown(
        #     '<span class="badge badge-pill badge-success"> Badge </span>',
        #     unsafe_allow_html=True
        # )


    if option == 'Heat_sensor1':
        st.write(pd.DataFrame({
                'Heat_sensor1': [1.21, 1.25, 1.31, 1.27],
                'Heat_sensor2': [10.21, 10.33, 11.12, 10.87],
                'Pressure_sensor1': [11.21, 11.19, 11.15, 10.99],
                'Pressure_sensor2': [11.15, 11.10, 10.98, 11.03],
            }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"thead",
                        "props":[("text-align","center")],
                        },                   
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 2: Random Dataset.")\
                        .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)
        
        st.markdown('')
        st.success('Your column names are of great quality!')
        st.markdown("Your data contains easy to read variables and are interpretable for anybody.")
        
    if option == 'Drehzalh01':
        st.write(pd.DataFrame({
                'Drehzalh01': [1.21, 1.25, 1.31, 1.27],
                'Drehzalh02': [10.21, 10.33, 11.12, 10.87],
                'Drehseth01': [11.21, 11.19, 11.15, 10.99],
                'Drehseth02': [11.15, 11.10, 10.98, 11.03],
            }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"thead",
                        "props":[("text-align","center")],
                        },                   
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 2: Random Dataset.")\
                        .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)
        
        st.markdown('')
        st.warning('Your column are identifyable, but English names are easier to interpet')


    if option == 'No Variable Names':
        e = np.random.normal(size=(5,2))  
        e_dataframe = pd.DataFrame(e)
        e_dataframe.columns = [' ','  ']
        
        
        st.table(e_dataframe.style.format('{:.2f}'))
        
        st.warning("""Your data contains columns but are not identifyable by name.
                   Ask your data supplier for specific information about what each column/variable measures.
                   This is necessary, since it is now not possible to interpret the data, since you do not know what each variable represents.
                   """)
    
    if option == 'heatsensor,1':
        e = np.random.normal(size=(5,2))  
        e_dataframe = pd.DataFrame(e)
        e_dataframe.columns = ['heatsensorA,1','heatsensorB,2']
        
        
        # st.table(e_dataframe.style.format('{:.2f}'))
        
        st.error("""Your dataset could be read wronly if the delimiter of your dataset is a comma.
        What then happens is that the dataset will be split into the following dataset:
                   """)

        e_2 = e_dataframe.copy(deep = True)
        e_2['var1'] = e_2['heatsensorA,1']+2
        e_2['var2'] = e_2['heatsensorB,2']-1
        print(e_2.shape)
        e_2.columns = ['heatsensorA','1','heatsensorB','2']
        # st.table(e_2.style.format('{:.2f}'))
        st.table(e_2)

        st.markdown('''
        While your desired goal maybe actually the following dataset:
        ''')

        st.table(e_dataframe.style.format('{:.2f}'))