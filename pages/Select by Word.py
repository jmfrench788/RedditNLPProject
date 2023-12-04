
import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


from utils.b2 import B2

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

REMOTE_DATA = 'https://raw.githubusercontent.com/jmfrench788/RedditNLPProject/main/RedditWordCount'





df_words = pd.read_csv(REMOTE_DATA)
df_words.rename(columns={'Unnamed: 0': 'Word'}, inplace=True)
df_words.rename(columns={'sum': 'Sum'}, inplace=True)

df_allwords = df_words.set_index('Word')
df_allwords.sort_index()



word_choice= st.multiselect('Select Words', df_allwords.index, default=None, key=None, help=None, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
df_choice= pd.DataFrame(word_choice)
if df_choice.empty:
    st.write("Select one or more words")
else:
    df_update= df_allwords[df_allwords.index.isin(df_choice[0])]
    st.write(df_update)
    fig, ax = plt.subplots()
    ax.barh(df_update.index,df_update['Sum'])
    ax.set_title('Count of Words')
    ax.invert_yaxis()

    show_graph = st.checkbox('Show Graph', value=True)

    if(show_graph):
        st.pyplot(fig)




