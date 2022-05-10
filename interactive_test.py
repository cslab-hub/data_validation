import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 

def return_interactive():
    
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('End result')

    path = 'data/delimiter_tests/turbine_semicolon.csv'
    import csv
    def get_delimiter(file_path, bytes = 4096):
        sniffer = csv.Sniffer()
        data = open(file_path, "r").read(bytes)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter

    show_first_table = False
    show_second_table = False
    import os

    def files(path):  
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                yield file

    filelist = []
    for file in files("data/delimiter_tests/"):  
        extension = file.split('.')[-1]
        if str(extension) in ['csv','txt','xlxs']:
            filelist.append(file)

    option = st.selectbox(
     'Which dataset do you want to investigate?',
     ([i for i in filelist]))

    st.write('You selected:', option)
    main_path = 'data/delimiter_tests/'
    st.write('delimiter used in this file was automatically detected and determined on = ',get_delimiter(main_path + option))

    num_of_rows = st.slider('How many rows should we use first?', 1, 3000,1)

    dataset = pd.read_csv(main_path + option,delimiter=get_delimiter(main_path+option), nrows=num_of_rows)
    st.write(f'there are a total of {dataset.shape[0]} observations and {dataset.shape[1]} variables in this dataset')
    
    if num_of_rows == 1:
        print()
    elif show_second_table == True:
        print()
    else:
        show_first_table = True

    if show_first_table == True:
        st.dataframe(dataset.head(num_of_rows), height=500)
    
    time_var_options = dataset.columns
    time_var_options = time_var_options.insert(0,'Select an option')
    time_var = st.selectbox(
     'Which variable contains time?',
     ([i for i in time_var_options]))

    end_df = pd.read_csv(main_path + option,delimiter=get_delimiter(main_path+option), nrows=num_of_rows)
    

    # placeholder = st.empty()
    # if not st.checkbox("Hide dataframe"):
    #     df = pd.DataFrame(range(0, 10))
    #     placeholder.dataframe(df)

    st.dataframe(end_df)