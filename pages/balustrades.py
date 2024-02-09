#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect

menu_with_redirect()


st.subheader("Balustrades en leuningen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")


value = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
besparen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


st.page_link("water.py", label="Warm- en koud water installaties")

