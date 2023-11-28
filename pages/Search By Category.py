import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from utils.b2 import B2

REMOTE_DATA = 'https://raw.githubusercontent.com/jmfrench788/RedditNLPProject/main/RedditWordCount'

df_words = pd.read_csv(REMOTE_DATA)
df_words.rename(columns={'Unnamed: 0': 'Word'}, inplace=True)
df_words.rename(columns={'sum': 'Sum'}, inplace=True)

df_allwords = df_words.set_index('Word')
df_allwords.sort_index()

def ChooseCat(category_chosen):
    category = category_chosen
    empty = []
    df_catWords = pd.DataFrame(empty)
    if category == 'Technology':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['link','file','data','cable','calling','call', 'calls', 'windows','online','phone','computer','media','video','videos','text','spotify','gmail','netflix','wifi','internet','password','passwords','youtube','email','app','ads','tv','movie','movies','screen'])]
    if category == 'Romance':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['love','loved','boyfriend','girlfriend','marriage','marry','romance','date','bf','gf','kiss','sex','husband','wife','partner','kissing', 'dating','ex'])]
    if category == 'Work':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['employee','employer','job','work','working','boss','hours','office'])]
    if category == 'Family':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['wife','husband','kids','kid','baby','father','mother','sister','family','brother','cousin'])]
    if category == 'Frequency':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['always', 'never', 'sometimes','often', 'rarely','usually','hardly','occasionally','seldom','normally','constantly','regularly','frequently','daily','weekly','yearly','annually','monthly','everyday','eventually'])]
    if category == 'Health':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['health','age','hospital','gym','unhealthy','body','run','exercise','diet','nutrition','food','nutritional','doctor','medicine','medical','ambulance','covid'])]
    if category == 'School':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['school','class','homework','teacher','grade','grades','test','exam'])]
    #Add in Money and check categories
    return df_catWords

#Choose by category
df_categories=['Romance','Work','Technology','Family','Frequency','Health','School']
category_choice= st.selectbox('Select A Category', df_categories, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.write("Category: ",category_choice)
df_categoryWords = ChooseCat(category_choice)
st.write("Total Count = ", sum(df_categoryWords['Sum']))

st.write(df_categoryWords)
fig2, ax2 = plt.subplots()

ax2.bar(df_categoryWords.index,df_categoryWords['Sum'])
ax2.set_title('Count of Words')

st.pyplot(fig2)



