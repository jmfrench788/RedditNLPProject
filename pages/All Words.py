import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


from utils.b2 import B2


REMOTE_DATA = 'https://raw.githubusercontent.com/jmfrench788/RedditNLPProject/main/RedditWordCount'

df_words = pd.read_csv(REMOTE_DATA)
df_words.rename(columns={'Unnamed: 0': 'Word'}, inplace=True)
df_words.rename(columns={'sum': 'Sum'}, inplace=True)

df_allwords = df_words.set_index('Word')
df_allwords.sort_index()

#df_tech=df_allwords.loc[df_allwords.index.isin(['phone','computer','media','video','videos','text','spotify','gmail','netflix','wifi','internet','password','passwords','youtube','email','app','ads','tv','movie','screen'])]
#st.dataframe(df_tech)

st.dataframe(df_allwords, height=5000)