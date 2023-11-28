
import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


from utils.b2 import B2


st.set_page_config(
    page_title="Welcome",
)


st.title('Reddit: r/LifeProTips ')

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.write('This is a collection of over 1,000 posts from r/LifeProTips. Each post was broken down into separate words, the words were counted, and some were sorted into categories.')








    

