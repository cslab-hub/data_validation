import streamlit as st
# st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
from PIL import Image 

def return_endresult():
    
    # hide_table_row_index = """
    #         <style>
    #         tbody th {display:none}
    #         .blank {display:none}
    #         </style>
    #         """
    # st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('End result')

    path = 'data/delimiter_tests/turbine_semicolon.csv'
    import csv
    def get_delimiter(file_path, bytes = 4096):
        sniffer = csv.Sniffer()
        data = open(file_path, "r").read(bytes)
        delimiter = sniffer.sniff(data).delimiter
        return delimiter



    import os
    # st.write(os.listdir("data/"))

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

    num_of_rows = st.slider('How many rows should we use first?', 1, 10000, 25)

    dataset = pd.read_csv(main_path + option,delimiter=get_delimiter(main_path+option), nrows=num_of_rows)
    dataset = dataset.iloc[0:int(dataset.shape[0] / 100),:]
    st.write(dataset.shape)

    st.dataframe(dataset.head(20), height=500)


    # options = st.multiselect(
    #  'Which variables do you want to keep?',
    #  [i for i in dataset.columns],dataset.columns[1], key=0)

    # st.dataframe(dataset[options])

    # visualized_options = st.multiselect(
    #  'Which variables do you want to keep?',
    #  [i for i in dataset.columns],dataset.columns[1], key=1)

    import matplotlib.pyplot as plt 
    import matplotlib.colors as mcolors
    colors = ['b','g','r','c','m','y','k','black']

    # for i,j in enumerate(visualized_options):
    #     fig, ax = plt.subplots(figsize=(8,3))
    #     ax.plot(dataset[j], label=j, c=colors[i],linewidth=1)
    #     ax.legend()
    #     st.pyplot(fig)



    #!  new test
    # from matplotlib import gridspec
    # import math

    # N = len(visualized_options)
    # cols = 2
    # rows = int(math.ceil(N / cols))
    # colors = ['b','g','r','c','m','y','k','black']

    # gs = gridspec.GridSpec(rows, cols)
    # fig = plt.figure(figsize=(12,3))
    # for n in range(N):
    #     ax = fig.add_subplot(gs[n])
    #     ax.plot(dataset[visualized_options[n]], label=visualized_options[n], c=colors[n],linewidth=1)
    #     ax.legend(fontsize=7)
    # fig.tight_layout()
    # st.pyplot(fig)


    st.title('test')

    from tdda.constraints import discover_df, verify_df

    constraints = discover_df(dataset)
    constraints_path = 'tdda_tests/' + option.split('.')[0] + '.tdda'
    with open(constraints_path, 'w') as f:
        f.write(constraints.to_json())
        
    #Show the generated constraints
    # st.write(str(constraints))
    df = pd.read_json(constraints.to_json(), orient='columns')
    df = df.drop(['local_time', 'utc_time','creator','host','user','n_records','n_selected'])
    df = df.drop(columns=['creation_metadata'])
    df = df.fields.apply(pd.Series)
    st.table(df)

    st.title('verify')
    v1 = verify_df(dataset, constraints_path, type_checking='strict', epsilon=0)
    # st.write(str(v1))
    st.table(v1.to_frame())
    
    

    # st.dataframe(pd.read_json(constraints.to_json(), orient='index'))
    st.title('Rrofiling')

    from pandas_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report
    profile = ProfileReport(dataset, title="Pandas Profiling Report", minimal=True)
    st_profile_report(profile)


#%%

# import pandas as pd 

# dataset = pd.read_csv("data/delimiter_tests/turbine_comma.csv",delimiter=',', nrows=20)
# dataset = dataset.iloc[0:int(dataset.shape[0] / 100),:]

# from tdda.constraints import discover_df, verify_df

# constraints = discover_df(dataset)
# constraints_path = 'tdda_tests/' + 'turbine_comma'.split('.')[0] + '.tdda'
# with open(constraints_path, 'w') as f:
#     f.write(constraints.to_json())
    
# df = pd.read_json(constraints.to_json(), orient='columns')
# df = df.drop(['local_time', 'utc_time','creator','host','user','n_records','n_selected'])
# df = df.drop(columns=['creation_metadata'])
# df = df.fields.apply(pd.Series)

# v1 = verify_df(dataset, constraints_path, type_checking='strict', epsilon=0)
# print(v1.to_frame())