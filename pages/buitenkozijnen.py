#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd


# In[ ]:


st.title("Projecten Eigen Haard")
st.header("Buitenkozijnen, -ramen, -deuren en -puien")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

if option == 'Nieuwbouw woningen':
    value = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
    besparen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


