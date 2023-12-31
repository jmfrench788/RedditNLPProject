
import os
import json

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st



st.set_page_config(
    page_title="Welcome",
)

with open('style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)



st.title("Reddit: r/LifeProTips")



st.write('This is a collection of over 1,000 posts from r/LifeProTips. Each post was broken down into separate words, the words were counted, and some were sorted into categories.')
st.write('These 597 words only include the ones that were used over 5 times.')








    

