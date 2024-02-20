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


# #### Buitenkozijnen, -ramen, -deuren en -puien

# In[ ]:


def set_buitenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.buitenkozijnen = st.session_state._buitenkozijnen

with st.container(border=True):
    st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
     
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_buitenkozijnen", on_change=set_buitenkozijnen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_buitenkozijnen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbuitenkozijnen")


# #### Lift

# In[ ]:


def set_lift():
    # Callback function to save the role selection to Session State
    st.session_state.lift = st.session_state._lift

with st.container(border=True):
    st.subheader("Lift")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_lift = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_lift", on_change=set_lift)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_lift = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxlift")


# #### Binnenkozijnen en deuren

# In[ ]:


def set_binnenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.binnenkozijnen = st.session_state._binnenkozijnen

with st.container(border=True):
    st.subheader("Binnenkozijnen en deuren")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenkozijnen", on_change=set_binnenkozijnen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenkozijnen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbinnenkozijnen")


# #### Binnenwandafwerkingen

# In[ ]:


def set_binnenwandafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwandafwerking = st.session_state._binnenwandafwerking

with st.container(border=True):
    st.subheader("Binnenwandafwerkingen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwandafwerkingen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenwandafwerking", on_change=set_binnenwandafwerking)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenwandafwerkingen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbinnenwandafwerking")


# #### Vloerafwerkingen

# In[ ]:


def set_vloerafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.vloerafwerking = st.session_state._vloerafwerking

with st.container(border=True):
    st.subheader("Vloerafwerkingen")
 
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloerafwerking = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_vloerafwerking", on_change=set_vloerafwerking)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_vloerafwerking = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbvloerafwerking")


# #### Plafonds

# In[ ]:


def set_plafonds():
    # Callback function to save the role selection to Session State
    st.session_state.plafonds = st.session_state._plafonds

with st.container(border=True):
    st.subheader("Plafonds")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_plafonds = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_plafonds", on_change=set_plafonds)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_plafonds = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxplafonds")


# #### Sanitair

# In[ ]:


def set_sanitair():
    # Callback function to save the role selection to Session State
    st.session_state.sanitair = st.session_state._sanitair

with st.container(border=True):
    st.subheader("Sanitair")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_sanitair = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_sanitair", on_change=set_sanitair)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_sanitair = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxsanitair")


# #### Keuken

# In[ ]:


def set_keuken():
    # Callback function to save the role selection to Session State
    st.session_state.keuken = st.session_state._keuken

with st.container(border=True):
    st.subheader("Keuken")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_keuken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_keuken", on_change=set_keuken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_keuken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxkeuken")


# #### Buitenwanden

# In[ ]:


def set_buitenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.buitenwanden = st.session_state._buitenwanden

with st.container(border=True):
    st.subheader("Buitenwanden")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_buitenwanden", on_change=set_buitenwanden)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_buitenwanden = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbuitenwanden")


# #### Vloeren

# In[ ]:


def set_vloeren():
    # Callback function to save the role selection to Session State
    st.session_state.vloeren = st.session_state._vloeren

with st.container(border=True):
    st.subheader("Vloeren")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloeren = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_vloeren", on_change=set_vloeren)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_vloeren = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxvloeren")


# #### Daken

# In[ ]:


def set_daken():
    # Callback function to save the role selection to Session State
    st.session_state.daken = st.session_state._daken

with st.container(border=True):
    st.subheader("Daken")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_daken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_daken", on_change=set_daken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_daken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxdaken")


# #### Hoofddraagconstructie

# In[ ]:


def set_hoofddraagconstructie():
    # Callback function to save the role selection to Session State
    st.session_state.hoofddraagconstructie = st.session_state._hoofddraagconstructie

with st.container(border=True):
    st.subheader("Hoofddraagconstructie")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_hoofddraagconstructie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_hoofddraagconstructie", on_change=set_hoofddraagconstructie)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_hoofddraagconstructie = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxhoofddraagconstructie")


# #### Na-isolatie binnen

# In[ ]:


def set_isolatie():
    # Callback function to save the role selection to Session State
    st.session_state.isolatie = st.session_state._isolatie

with st.container(border=True):
    st.subheader("Na-isolatie binnen")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_isolatie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_isolatie", on_change=set_isolatie)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_isolatie = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxisolatie")


# #### Riolering en HWA

# In[ ]:


def set_riolering():
    # Callback function to save the role selection to Session State
    st.session_state.riolering = st.session_state._riolering

with st.container(border=True):
    st.subheader("Riolering en HWA")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_riolering = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_riolering", on_change=set_riolering)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_riolering = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxriolering")


# #### Terreininrichting

# In[ ]:


def set_terreininrichting():
    # Callback function to save the role selection to Session State
    st.session_state.terreininrichting = st.session_state._terreininrichting

with st.container(border=True):
    st.subheader("Terreininrichting")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_terreininrichting = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_terreininrichting", on_change=set_terreininrichting)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_terreininrichting = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxterreininrichting")


# #### Verwarming en koeling

# In[ ]:


def set_verwarming():
    # Callback function to save the role selection to Session State
    st.session_state.verwarming = st.session_state._verwarming

with st.container(border=True):
    st.subheader("Verwarming en koeling")
 
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_koeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_verwarming", on_change=set_verwarming)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_verwarming = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxverwarming")


# #### Luchtbehandeling

# In[ ]:


def set_luchtbehandeling():
    # Callback function to save the role selection to Session State
    st.session_state.luchtbehandeling = st.session_state._luchtbehandeling

with st.container(border=True):
    st.subheader("Luchtbehandeling")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luchtbehandeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_luchtbehandeling", on_change=set_luchtbehandeling)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_luchtbehandeling = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxluchtbehandeling")


# #### Vaste gebouwvoorzieningen

# In[ ]:


def set_gebouwvoorzieningen():
    # Callback function to save the role selection to Session State
    st.session_state.gebouwvoorzieningen = st.session_state._gebouwvoorzieningen

with st.container(border=True):
    st.subheader("Vaste gebouwvoorzieningen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_gebouwvoorzieningen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_gebouwvoorzieningen", on_change=set_gebouwvoorzieningen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_gebouwvoorzieningen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxgebouwvoorzieningen")


# #### Binnenwanden

# In[ ]:


def set_binnenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwanden = st.session_state._binnenwanden

with st.container(border=True):
    st.subheader("Binnenwanden")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenwanden", on_change=set_binnenwanden)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenwanden = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbinnenwanden")


# #### Trappen en hellingen

# In[ ]:


def set_trappen():
    # Callback function to save the role selection to Session State
    st.session_state.trappen = st.session_state._trappen

with st.container(border=True):
    st.subheader("Trappen en hellingen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_trappen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_trappen", on_change=set_trappen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_trappen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxtrappen")


# #### Luiken en vensters

# In[ ]:


def set_luiken():
    # Callback function to save the role selection to Session State
    st.session_state.luiken = st.session_state._luiken

with st.container(border=True):
    st.subheader("Luiken en vensters")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luiken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_luiken", on_change=set_luiken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_luiken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxluiken")


# #### Balustrades en leuningen

# In[ ]:


def set_balustrades():
    # Callback function to save the role selection to Session State
    st.session_state.balustrades = st.session_state._balustrades


with st.container(border=True):
    st.subheader("**Balustrades en leuningen**")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_balustrades = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_balustrades", on_change=set_balustrades)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_balustrades = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbalustrades")


# #### Warm- en koud water installaties

# In[ ]:


def set_water():
    # Callback function to save the role selection to Session State
    st.session_state.water = st.session_state._water

with st.container(border=True):
    st.subheader("Warm- en koud water installaties")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_water = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_water", on_change=set_water)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_water = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxwater")


# #### Elektrische installaties

# In[ ]:


def set_elektra():
    # Callback function to save the role selection to Session State
    st.session_state.elektra = st.session_state._elektra

with st.container(border=True):
    st.subheader("Elektrische installaties")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_elektra = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_elektra", on_change=set_elektra)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_elektra = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxelektra")


# #### Beveiliging

# In[ ]:


def set_beveiliging():
    # Callback function to save the role selection to Session State
    st.session_state.beveiliging = st.session_state._beveiliging


with st.container(border=True):
    st.subheader("Beveiliging")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_beveiliging = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_beveiliging", on_change=set_beveiliging)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_beveiliging = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 20, 10, key="_maxbeveiliging")


# #### Optimalisatie

# In[ ]:


def set_optimalisatie():
    # Callback function to save the role selection to Session State
    st.session_state.optimalisatie = st.session_state._optimalisatie


# In[ ]:


with st.container(border = True):
    st.page_link("pages/optimalisatie.py", label = "Klik hier om de optimalisatie te starten")
