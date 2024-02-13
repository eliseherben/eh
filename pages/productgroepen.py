#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu_with_redirect


# In[ ]:


menu_with_redirect()


# In[ ]:


st.title("Projecten Eigen Haard")
st.markdown("Hieronder zijn de verschillende productgroepen weergegeven. Bij elke productgroep dient er aangegeven te worden hoeveel producten er binnen die productgroep geïmplementeerd kunenn worden en hoeveel er al geïmplementeerd zijn in het project. ")


# #### Balustrades en leuningen

# In[ ]:


with st.container(border=True):
    st.subheader("**Balustrades en leuningen**")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_balustrades = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=1)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_balustrades = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=2)


# #### Beveiliging

# In[ ]:


with st.container(border=True):
    st.subheader("Beveiliging")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_beveiliging = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=3)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_beveiliging = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=4)


# #### Binnenkozijnen en deuren

# In[ ]:


with st.container(border=True):
    st.subheader("Binnenkozijnen en deuren")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenkozijnen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=5)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=6)


# #### Binnenwandafwerkingen

# In[ ]:


with st.container(border=True):
    st.subheader("Binnenwandafwerkingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenwandafwerkingen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=7)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwandafwerkingen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=8)


# #### Binnenwanden

# In[ ]:


with st.container(border=True):

    st.subheader("Binnenwanden")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenwanden = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=9)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=10)


# #### Buitenkozijnen, -ramen, -deuren en -puien

# In[ ]:


with st.container(border=True):

    st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_buitenkozijnen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=11)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=12)


# #### Buitenwanden

# In[ ]:


with st.container(border=True):

    st.subheader("Buitenwanden")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_buitenwanden = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=13)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=14)


# #### Daken

# In[ ]:


with st.container(border=True):

    st.subheader("Daken")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_daken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=15)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_daken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=16)


# #### Elektrische installaties

# In[ ]:


with st.container(border=True):

    st.subheader("Elektrische installaties")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_elektra = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=17)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_elektra = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=18)


# #### Vaste gebouwvoorzieningen

# In[ ]:


with st.container(border=True):

    st.subheader("Vaste gebouwvoorzieningen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_gebouwvoorzieningen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=19)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_gebouwvoorzieningen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=20)


# #### Hoofddraagconstructie

# In[ ]:


with st.container(border=True):

    st.subheader("Hoofddraagconstructie")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_hoofddraagconstructie = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=21)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_hoofddraagconstructie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=22)


# #### Na-isolatie binnen

# In[ ]:


with st.container(border=True):

    st.subheader("Na-isolatie binnen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_isolatie = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=23)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_isolatie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=24)


# #### Keuken

# In[ ]:


with st.container(border=True):

    st.subheader("Keuken")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_keuken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=25)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_keuken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=26)


# #### Lift

# In[ ]:


with st.container(border=True):

    st.subheader("Lift")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_lift = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=27)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_lift = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=28)


# #### Luchtbehandeling

# In[ ]:


with st.container(border=True):

    st.subheader("Luchtbehandeling")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_luchtbehandeling = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=29)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luchtbehandeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=30)


# #### Luiken en vensters

# In[ ]:


with st.container(border=True):

    st.subheader("Luiken en vensters")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_luiken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=31)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luiken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=32)


# #### Plafonds

# In[ ]:


with st.container(border=True):

    st.subheader("Plafonds")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_plafonds = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=33)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_plafonds = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=34)


# #### Riolering en HWA

# In[ ]:


with st.container(border=True):

    st.subheader("Riolering en HWA")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_riolering = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=35)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_riolering = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=36)


# #### Sanitair

# In[ ]:


with st.container(border=True):

    st.subheader("Sanitair")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_sanitair = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=37)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_sanitair = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=38)


# #### Terreininrichting

# In[ ]:


with st.container(border=True):

    st.subheader("Terreininrichting")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_terreininrichting = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=39)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_terreininrichting = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=40)


# #### Trappen en hellingen

# In[ ]:


with st.container(border=True):

    st.subheader("Trappen en hellingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_trappen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=41)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_trappen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=42)


# #### Verwarming en koeling

# In[ ]:


with st.container(border=True):

    st.subheader("Verwarming en koeling")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_verwarming = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=43)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_koeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=44)


# #### Vloerafwerkingen

# In[ ]:


with st.container(border=True):

    st.subheader("Vloerafwerkingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_vloerafwerking = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=45)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloerafwerking = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=46)


# #### Vloeren

# In[ ]:


with st.container(border=True):

    st.subheader("Vloeren")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_vloeren = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=47)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloeren = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=48)


# #### Warm- en koud water installaties

# In[ ]:


with st.container(border=True):

    st.subheader("Warm- en koud water installaties")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_water = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key=49)
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_water = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key=50)


# #### Optimalisatie

# In[ ]:


if "optimalisatie" not in st.session_state:
    st.session_state.optimalisatie = None
    
st.session_state._optimalisatie = st.session_state.optimalisatie

def set_optimalisatie():
    # Callback function to save the role selection to Session State
    st.session_state.optimalisatie = st.session_state._optimalisatie

st.button("Klik hier om de optimalisatie te starten", key="_project", on_change=set_project)


# In[ ]:


with st.container(border = True):
    st.page_link("pages/optimalisatie.py", label = "Klik hier om de optimalisatie te starten")

