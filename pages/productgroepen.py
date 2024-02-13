#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect


# In[ ]:


menu_with_redirect()


# #### Balustrades en leuningen

# In[ ]:


with st.container(border=True):
    st.subheader("**Balustrades en leuningen**")
    st.markdown("*Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?*")

    v_balustrades = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=1)
    b_balustrades = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=2)


# #### Beveiliging

# In[ ]:


with st.container(border=True):
    st.subheader("Beveiliging")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_beveiliging = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 2), key=3)
    b_beveiliging = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=4)


# #### Binnenkozijnen en deuren

# In[ ]:


with st.container(border=True):
    st.subheader("Binnenkozijnen en deuren")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_binnenkozijnen = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=5)
    b_binnenkozijnen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=6)


# #### Binnenwandafwerkingen

# In[ ]:


with st.container(border=True):
    st.subheader("Binnenwandafwerkingen")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_binnenwandafwerkingen = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=7)
    b_binnenwandafwerkingen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=8)


# #### Binnenwanden

# In[ ]:


with st.container(border=True):

    st.subheader("Binnenwanden")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_binnenwanden = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=9)
    b_binnenwanden = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=10)


# #### Buitenkozijnen, -ramen, -deuren en -puien

# In[ ]:


with st.container(border=True):

    st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_buitenkozijnen = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=11)
    b_buitenkozijnen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=12)


# #### Buitenwanden

# In[ ]:


with st.container(border=True):

    st.subheader("Buitenwanden")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_buitenwanden = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=13)
    b_buitenwanden = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=14)


# #### Daken

# In[ ]:


with st.container(border=True):

    st.subheader("Daken")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_daken = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=15)
    b_daken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=16)


# #### Elektrische installaties

# In[ ]:


with st.container(border=True):

    st.subheader("Elektrische installaties")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_elektra = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=17)
    b_elektra = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=18)


# #### Vaste gebouwvoorzieningen

# In[ ]:


with st.container(border=True):

    st.subheader("Vaste gebouwvoorzieningen")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_gebouwvoorzieningen = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=19)
    b_gebouwvoorzieningen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=20)


# #### Hoofddraagconstructie

# In[ ]:


with st.container(border=True):

    st.subheader("Hoofddraagconstructie")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_hoofddraagconstructie = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=21)
    b_hoofddraagconstructie = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=22)


# #### Na-isolatie binnen

# In[ ]:


with st.container(border=True):

    st.subheader("Na-isolatie binnen")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_isolatie = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=23)
    b_isolatie = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=24)


# #### Keuken

# In[ ]:


with st.container(border=True):

    st.subheader("Keuken")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_keuken = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=25)
    b_keuken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=26)


# #### Lift

# In[ ]:


with st.container(border=True):

    st.subheader("Lift")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_lift = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=27)
    b_lift = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=28)


# #### Luchtbehandeling

# In[ ]:


with st.container(border=True):

    st.subheader("Luchtbehandeling")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_luchtbehandeling = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=29)
    b_luchtbehandeling = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=30)


# #### Luiken en vensters

# In[ ]:


with st.container(border=True):

    st.subheader("Luiken en vensters")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_luiken = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=31)
    b_luiken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=32)


# #### Plafonds

# In[ ]:


with st.container(border=True):

    st.subheader("Plafonds")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_plafonds = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=33)
    b_plafonds = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=34)


# #### Riolering en HWA

# In[ ]:


with st.container(border=True):

    st.subheader("Riolering en HWA")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_riolering = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=35)
    b_riolering = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=36)


# #### Sanitair

# In[ ]:


with st.container(border=True):

    st.subheader("Sanitair")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_sanitair = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=37)
    b_sanitair = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=38)


# #### Terreininrichting

# In[ ]:


with st.container(border=True):

    st.subheader("Terreininrichting")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_terreininrichting = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=39)
    b_terreininrichting = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=40)


# #### Trappen en hellingen

# In[ ]:


with st.container(border=True):

    st.subheader("Trappen en hellingen")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_trappen = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=41)
    b_trappen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=42)


# #### Verwarming en koeling

# In[ ]:


with st.container(border=True):

    st.subheader("Verwarming en koeling")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_verwarming = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=43)
    b_koeling = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=44)


# #### Vloerafwerkingen

# In[ ]:


with st.container(border=True):

    st.subheader("Vloerafwerkingen")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_vloerafwerking = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=45)
    b_vloerafwerking = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=46)


# #### Vloeren

# In[ ]:


with st.container(border=True):

    st.subheader("Vloeren")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_vloeren = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=47)
    b_vloeren = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=48)


# #### Warm- en koud water installaties

# In[ ]:


with st.container(border=True):

    st.subheader("Warm- en koud water installaties")
    st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

    v_water = st.slider('vul max en min te implementeren producten in',0, 20, (0, 2), key=49)
    b_water = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=50)

