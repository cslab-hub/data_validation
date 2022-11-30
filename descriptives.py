import streamlit as st
import pandas as pd
pd.set_option('display.colheader_justify', 'center')
import numpy as np
from PIL import Image 


def return_descriptives():

    st.title('Descriptives of your dataset')
    
    st.markdown("""
                It is also important to check the initial descriptives of your dataset.
                There are several ways to achieve this. 
                For example, consider the following dataset:
                """)

    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")


    dataframe['var2'] = dataframe['var1'] + np.random.randint(10,size=9)
    dataframe['var3'] = 1 + np.random.uniform(low=0.0001, high=0.1,size=9)
    dataframe['var4'] = 3
    
    dataframe = dataframe[['Time','var2','var3','var4']]

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

            .set_caption('Table 1: Sample dataset.')\
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
            .to_html()           
            , unsafe_allow_html=True)

    st.write('')
    st.markdown("""
                It is possible to learn the characteristics of the dataset by inspecting these summary statistics.
                For example, if we look at Table 2, which is visualized below, we can already see that the variable called: 'var4' does not deviate in its measurements.
                This could indicate that this variable does not provide any new information to us. Therefore this variable can be removed from the dataset.\n

                Second, we can see that the mean of the variable 'var2' is much higher than 'var3' or 'var4'. 
                If this behavior is expected, then it is okay. But, you should check every value to know what the variable represents.
                """)
    col1, col2, col3 = st.columns([1,5,1])
    
    with col2:
        st.write(dataframe.describe().style.set_table_styles([
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

            .set_caption('Table 2: Descriptives of the dataset.')\
            .format(precision=2)\
            .to_html()           
            , unsafe_allow_html=True)


    st.markdown("# Density plot of variables")

    st.markdown("""
                A quick inspection of your dataset can also be performed by looking at Density plots of your data.
                These density plots look at the distribution of all the values measured by a variable.
                It could be helpful to think about a 'safe' range of values where you expect a sensor's data to fall into.
                If the values of this variable deviate from the range of values when looking at the density plots, then it might be relevant to further inspect the data.
                """)

    iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    iris['sepal_width'] = iris['sepal_width'] + 90
    iris['sepal_length'] = iris['sepal_length'] + 90
    iris.columns = ['Temp1','Temp2','Temp3','Temp4','Temp5']

    import matplotlib.pyplot as plt
    iris_plot = iris[['Temp1','Temp2']].plot(kind='density', figsize=(8,4))
    iris_plot.set_xlabel("Temperature")
    iris_plot.set_ylabel("Density")
    st.pyplot(iris_plot.figure, clear_figure=True)


    st.markdown('# Data types of variables')
    st.markdown("""
                It is also possible to check the data types of your variables. 
                Consider Table 3, which is visualized below. The values of the variables are different from each other.
                For example, 'var3' is measuring a numerical value with decimals, while 'var2' and 'var4' is measuring a numerical value of whole numbers.  
                \n """)

                # You should ask yourself whether some variables should remain in your dataset.
                # Most often, 'word' based variables often resembles categorical variables, which could be target variables you want to predict.
                # E.g., your data contains an variable with the values = ['damage','no-damage'], where you want to predict if your product had damage or not, based on sensor values.
                # In that case, you would like to keep this variable in your dataset.
                # However, if your data contains a variable with non-valuable categorial data, you could remove it.
                # It is, therefore, always up to you to decide what should remain and what should be removed!
               

    st.write(dataframe.head(2).style.set_table_styles([
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

            .set_caption('Table 3: Sample dataset.')\
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
            .to_html()           
            , unsafe_allow_html=True)

    dtype_df = dataframe.dtypes.value_counts().reset_index()

    dtype_df.columns = ['VariableType','Count']
    dtype_df['VariableType'] = dtype_df['VariableType'].astype(str)
    dtypefig, dtypeax = plt.subplots(figsize=(8,4))
    dtypeax.set_yticks(np.arange(0,3,1))
    dtypeax.bar(dtype_df['VariableType'],dtype_df['Count'])
    st.pyplot(dtypefig)

    st.title('Unit of Measurements')
    st.markdown("""
    In order to draw correct conclusions from your data, the accuracy of your measurements and calculations are crucial.
    Measuring means measuring a comparison between standardized units and an unknown size.
    Without mentioning the standard unit to which the unknown is compared, the numbers in your dataset itself are meaningless.
    Therefore, we advice to find out the unit of measurement of every variable in your dataset.
    Some variables might be easy to interpet, e.g., temperature.
    However, some variables are a combination of several units (pressure, rotation speeds).
    Here, errors are easier made if not taken caution.
    For example, if the rotation per minute is measured but you think it means rotation per second, results from the analysis could be wrongly interpreted.
    Therefore:
    """)

    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #ceeed8; border-color: #ceeed8;">
                Tip: Create a seperate notebook/piece of paper where you write down the units of measurement for each variable
                </div>""", unsafe_allow_html=True)

    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #ceeed8; border-color: #ceeed8;">
                Bonus: Knowing the units of measurement makes it easier for colleagues to interpret your dataset
                </div>""", unsafe_allow_html=True)