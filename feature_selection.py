from select import select
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 

from statsmodels.tsa.stattools import grangercausalitytests

def return_feature_selection():
    
    st.title('Create Correlation plots')
    
    st.markdown("""
    Correlation is a statistical term which refers to how close two variables have a linear relationship to each other.
    Variables that have a linear relationship tell us less about our dataset, since measuring one tells you something about the other.
    In other words, if two variables have a high correlation, we can drop one of the two!
    """)
    import pandas as pd
    iris_correlation = pd.read_csv('data/iris.csv')
    iris_correlation.insert(0,'Time', pd.date_range(start='1/1/2018', periods=iris_correlation.shape[0], freq='T'))
    iris_correlation.columns = ['Time','temperature1','temperature2','temperature3','temperature4']
    st.table(iris_correlation.head(5).style.format(precision=2)\
        .set_table_styles([
                        {"selector":"caption",
                        "props":[("text-align","center")],
                        }

                        ], overwrite=False)\

            .set_caption('Table 1.'))
    
    st.markdown("""
    Here you can see a correlation table where a 1 means two variables correlate and 0 means they don't.
    If you want to test this on your own data, try out the Data Analytics tool!         
    """)
    
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

    st.title('PCA Analysis')
    st.markdown('''
    Another technique to reduce the dimensionality of your dataset is by performing Principal Component Analysis.
    PCA uses a set of large variables by combining them together to retain as much information as possible.
    PCA dates back to the 1990's and is one of the most widely used analysis techniques in Data Science.
    ''')

    from sklearn.preprocessing import StandardScaler # for standardizing the Data
    from sklearn.decomposition import PCA # for PCA calculation

    import pandas as pd
    df = pd.read_csv('data/Turbine_Data.csv', parse_dates=["Unnamed: 0"])
    df['DateTime'] = df['Unnamed: 0'] 
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df['DateTime'] = pd.to_datetime(df['DateTime'], 
    format = '%Y-%m-%dT%H:%M:%SZ', 
    errors = 'coerce')


    df = df.iloc[33065:]

    df = df.drop(columns=['Blade1PitchAngle', 'Blade2PitchAngle', 'Blade3PitchAngle'])
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.drop(columns=['WTG'], axis=1, inplace=True)

    df.drop('ControlBoxTemperature', axis=1, inplace=True)

    all_values = df.copy()
    features = ['WindSpeed', 'RotorRPM', 'ReactivePower', 'GeneratorWinding1Temperature', 
        'GeneratorWinding2Temperature', 'GeneratorRPM', 'GearboxBearingTemperature', 'GearboxOilTemperature']

    # Separate data into Y and X 
    y = all_values['ActivePower']
    X = all_values[features]

    st.dataframe(X.head(40))

    sc = StandardScaler() # creating a StandardScaler object
    X_std = sc.fit_transform(X) # standardizing the data

    pca = PCA()

    def pcaplotter():
        fig, ax = plt.subplots(figsize=(8,3))
        plt.plot(np.cumsum(pca.explained_variance_ratio_))
        plt.gca().locator_params(nbins=max(ax.get_xlim())+1)
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')

        return fig

    aim_target = 0.98
    pca = PCA(n_components = aim_target)
    X_pca = pca.fit_transform(X_std) # this will fit and reduce dimensions

    st.pyplot(pcaplotter())
    pd.DataFrame(pca.components_, columns = X.columns)

    n_pcs= pca.n_components_ # get number of component
    # get the index of the most important feature on EACH component
    most_important = [np.abs(pca.components_[i]).argmax() for i in range(n_pcs)]
    initial_feature_names = X.columns
    # get the most important feature names
    most_important_names = [initial_feature_names[most_important[i]] for i in range(n_pcs)]
    most_important_names = list(dict.fromkeys(most_important_names))
    
    for i,j in enumerate(most_important_names):
        st.write(f"{i + 1}th most important variable = {j}")

    st.markdown("#### Explanation")
    st.markdown("""
    We can interpret the most important variables in the following way.
    With help of only the GeneratorWinding1Temperature variable, we can already explain around 87\% of the variance in the dataset.
    And with help of adding ReactivePower, around 94\% can be explained. 
    Again, this analysis can be performed with you own dataset in the Data Analytics tool!
                """)


