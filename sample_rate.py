import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 



def return_sample_rate():
    
    # hide_table_row_index = """
    #         <style>
    #         tbody th {display:none}
    #         .blank {display:none}
    #         </style>
    #         """
    # st.markdown(hide_table_row_index, unsafe_allow_html=True)


    html_arrow = """<p style="text-align:center"><img src="https://github.com/cslab-hub/Data_Validation_DIPLAST/blob/main/images/down-arrow.png?raw=true" width="50"></p>"""


    st.title('Determine the Sample Rate')
    st.markdown("""
    Now that we have determined sensible column names and reduced our dataset to a few variables, we can investigate other aspects of our data.
    One of the first things to check is the sample rate of your dataset.
    It is very likely that one of the first variables in your dataset looks like the following (highlighted in green):
    
    """)
    # st.markdown(<font color=‘red’>THIS TEXT WILL BE RED</font>, unsafe_allow_html=True)))

    def color_column(val):
        color = 'lightgreen'
        return f'background-color: {color}'


    col1, col2, col3 = st.columns([1,5,1])

    with col2:
        st.write(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
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

                        ], overwrite=False)\

            .set_caption('Table 1. Random Dataset where each second an observation is recorded.')\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            .hide(axis='index')\
            .to_html()\
            # .hide_index()
            
            , unsafe_allow_html=True)




    st.markdown('')
    st.markdown("""
                In this dataset, the time variable reflects each moment an observation is recorded.
                This means that every second, each variable in your dataset takes a measurement.
                It could, however, also be the case that your data looks like the following, where every 5 minutes the data is recorded:
                """)
    
    col1, col2, col3 = st.columns([1,2.5,1])
    
    with col2:
        st.write(pd.DataFrame({
                'Time': ['21-12-21 10:00:00', '21-12-21 10:05:00','21-12-21 10:10:00','21-12-21 10:15:00'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
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

                        ], overwrite=False)\

            .set_caption('Table 2: Random dataset with a measure taken every 5 minutes.')\
            # .hide_index()\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
            .hide(axis='index')\
            .to_html()           
            , unsafe_allow_html=True)
    
    # st.markdown('Which means that every 5 minutes your data is recorded.')
    st.markdown("")
    # st.warning('It depends on your goal wheter or not every second or every 5 minutes is prefered')
    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #fef4d5; border-color: #fef4d5;">
                It depends on your goal wheter or not every second or every 5 minutes is prefered
                </div>""", unsafe_allow_html=True)
    
    st.markdown("""
                For example, imagine that the dataset your interested in measures the total stock of a certain material.
                It is ofcourse not neccesary to measure the total stock every second, especially of your stock data only changes every few hours on average.
                However, when the pressure or temperature in an Extruder is to be analysed, more observations help alot!
                Therefore, you shoul talk with your IT department for the best sample rate for your analysis goals!
                
                """)
    
    
    
    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #ffdbdb; border-color: #ffdbdb;">
                Watch out if your data looks like the following:
                </div>""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,10,1])

    with col2:
        st.write(pd.DataFrame({
                'Time': ['0', '1','2','3'],
                'Sensor1': [10, 10, 11, 10],
                'Sensor2': [14,15,14,14]
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

                        ], overwrite=False)\

            .set_caption('Table 3: Dataset without any information about difference in time.')\
            
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
            .hide(axis='index')\
            .to_html(index=False)           
            , unsafe_allow_html=True)
    st.markdown('')
    st.markdown("""
                In this case, there is no notion of time. The only information available is the order of the observations.
                In this case, we advice you to figure out what the sample rate of you dataset is. 
                
                In addition, it is also possible to change the sample rate in your dataset. 
                Consider the following dataframe where each minute a sample is taken from a variable called 'Measure'.
                This dataset could be reduced in size by taken the average of sequential rows, which is visible in Table in the following two tables: 
                """)
    
    st.title('How to improve')
    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 50px; border-radius: 4px;  background-color: #ceeed8; border-color: #ceeed8;">
                Tip 1: Calculate rolling average to smooth out observations
                </div>""", unsafe_allow_html=True)

    # st.success('Tip 1: Calculate rolling average to smooth out observations')
    
    st.markdown("""
    Consider the following dataset where the Variable 'var1' measures a random variable that counts up.
    However, it could be that the dataset is way to big, and needs some resampling to reduce the number of observations.
    Therefore, a technique called 'resampling' takes the average value for some time periods to reduce the dataset.
    """)

    # Create sample dataframe with resample example
    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    # df_values = dataframe.rolling(2).mean() 
    # df_values = dataframe.rolling(2).mean()
    df_values = dataframe.rolling(2, on='Time').mean()
    df = dataframe.iloc[::2, :]
    df['var1'] = df_values['var1']
    df = df.iloc[1:,:]
    df['var1'] = ['2.5','4.5','6.5','8.5']

    col1, col2, col3 = st.columns([1,5,1])
    
    with col2:            
        st.write(dataframe.style.set_table_styles([
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

                        ], overwrite=False)\

            .set_caption('Table 4: Measurements taken every minute.')\
            # .hide_index()\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
            .hide(axis='index')\
            .to_html()           
            , unsafe_allow_html=True)

        st.markdown("")  

        st.markdown('')
        st.write(html_arrow, unsafe_allow_html=True)

        st.write(df.style.set_table_styles([
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

                        ], overwrite=False)\

            .set_caption('Table 5: Average Taken of every 2 minutes.')\
            # .hide_index()\
            .set_table_styles({"Time" : [
                            {
                                "selector" :"th",
                                "props": "background-color:lightgreen;"
                            },
                            
                            {
                                "selector" :"td",
                                "props": "background-color:lightgreen;"
                            }
                        ]
                    }, overwrite=False)\
            # .applymap(lambda x: "background-color: lightgreen", subset="var1")\
            .hide(axis='index')\
            .to_html()           
            , unsafe_allow_html=True)



## Combine multiple table styles

    # with col2:
    #     st.table(pd.DataFrame({
    #             'Time': ['21-12-21 10:00:00', '21-12-21 10:00:01','21-12-21 10:00:02','21-12-21 10:00:03'],
    #             'Sensor1': [10, 10, 11, 10],
    #             'Sensor2': [14,15,14,14]
    #         }).style.set_table_styles([
    #                         {
    #                             "selector":"thead",
    #                             "props": [("background-color", "dodgerblue"), ("color", "white"),
    #                                       ("border", "3px solid red"),
    #                                       ("font-size", "2rem"), ("font-style", "italic")],
      
    #                         },
    #                         {
    #                             "selector":"th.row_heading",
    #                             "props": [("background-color", "orange"), ("color", "green"),
    #                                       ("border", "3px solid black"),
    #                                       ("font-size", "2rem"), ("font-style", "italic")]
    #                         },
    #                        {"selector":"caption",
    #                         "props":[("text-align","center")],
    #                        }

    #                     ], overwrite=False)\
    #                     .set_caption('test')\
    #                     .set_table_styles({"Time" : [
    #                                     {
    #                                         "selector" :"td",
    #                                         "props": "border: 2px solid red; color:green; background-color:yellow;"
    #                                     }
    #                                 ]
    #                           }, overwrite=False))