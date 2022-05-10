#%%
import streamlit as st
import pandas as pd
# pd.set_option('mode.chained_assignment', None)
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt 
# from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
data.to_csv('data/anomaly.csv', index=None)
# fig = plt.plot(data['value'])

#%%
def first_plot(data, title):
    # fig = plt.figure()

    fig, ax = plt.subplots(figsize=(16,6))
    # ax.plot(data['value'])

    plt.scatter(data.index, data['value'], c='b', s=75)
    plt.plot(data.index, data['value'], linewidth=3)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")

    plt.ylim([-0.1,3.1])

    plt.title(title, fontsize=24)
    plt.xlabel("Time (seconds)", fontsize=22)
    plt.ylabel("Value", fontsize=22)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.5)
        ax.spines[axis].set_color("black")
        ax.spines[axis].set_zorder(0)
    ax.tick_params('both', length=10, width=2, which='major')

    return fig

# fig, ax = plt.subplots()
# ax.plot(data['value'])
fig1 = first_plot(data, 'Figure 1: Plotted Data')
#
# new plot with anomalies
#%%
data = pd.read_csv('https://raw.githubusercontent.com/DHI/tsod/main/tests/data/example.csv')
q_low = data["value"].quantile(0.05)
q_hi  = data["value"].quantile(0.95)

df_filtered = data[(data["value"] < q_hi) & (data["value"] > q_low)]
with pd.option_context('mode.chained_assignment', None):
    df_filtered['identifier'] = 'b'


#%%
##
og_set = set(data.index.to_list())
new_set = set(df_filtered.index.tolist())
og_set - new_set

# filtered_df_values = pd.DataFrame(data.loc[og_set - new_set])
filtered_df_values = pd.DataFrame(data.iloc[list(og_set - new_set),:])

filtered_df_values = filtered_df_values.sort_values('datetime')
# with pd.option_context('mode.chained_assignment', None):
    # data[data.bidder == 'parakeet2004']['bidderrate'] = 100
filtered_df_values['identifier'] = 'r'
final_df = df_filtered.combine_first(filtered_df_values)

#%%
final_df['value_grp'] = (final_df['value'].diff(1) != 0).astype('int')
# final_df.plot(x='datetime',y='value_grp')
# final_df[final_df['value_grp'] == 0, 'value_grp'] = 'r'
final_df.loc[final_df["value_grp"] == 0, "value_grp"] = 'r'
final_df.loc[final_df["value_grp"] == 1, "value_grp"] = 'b'

# final_df.loc[final_df["value_grp_seq"] == 0, "value_grp"] = 'b'
# final_df.loc[final_df["value_grp_seq"] == 1, "value_grp"] = 'r'

# print( 'value counts = ',final_df['value_grp_seq'].value_counts())
final_df.iloc[78:88,3] = 'r'

final_df.iloc[78:90,:]
#%%
# fig2, ax = plt.subplots()

# ax.scatter(data=final_df, x='datetime', y='value', c='identifier', cmap='Set3')
# ax.set(title='', xlabel='Time', ylabel='')

# ax.axes.xaxis.set_ticklabels([0,20,40,60,80,100,120])
# ax.set_xticks([0,20,40,60,80,100,120])

#%%
# fig3 = plt.Figure()
# plt.scatter(final_df.index, final_df['value'],c=final_df['identifier'],)
# plt.plot(final_df.index, final_df['value'])
# plt.title("Spotted Outliers")
# plt.xlabel("Time")
# plt.ylabel("Value")
# plt.show()

def outlier_spotter(title_set):
    # fig = plt.figure()
    fig3, ax = plt.subplots(figsize=(16,6))
    plt.scatter(final_df.index, final_df['value'],c=final_df['identifier'], s=75)
    plt.plot(final_df.index, final_df['value'], linewidth=3)
    plt.title("Figure 2: Spotted Outliers")
    plt.xlabel("Time")
    plt.ylabel("Value")

    plt.title(title_set, fontsize=24)
    plt.xlabel("Time (seconds)", fontsize=22)
    plt.ylabel("Value", fontsize=22)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.5)
        ax.spines[axis].set_color("black")
        ax.spines[axis].set_zorder(0)
    ax.tick_params('both', length=10, width=2, which='major')

    return fig3

first_fig = outlier_spotter(title_set="Figure 2: Spotted Point-Wise Outliers")


#%%
outliers_removed = final_df.copy(deep=True)

outliers_removed = outliers_removed[outliers_removed['identifier'] == 'b']
third_fig = first_plot(outliers_removed, 'Figure 3: Outliers Removed')
#%%
def pattern_wise_plot(title_set):
    # fig = plt.figure()
    fig4, ax = plt.subplots(figsize=(16,6))
    plt.scatter(final_df.index, final_df['value'],c=final_df['value_grp'], s=75)
    plt.plot(final_df.index, final_df['value'], linewidth=3)
    # plt.title("Figure 4: Spotted Pattern-Wise Outliers")
    plt.xlabel("Time")
    plt.ylabel("Value")

    plt.title(title_set, fontsize=24)
    plt.xlabel("Time (seconds)", fontsize=22)
    plt.ylabel("Value", fontsize=22)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.5)
        ax.spines[axis].set_color("black")
        ax.spines[axis].set_zorder(0)
    ax.tick_params('both', length=10, width=2, which='major')

    return fig4

pattern_wise_fig = pattern_wise_plot(title_set="Figure 4: Spotted Pattern-Wise Outliers")

# outliers_removed = final_df.copy(deep=True)

pattern_wise_df = final_df[final_df['value_grp'] == 'b']
pattern_wise_figure_2 = first_plot(pattern_wise_df, 'Figure 5: Pattern-Wise Outliers Removed')

# final_df.iloc[78:90,:]
#%%

def return_outliers():

    # hide_table_row_index = """
    #         <style>
    #         tbody th {display:none}
    #         .blank {display:none}
    #         </style>
    #         """
    # st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
    st.title('Outlier detection')
    
    st.markdown('''
    Finding outliers in time series means identifying unexpected or weird instances in your dataset.
    When considering data from a machine (time series data), there are a few categories:

    - Point-wise Outliers
    - Pattern-wise Outliers
    - System-wise Outliers
    ''')

    st.markdown('### Point-wise Outliers')

    st.markdown("""
    These outliers occur when small weird instances happen in a process.
    These errors mostly consist of one or more single instances that deviate from the rest of the data entirely or from its direct neighbours.
    Techniques to spot them are via checking them against the distribution of a variable, or locally by looking at its direct neighbours.


    As an example, Imagine you have a dataset with the following data:\n              
                """)

    
    col1, col2, col3 = st.columns([1,2.5,1])
    col2.write(data.head(10).style.set_table_styles([
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

                        ]).set_caption("Table 1: Dataset with random numbers.")\
                        .format(precision=2)\
                        # .hide_index()\
                        .hide(axis='index')\
                        .to_html()           
                        , unsafe_allow_html=True)

    st.markdown("""
                It is hard to spot wether something is wrong with this dataset by looking at it in a table manner. 
                Therefore, if we plot the data, something different becomes visible:         
                """)
    
    st.pyplot(fig1)
    st.markdown("""
                Several of these points are showing very strange values on the y-axis. 
                These can be spotted and filtered out by so called: Anomaly Detection algorithms.
                A simple anomaly detection algorithm applied here labels anomalies if they are outside a certain boundary.
                However, there are countless techniques to achieve this results, one more complex than the other.
                If you think that you dataset could benefit from removing outliers, consider removing them!              
                """)
    
    st.pyplot(first_fig)
    # st.pyplot(fig3)

    st.markdown("""
                The following Figure shows the same data, but with the outliers removed:        
                """)
    st.pyplot(third_fig)

    st.markdown("""
                A few observations can be made from this visualization. To start, the overall dynamics of the dataset have not changed. 
                Plenty of information is still available, only the outliers have been removed.        
                """)

    

    st.markdown('### Pattern-wise Outliers')
    st.markdown('''
    Pattern-wise outliers always consist of a subsequence of observations in your data that behave differently.
    So instead of a few observations, pattern-wise outliers could consists of 100 observations that deviate.
    
    ''')
    
    st.pyplot(pattern_wise_fig)
    st.pyplot(pattern_wise_figure_2)


    st.markdown('### System-wise Outliers')
    st.markdown('''
    System-wise outliers are only visible when compared against other variables in it's 'system'.
    For example, the following plot shows one 'ideal' variable colored in blue, and two variables (in green and orange) that have a more chaotic nature.

    ''')
    t = np.linspace(0.0, 19, 100)       # time axis
    sig = np.sin(t)
    # random.uniform(0, 1)
    import random
    from matplotlib.ticker import MaxNLocator
    sig2 = [i + random.uniform(0, 0.3) for i in sig]
    sig3 = [i - random.uniform(0, 0.3) for i in sig]

    def system_wise_plot():
        # fig = plt.figure()
        fig5, ax = plt.subplots(figsize=(16,6))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        t = np.linspace(0, 19, 100)       # time axis
        sig = np.sin(t)
        # random.uniform(0, 1)
        sig2 = [i + random.uniform(0, 0.3) for i in sig]
        sig3 = [i - random.uniform(0, 0.3) for i in sig]

        plt.plot(t,sig, linewidth=3)
        plt.plot(t,sig2,linewidth=3)
        plt.plot(t,sig3,linewidth=3)
        plt.title("Figure 6: Spotted System-Wise Outliers", fontsize=24)
        plt.xlabel("Time (seconds)", fontsize=22)
        plt.ylabel("Value", fontsize=22)
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)

        for axis in ['top','bottom','left','right']:
            ax.spines[axis].set_linewidth(1.5)
            ax.spines[axis].set_color("black")
            ax.spines[axis].set_zorder(0)
        ax.tick_params('both', length=10, width=2, which='major')

        return fig5

    system_wise_plot_fig = system_wise_plot()
    st.pyplot(system_wise_plot_fig)