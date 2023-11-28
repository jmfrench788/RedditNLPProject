import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from utils.b2 import B2


#Cannot connect to endpoint. When I actually go to it, it says "Unauthenticated requests are not allowed for this api"
#So, I tried to do this without b2 for now

# ------------------------------------------------------
#                      APP CONSTANTS
# ------------------------------------------------------
REMOTE_DATA = 'RedditWordCount'


# ------------------------------------------------------
#                        CONFIG
# ------------------------------------------------------
load_dotenv()

# load Backblaze connection
#b2 = B2(endpoint=os.environ['B2_ENDPOINT'],
        #key_id=os.environ['B2_KEYID'],
        #secret_key=os.environ['B2_APPKEY'])


# ------------------------------------------------------
#                         APP
# ------------------------------------------------------
st.write()

#b2.set_bucket(os.environ['B2_BUCKETNAME'])

#df_words = b2.to_df(REMOTE_DATA)
df_words = pd.read_csv(REMOTE_DATA)
df_words.rename(columns={'Unnamed: 0': 'word'}, inplace=True)

df_allwords = df_words.set_index('word')
df_allwords.sort_index()

st.dataframe(df_allwords)

#Select by words

word_choice= st.multiselect('Select Words', df_allwords.index, default=None, key=None, help=None, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
df_choice= pd.DataFrame(word_choice)
df_update= df_allwords[df_allwords.index.isin(df_choice[0])]
st.write(df_update)

fig, ax = plt.subplots()

ax.bar(df_update.index,df_update['sum'])
ax.set_title('Count of Words')

show_graph = st.checkbox('Show Graph', value=True)

if show_graph:
    st.pyplot(fig)


st.write()

#Choose by category
df_categories=['Romance','Work','Technology','Family','Frequency','Health','School']
category_choice= st.selectbox('Select A Category', df_categories, placeholder="Choose an option", disabled=False, label_visibility="visible")
st.write("Category: ",category_choice)

#Get words based on category
def ChooseCat(category_chosen):
    category = category_chosen
    empty = []
    df_catWords = pd.DataFrame(empty)
    if category == 'Technology':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['phone','computer','media','video','videos','text','spotify','gmail','netflix','wifi','internet','password','passwords','youtube','email','app','ads','tv','movie','screen'])]
    #if category == 'Romance':
        #df_catWords=df_allwords.loc[df_allwords.index.isin(['phone','computer','media','video','videos','text','spotify','gmail','netflix','wifi','internet','password','passwords','youtube','email','app','ads','tv','movie','screen'])]

    return df_catWords

df_categoryWords = ChooseCat(category_choice)
st.write("Total Sum = ", sum(df_categoryWords['sum']))
st.write(df_categoryWords)

#Graph
fig2, ax2 = plt.subplots()

ax2.bar(df_categoryWords.index,df_categoryWords['sum'])
ax2.set_title('Count of Words')

st.pyplot(fig2)


    

