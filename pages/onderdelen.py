#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect


# In[ ]:


menu_with_redirect()

st.markdown("hebben onderstaande onderdelen een zwaardere weging? de weging van de onderdelen staat standaard op 1. Als er onderdelen zijn die zwaarder wegen kunnen die hieronder aangepast worden.")

aanschafprijs = st.number_input("weging aanschafprijs", min_value=1)
onderhoudsprijs = st.number_input("weging onderhoudsprijs", min_value=1)
losmaakbaarheid = st.number_input("weging mate van losmaakbaarheid", min_value=1)
toepassingsmogelijkheden = st.number_input("weging toepassingsmogelijkheden", min_value=1)
woonbeleving = st.number_input("weging woonbeleving", min_value=1)
milieubelasting = st.number_input("weging milieubelasting", min_value=1)
flexibiliteit = st.number_input("weging flexibiliteit", min_value=1)
standaardisering = st.number_input("weging mate van standaardisering", min_value=1)

