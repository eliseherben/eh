#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect


# #### Balustrades en leuningen

# In[ ]:


menu_with_redirect()

st.subheader("Balustrades en leuningen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_balustrades = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_balustrades = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Beveiliging

# In[ ]:


menu_with_redirect()

st.subheader("Beveiliging")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_beveiliging = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_beveiliging = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Binnenkozijnen en deuren

# In[ ]:


menu_with_redirect()

st.subheader("Binnenkozijnen en deuren")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_binnenkozijnen = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_binnenkozijnen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Binnenwandafwerkingen

# In[ ]:


menu_with_redirect()

st.subheader("Binnenwandafwerkingen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_binnenwandafwerkingen = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_binnenwandafwerkingen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Binnenwanden

# In[ ]:


menu_with_redirect()

st.subheader("Binnenwanden")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_binnenwanden = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_binnenwanden = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Buitenkozijnen, -ramen, -deuren en -puien

# In[ ]:


menu_with_redirect()

st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_buitenkozijnen = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_buitenkozijnen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Buitenwanden

# In[ ]:


menu_with_redirect()

st.subheader("Buitenwanden")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_buitenwanden = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_buitenwanden = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Daken

# In[ ]:


menu_with_redirect()

st.subheader("Daken")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_daken = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_daken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Elektrische installaties

# In[ ]:


menu_with_redirect()

st.subheader("Elektrische installaties")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_elektra = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_elektra = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Vaste gebouwvoorzieningen

# In[ ]:


menu_with_redirect()

st.subheader("Vaste gebouwvoorzieningen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_gebouwvoorzieningen = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_gebouwvoorzieningen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Hoofddraagconstructie

# In[ ]:


menu_with_redirect()

st.subheader("Hoofddraagconstructie")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_hoofddraagconstructie = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_hoofddraagconstructie = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Na-isolatie binnen

# In[ ]:


menu_with_redirect()

st.subheader("Na-isolatie binnen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_isolatie = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_isolatie = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Keuken

# In[ ]:


menu_with_redirect()

st.subheader("Keuken")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_keuken = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_keuken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Lift

# In[ ]:


menu_with_redirect()

st.subheader("Lift")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_lift = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_lift = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Luchtbehandeling

# In[ ]:


menu_with_redirect()

st.subheader("Luchtbehandeling")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_luchtbehandeling = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_luchtbehandeling = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Luiken en vensters

# In[ ]:


menu_with_redirect()

st.subheader("Luiken en vensters")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_luiken = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_luiken = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Plafonds

# In[ ]:


menu_with_redirect()

st.subheader("Plafonds")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_plafonds = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_plafonds = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Riolering en HWA

# In[ ]:


menu_with_redirect()

st.subheader("Riolering en HWA")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_riolering = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_riolering = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Sanitair

# In[ ]:


menu_with_redirect()

st.subheader("Sanitair")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_sanitair = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_sanitair = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Terreininrichting

# In[ ]:


menu_with_redirect()

st.subheader("Terreininrichting")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_terreininrichting = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_terreininrichting = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Trappen en hellingen

# In[ ]:


menu_with_redirect()

st.subheader("Trappen en hellingen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_trappen = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_trappen = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Verwarming en koeling

# In[ ]:


menu_with_redirect()

st.subheader("Verwarming en koeling")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_verwarming = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_koeling = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Vloerafwerkingen

# In[ ]:


menu_with_redirect()

st.subheader("Vloerafwerkingen")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_vloerafwerking = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_vloerafwerking = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Vloeren

# In[ ]:


menu_with_redirect()

st.subheader("Vloeren")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_vloeren = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_vloeren = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)


# #### Warm- en koud water installaties

# In[ ]:


menu_with_redirect()

st.subheader("Warm- en koud water installaties")
st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")

v_water = st.slider('vul max en min te implementeren producten in',0, 100, (2, 10))
b_water = st.number_input("vul hoeveel producten er al geimplementeerd zijn in", min_value=0)

