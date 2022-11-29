import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_file_format():

    st.title('File Formats')

    st.markdown("""
    Storage systems store your data in files with different formats. These different formats provide benefits to the users.
    File formats are specificaly designed to store specific types of information.
    How you store your data is critical so you need to consider the most optimal format to work with.
    Things to consider are:

    - Structure of your data
    - Easy to read and understand
    - Compatability

    """)

    st.title('What is the file format of your data?')

    st.markdown("""
                ### Take a look at your dataset in the folder where it is stored.\n
                The file contains a specific file extension which is found after the filename.
                For example, a file called dataset.csv has the file format comma-separated-value (.csv).
                Excel files would have the name: .xlsx or .xsl and files from text editors end with .txt.
                
                After you have found your file format, you can select it in the drop-down menu below:
                """)


    option = st.selectbox(
        'What is the file format of your data?',
        ['','csv','excel','txt','parquet','other'], format_func=lambda x: 'Select an option' if x == '' else x)
    

    if option == 'csv':
        st.success('You have an ideal data format!')
        "CSV files are structured in a [row, column] manner and are easy to work with."
        
        st.write(pd.DataFrame({
            'Sensor1': [1.21, 1.25, 1.31, 1.27],
            'Sensor2': [10.21, 10.33, 11.12, 10.87]
        }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"th",
                        "props":[("text-align","center")],
                        },
                        {"selector":"th:row_heading",
                        "props":[("display","None")],
                        },
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 1: Dataset.")\
                        .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)

        st.markdown('')
        st.warning('Also try saving your data with a comma that separates values: Var1, Var2 instead of Var1; Var2. That makes it easier to process the data in software since it assumes a comma as the seperator between values.')
        
    
    if option == 'excel':
        st.error('Better data formats are available depending on your goals!')

        col1, col2, col3 = st.columns([1,2.5,1])

        with col2:
            image = Image.open('images/excel_example.png')
            st.image(image, caption='Figure 1: Example of how Excel structures data.', use_column_width=True)


        st.markdown("""
        #### For simple manipulation of your data, and if programming knowledge is not available in your organization, we recommend to stick to Excel.
        However, if you are interested to learn more about data analytics, the standard way to store data is with a Comma Seperated Value file, called .csv.
        These files are just plain text files that store your data, which can be very easily used in any programming language to manipulate them.
        
        For example, Table 2 shows a very simple dataset similar to Figure 1. 
        However, the data format is just a plain text file which can be copy-pasted below and used in other programs or software:
        """)
        
        st.write(pd.DataFrame({
            'Sensor1': [1.21, 1.25, 1.31, 1.27],
            'Sensor2': [10.21, 10.33, 11.12, 10.87]
        }).style.set_table_styles([
                            {"selector":"caption",
                        "props":[("text-align","center"),("caption-side","top")],
                        },
                        {"selector":"th",
                        "props":[("text-align","center")],
                        },
                        {"selector":"td",
                        "props":[("text-align","center")],
                        },
                        {"selector":"",
                        "props":[("margin-left","auto"),("margin-right","auto")],
                        }

                        ]).set_caption("Table 2: Dataset.")\
                            .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)

        st.markdown("""

        This dataset is simply stored in a .csv file that looks like the following:
        """)

        code = '''
1.21, 10.21,
1.25, 10.33,
1.31, 11.12,
1.27, 10.87
        '''
        st.code(code, language='csv')

            
            
        
            
    if option == 'txt':
        st.success('You have an ideal data file format!')
        st.markdown(".txt files are just like .csv files, organised in a [row, column] manner and therefore are easy to work with.")
        

    if option == 'parquet':
        st.warning('Parquet is not the ideal data file format')
        st.markdown('Parquet files are column-based datasets which can be used. However, not many support documentation can be found on the web that help with processing this type of data. Please check with your data supplier if the data could be converted to .csv or .txt format.')

    if option == 'other':
        st.error('Your data file format is not commonly used')
        st.markdown('Please ask your data supplier for a .csv or .txt version of your data, because it is highly likely that errors will occur in the future due to the data file format you have.')
        

    