#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect


# In[ ]:


menu_with_redirect()

st.markdown("hebben onderstaande onderdelen een zwaardere weging? de weging van de onderdelen staat standaard op 1. Als er onderdelen zijn die zwaarder wegen kunnen die hieronder aangepast worden.")

st.markdown("Aanschafprijs")
aanschafprijs = st.number_input("Weging", min_value=1)
st.markdown("Onderhoudsprijs")
onderhoudsprijs = st.number_input("Weging", min_value=1)
st.markdown("Mate van losmaakbaarheid")
losmaakbaarheid = st.number_input("Weging", min_value=1)
st.markdown("Toepassingsmogelijkheden")
toepassingsmogelijkheden = st.number_input("Weging", min_value=1)
st.markdown("Woonbeleving")
woonbeleving = st.number_input("Weging", min_value=1)
st.markdown("Milieubelasting")
milieubelasting = st.number_input("Weging", min_value=1)
st.markdown("Flexibiliteit tbv toekomstbestendigheid en innovatie")
flexibiliteit = st.number_input("Weging", min_value=1)
st.markdown("Mate van standaardisering")
standaardisering = st.number_input("Weging", min_value=1)

