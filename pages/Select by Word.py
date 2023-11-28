
import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from utils.b2 import B2


REMOTE_DATA = 'RedditWordCount'


load_dotenv()

# load Backblaze connection
#b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        #key_id=os.environ['B2_KEYID'],
        #secret_key=os.environ['B2_APPKEY'])

df_words = pd.read_csv(REMOTE_DATA)
df_words.rename(columns={'Unnamed: 0': 'Word'}, inplace=True)
df_words.rename(columns={'sum': 'Sum'}, inplace=True)

df_allwords = df_words.set_index('Word')
df_allwords.sort_index()



word_choice= st.multiselect('Select Words', df_allwords.index, default=None, key=None, help=None, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
df_choice= pd.DataFrame(word_choice)
if df_choice.empty:
    print("Select one or more words")
else:
    df_update= df_allwords[df_allwords.index.isin(df_choice[0])]
    st.write(df_update)
    fig, ax = plt.subplots()
    ax.bar(df_update.index,df_update['Sum'])
    ax.set_title('Count of Words')

    show_graph = st.checkbox('Show Graph', value=True)

    if(show_graph):
        st.pyplot(fig)




