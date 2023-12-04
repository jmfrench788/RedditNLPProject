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

def ChooseCat(category_chosen):
    category = category_chosen
    empty = []
    df_catWords = pd.DataFrame(empty)
    if category == 'Technology':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['link','file','data','cable','calling','call', 'calls', 'windows','online','phone','computer','media','video','videos','text','spotify','gmail','netflix','wifi','internet','password','passwords','youtube','email','app','ads','tv','movie','movies','screen','download','picture','pictures','reddit','photo','photos','website','security','camera','documents'])]
    if category == 'Romance':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['single','love','loved','boyfriend','girlfriend','marriage','marry','romance','date','bf','gf','kiss','sex','husband','wife','partner','kissing','wedding'])]
    if category == 'Work':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['employee','employer','job','work','working','boss','hours','office','company','manager','store','position','salary','staff','volunteer','resume','presentation','employers','employees','workplace','product','budget','task', 'transfer','companies','sale','security','hr','interview','opportunity','career'])]
    if category == 'Family':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['wife','husband','kids','kid','baby','father','mother','sister','family','brother','cousin', 'home','children','child'])]
    if category == 'Frequency':
        df_catWords=df_allwords.loc[df_allwords.index.isin(['always', 'never', 'sometimes','often', 'rarely','usually','hardly','occasionally','seldom','normally','constantly','regularly','frequently','daily','weekly','yearly','annually','monthly','everyday','eventually'])]
    if category == 'Health':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['health','age','hospital','gym','unhealthy','body','run','exercise','diet','nutrition','food','nutritional','doctor','medicine','medical','ambulance','covid','water','eat','walk','drink','mental','brain','sleep','meal','emergency','eating','memory','mood','drinking','physical','mouth','environment','air','walking','stress','weight','shower','cold'])]
    if category == 'School':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['school','class','homework','teacher','grade','grades','test','exam','college','presentation','book', 'transfer'])]
    if category == 'Money':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['money','buy', 'house', 'car', 'buying', 'pay', 'save', 'free','clothes','college','gift','gifts','account','trip','trips','cost','vacation','salary','cheaper','restaurant','charge','card','cheap','vehicle','homeless','poor','bill','donate','paying','accounts','budget','transfer','sale','discount'])]
    if category == 'Relationships':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['relationship','boyfriend','girlfriend','bf','gf','husband','wife','partner','friend','employee','employer','boss','kids','kid','baby','father','mother','sister','family','brother','cousin','child','member','neighbors' ])]
    if category == 'Entertainment':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['media','video','videos', 'spotify', 'netflix', 'youtube', 'app', 'tv','television','movie','hobby','cable'])]
    if category == 'Events':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['party','christmas','wedding','trip','trips','night','vacation','date','event','emergency','presentation','flights','flight'])]
    if category == 'Pets':
       df_catWords=df_allwords.loc[df_allwords.index.isin(['dog', 'dogs','cat','cats','pet','pets','vet','animal'])]
    #Add in Money and check categories
    return df_catWords

#Choose by category
df_categories=['Romance','Work','Technology','Family','Frequency','Health','School','Relationships','Money','Entertainment','Events','Pets']
category_choice= st.selectbox('Select A Category', df_categories, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.write("Category: ",category_choice)
df_categoryWords = ChooseCat(category_choice)
st.write("Total Count = ", sum(df_categoryWords['Sum']))

st.write(df_categoryWords)
fig2, ax2 = plt.subplots()

ax2.barh(df_categoryWords.index,df_categoryWords['Sum'])
ax2.set_title('Count of Words')
ax2.invert_yaxis()

st.pyplot(fig2)



