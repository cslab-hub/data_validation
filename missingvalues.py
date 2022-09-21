import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 



def return_missing_values():
    
    html_arrow = """<p style="text-align:center"><img src="https://github.com/cslab-hub/data_validation/blob/main/images/down-arrow.png?raw=true" width="50"></p>"""

    st.title('It could occur that various variables did not measure all time points.')

    st.markdown("""
    Missing data can be a serious issue for the quality of your dataset.
    But what do we mean by missing? Missing data means that one or more variables in your dataset have values missing that contain nothing, -999, nan or nul.
    These values most often originate from wrong data collection, a lack of data, or errors when entering data. 
    When conclusions are drawn from these dataset, drastic errors can be made!

    In general there are 2 types of missing data:
    - ###### Missing completely at random
    - ###### Missing at Random
    """)

    st.markdown('### Mising Completely at Random')
    st.markdown("""
    When the data is missing completely at random, we say that there is no relationship whether a data point is missing and other observations in the dataset.
    A simple way to check for missing data is by filtering a dataset on several assumptions, and check whether there are more missing values in one of them.
    If you data is missing completely at random, there should be no difference!
    """)

    # Create sample dataframe with resample example
    index = pd.date_range('1-1-2000', periods=9, freq='T')
    series = pd.Series(range(1,10), index=index)
    dataframe = pd.DataFrame(series, columns=['Measurement'])
    dataframe = dataframe.reset_index()
    dataframe.columns = ['Time','var1']
    dataframe["Time"] = pd.to_datetime(dataframe["Time"])
    dataframe["Time"] = dataframe["Time"].dt.strftime("%Y-%m-%d %H:%M:%S")
    
    df_values = dataframe.rolling(2, on='Time').mean()
    df = dataframe.iloc[::2, :]
    df['var1'] = df_values['var1']
    df = df.iloc[0:,:]

    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #ffdbdb; border-color: #ffbebe;">
                Bad Example 1: There are  various missing values scattered around your dataset.
                </div>""", unsafe_allow_html=True)


    st.markdown("""
    It could occur that the variables in your dataset have scattered missing values. 
    In this case, it is possible to delete these observations as well, but also imputing them from their neighbours. 
    For example, in the following toy example dataset, it is possible to infer the linear pattern in the data. 
    This is also possible with other kind of measurements!

    """)
    inconsistent_df = dataframe.copy(deep = True)
    inconsistent_df['var2'] = [1,2,np.nan,4,5,np.nan,7,8,9]
    inconsistent_df['var3'] = [1,np.nan,3,4,np.nan,6,np.nan,8,9]

    col1, col2, col3 = st.columns([1,6,1])
    with col2:

        st.write(inconsistent_df.style.set_table_styles([
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

                        ]).highlight_null(null_color='tomato').format(precision=0)\
                        .set_caption("Table 1: Dataset with random numbers missing.")\
                        .hide(axis='index')\
                        .to_html()\
                        , unsafe_allow_html=True)


    col1, col2, col3 , col4, col5 = st.columns(5)

    with col3 :
        st.markdown('')
        st.write(html_arrow, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        inconsistent_df['var2'] = inconsistent_df['var2'].interpolate().astype(int)
        inconsistent_df['var3'] = inconsistent_df['var3'].interpolate().astype(int)

        st.write(inconsistent_df.style.set_table_styles([
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

                        ]).highlight_null(null_color='tomato').format(precision=0)\
                        .set_caption("Table 2: Dataset the measurements imputed.")\
                        .hide(axis='index')\
                        .to_html()\
                        , unsafe_allow_html=True)


    st.markdown('')


    st.markdown('### Missing at Random')
    st.markdown("""
    When data is missing at random, the missing data is only caused by other variables in the dataset. 
    For example, it could occur that one variable in your dataset did not measure correctly every timepoint. 
    However, this is caused because another variable started recording earlier, so this 'missing' of the data is caused by the other variable measuring earlier.
    In this case, we advice to remove all the observations where even a single variable measured nothing, in order to prevent errors in the future analysis.\n
    """)
    st.write("""<div style="padding: 15px; text-align:center; border: 1px solid transparent; border-color: transparent; margin-bottom: 20px; border-radius: 4px;  background-color: #ffdbdb; border-color: #ffbebe;">
                Bad Example 2: Each variable started recording at different timepoints.
                </div>""", unsafe_allow_html=True)
    inconsistent_df = dataframe.copy(deep = True)
    inconsistent_df['var2'] = [np.nan, np.nan, np.nan,4,5,6,7,8,9]
    inconsistent_df['var3'] = [np.nan,np.nan,np.nan,np.nan,5,6,7,8,9]


    image = Image.open('images/down-arrow.png')

    col1, col2, col3 = st.columns([1,6,1])
    with col2:

        st.write(inconsistent_df.style.set_table_styles([
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

                        ]).highlight_null(null_color='tomato').format(precision=0)\
                        .set_caption("Table 3: Dataset with non-random numbers.")\
                        .hide(axis='index')\
                        .to_html()\
                        , unsafe_allow_html=True)

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col3 :
        st.markdown('')

        html_arrow = """<p style="text-align:center"><img src="https://github.com/cslab-hub/data_validation/blob/main/images/down-arrow.png?raw=true" width="50"></p>"""
        st.write(html_arrow, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,6,1])
    with col2:
        st.write(inconsistent_df.iloc[4:,:].style.set_table_styles([
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

                        ]).highlight_null(null_color='tomato').format(precision=0)\
                        .set_caption("Table 4: Dataset with missing measurements removed.")\
                        .hide(axis='index')\
                        .to_html()\
                        , unsafe_allow_html=True)

    