from select import select
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 

# import seaborn as sns
from statsmodels.tsa.stattools import grangercausalitytests

def return_feature_selection():
    
    hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('Create Correlation plots')
    
    st.markdown("""
    Correlation is a statistical term which refers to how close two variables have a linear relationship to each other.
    Variables that have a linear relationship tell us less about our dataset, since measuring one tells you something about the other.
    In other words, if two variables have a high correlation, we can drop on of the two!
    """)
    import pandas as pd
    iris_correlation = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
    iris_correlation = iris_correlation.iloc[:,:4]
    iris_correlation.columns = ['temperature1','temperature2','temperature3','temperature4']
    st.table(iris_correlation.head(5).style.format(precision=2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1.'))
    corr = iris_correlation.corr().round(2)
    corr.style.background_gradient(cmap='coolwarm')
    st.table(corr.style.background_gradient(cmap='coolwarm')\
        .format(precision=2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\
            

            .set_caption('Table 2.'))

#     st.title('Granger Causality')
#     st.markdown("""The Granger Causality is a statistical test for finding out wether one timeseries is usefull in forecasting another.
#     In other words, a variable X granger-causes variable Y, of the values of X provide statistical significant information about future values of Y.


    
    
#     """)

#     #build the time series, just a simple AR(1)
#     np.random.seed(2)
#     t1 = [0.1*np.random.normal()]
#     for _ in range(45):
#         t1.append(0.5*t1[-1] + 0.1*np.random.normal())

#     t2 = [item + 0.1*np.random.normal() for item in t1]
#     t2 = [item + 0.03*np.random.normal() for item in t1]

#     t1 = t1[3:]
#     t2 = t2[:-3]

#     def grangercausality():
#         fig, ax = plt.subplots(figsize=(8,3))

#         plt.figure(figsize=(7,2))
#         ax.plot(t1, color='b')
#         ax.plot(t2, color='r')

#         ax.annotate('Lagging Peak', xy=(12, 0.2),  xycoords='data',
#             xytext=(0.6, 0.95), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             horizontalalignment='right', verticalalignment='top',
#             )

#         ax.annotate('Lagging Low', xy=(28.5, -0.2),  xycoords='data',
#             xytext=(0.9, 0.2), textcoords='axes fraction',
#             arrowprops=dict(facecolor='black', shrink=0.1),
#             horizontalalignment='right', verticalalignment='top',
#             )
#         ax.set_title("Figure 1: Granger Causality with peaks highlighted by arrows.", y=-0.25)
#         ax.legend(['Original', 'Lagged'], fontsize=8)

#         return fig

#     st.pyplot(grangercausality())

#     selection_taken = st.slider(
#         'Select how many monents in time to look back:',
#         1, 6)

# #
#     ts_df = pd.DataFrame(columns=['t2', 't1'], data=zip(t2,t1))
#     gc_res = grangercausalitytests(ts_df, selection_taken,verbose=False)
#     for i,j in enumerate(gc_res.values()):
#         combined = round(np.mean([j[0]['ssr_ftest'][1], j[0]['ssr_chi2test'][1]]),3)
#         st.write(f"P-value after {i} lags <= {combined}")


    #######################################################
    st.title('PCA Analysis')
    st.markdown('''
    Another technique to reduce the dimensionality of your dataset is by performing Principal Component Analysis.
    PCA uses a set of large variables by combining them together to retain as much as information as possible.
    PCA dates back to the 1990's and is one of the most widely used analysis techniques in Data Science.
    ''')

    from sklearn.preprocessing import StandardScaler # for standardizing the Data
    from sklearn.decomposition import PCA # for PCA calculation

    import pandas as pd
    df = pd.read_csv('data/Turbine_Data.csv', parse_dates=["Unnamed: 0"])
    df['DateTime'] = df['Unnamed: 0'] 
    df.drop('Unnamed: 0', axis=1, inplace=True)
    # Add datetime parameters 
    df['DateTime'] = pd.to_datetime(df['DateTime'], 
    format = '%Y-%m-%dT%H:%M:%SZ', 
    errors = 'coerce')


    df = df.iloc[33065:]

    # Drop Blade1PitchAngle columns due to high number of missing values
    # df = df.drop(['Blade1PitchAngle', 'Blade2PitchAngle', 'Blade3PitchAngle'], 1)
    df = df.drop(columns=['Blade1PitchAngle', 'Blade2PitchAngle', 'Blade3PitchAngle'])
    df.fillna(df.mean(numeric_only=True), inplace=True)
    # Drop WTG column because it doesn't add much
    df.drop(columns=['WTG'], axis=1, inplace=True)

    # Drop ControlBoxTemperature column because it doesn't add much
    df.drop('ControlBoxTemperature', axis=1, inplace=True)

    # st.dataframe(df.head(40))
    all_values = df.copy()
    # all_values.to_csv('data/delimiter_tests/turbine.csv', index=False)
    features = ['WindSpeed', 'RotorRPM', 'ReactivePower', 'GeneratorWinding1Temperature', 
        'GeneratorWinding2Temperature', 'GeneratorRPM', 'GearboxBearingTemperature', 'GearboxOilTemperature']

    # Separate data into Y and X 
    y = all_values['ActivePower']
    X = all_values[features]

    st.dataframe(X.head(40))

    sc = StandardScaler() # creating a StandardScaler object
    X_std = sc.fit_transform(X) # standardizing the data

    pca = PCA()
    # X_pca = pca.fit(X_std)

    def pcaplotter():
        fig, ax = plt.subplots(figsize=(8,3))
        # max_bins = int(max(ax.get_xlim()) + 2)
        # print('max bins = ',max_bins)
        plt.plot(np.cumsum(pca.explained_variance_ratio_))
        # ax.set_xticks([i for i in range(1,max(ax.get_xlim())+2)])
        # ax.set_xticks([i for i in range(1,max_bins,1)])
        # ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.gca().locator_params(nbins=max(ax.get_xlim())+1)
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')

        return fig

    # st.pyplot(pcaplotter())

    # num_components = 4
    # pca = PCA(num_components)  
    # X_pca = pca.fit_transform(X_std) # fit and reduce dimension
    # print(pca.n_components_)
    # aim_target = st.slider('How much variance should be explained?', min_value=0.9, max_value=0.99, step=0.01, value=0.95)
    aim_target = 0.98
    pca = PCA(n_components = aim_target)
    X_pca = pca.fit_transform(X_std) # this will fit and reduce dimensions
    # st.markdown(f'{pca.n_components_}') # one can print and see how many components are selected. In this case it is 4 same as above we saw in step 5

    st.pyplot(pcaplotter())
    pd.DataFrame(pca.components_, columns = X.columns)

    n_pcs= pca.n_components_ # get number of component
    # get the index of the most important feature on EACH component
    most_important = [np.abs(pca.components_[i]).argmax() for i in range(n_pcs)]
    initial_feature_names = X.columns
    # get the most important feature names
    most_important_names = [initial_feature_names[most_important[i]] for i in range(n_pcs)]
    most_important_names = list(dict.fromkeys(most_important_names))
    # st.markdown(f'The most outstanding variables in your dataset are in order from important to less important: {most_important_names}')
    
    for i,j in enumerate(most_important_names):
        st.write(f"{i + 1}th most important variable = {j}")

    # list(dict.fromkeys(most_important_names))




