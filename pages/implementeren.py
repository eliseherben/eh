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
    
def set_max_buitenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.max_buitenkozijnen = st.session_state._max_buitenkozijnen

with st.container(border=True):
    st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
     
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_buitenkozijnen", on_change=set_buitenkozijnen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_buitenkozijnen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_buitenkozijnen", on_change=set_max_buitenkozijnen)


# #### Lift

# In[ ]:


def set_lift():
    # Callback function to save the role selection to Session State
    st.session_state.lift = st.session_state._lift
    
def set_max_lift():
    # Callback function to save the role selection to Session State
    st.session_state.max_lift = st.session_state._max_lift

with st.container(border=True):
    st.subheader("Lift")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_lift = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_lift", on_change=set_lift)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_lift = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_lift", on_change=set_max_lift)


# #### Binnenkozijnen en deuren

# In[ ]:


def set_binnenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.binnenkozijnen = st.session_state._binnenkozijnen
    
def set_max_binnenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.max_binnenkozijnen = st.session_state._max_binnenkozijnen

with st.container(border=True):
    st.subheader("Binnenkozijnen en deuren")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenkozijnen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenkozijnen", on_change=set_binnenkozijnen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenkozijnen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_binnenkozijnen", on_change=set_max_binnenkozijnen)


# #### Binnenwandafwerkingen

# In[ ]:


def set_binnenwandafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwandafwerking = st.session_state._binnenwandafwerking
    
def set_max_binnenwandafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.max_binnenwandafwerking = st.session_state._max_binnenwandafwerking

with st.container(border=True):
    st.subheader("Binnenwandafwerkingen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwandafwerkingen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenwandafwerking", on_change=set_binnenwandafwerking)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenwandafwerkingen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_binnenwandafwerking", on_change=set_max_binnenwandafwerking)


# #### Vloerafwerkingen

# In[ ]:


def set_vloerafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.vloerafwerking = st.session_state._vloerafwerking
    
def set_max_vloerafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.max_vloerafwerking = st.session_state._max_vloerafwerking

with st.container(border=True):
    st.subheader("Vloerafwerkingen")
 
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloerafwerking = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_vloerafwerking", on_change=set_vloerafwerking)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_vloerafwerking = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_vloerafwerking", on_change=set_max_vloerafwerking)


# #### Plafonds

# In[ ]:


def set_plafonds():
    # Callback function to save the role selection to Session State
    st.session_state.plafonds = st.session_state._plafonds
    
def set_max_plafonds():
    # Callback function to save the role selection to Session State
    st.session_state.max_plafonds = st.session_state._max_plafonds

with st.container(border=True):
    st.subheader("Plafonds")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_plafonds = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_plafonds", on_change=set_plafonds)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_plafonds = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_plafonds", on_change=set_max_plafonds)


# #### Sanitair

# In[ ]:


def set_sanitair():
    # Callback function to save the role selection to Session State
    st.session_state.sanitair = st.session_state._sanitair
    
def set_max_sanitair():
    # Callback function to save the role selection to Session State
    st.session_state.max_sanitair = st.session_state._max_sanitair

with st.container(border=True):
    st.subheader("Sanitair")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_sanitair = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_sanitair", on_change=set_sanitair)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_sanitair = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_sanitair", on_change=set_max_sanitair)


# #### Keuken

# In[ ]:


def set_keuken():
    # Callback function to save the role selection to Session State
    st.session_state.keuken = st.session_state._keuken

def set_max_keuken():
    # Callback function to save the role selection to Session State
    st.session_state.max_keuken = st.session_state._max_keuken
    
with st.container(border=True):
    st.subheader("Keuken")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_keuken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_keuken", on_change=set_keuken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_keuken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_keuken", on_change=set_max_keuken)


# #### Buitenwanden

# In[ ]:


def set_buitenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.buitenwanden = st.session_state._buitenwanden
    
def set_max_buitenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.max_buitenwanden = st.session_state._max_buitenwanden

with st.container(border=True):
    st.subheader("Buitenwanden")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_buitenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_buitenwanden", on_change=set_buitenwanden)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_buitenwanden = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_buitenwanden", on_change=set_max_buitenwanden)


# #### Vloeren

# In[ ]:


def set_vloeren():
    # Callback function to save the role selection to Session State
    st.session_state.vloeren = st.session_state._vloeren
    
def set_max_vloeren():
    # Callback function to save the role selection to Session State
    st.session_state.max_vloeren = st.session_state._max_vloeren

with st.container(border=True):
    st.subheader("Vloeren")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_vloeren = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_vloeren", on_change=set_vloeren)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_vloeren = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_vloeren", on_change=set_max_vloeren)


# #### Daken

# In[ ]:


def set_daken():
    # Callback function to save the role selection to Session State
    st.session_state.daken = st.session_state._daken
    
def set_max_daken():
    # Callback function to save the role selection to Session State
    st.session_state.max_daken = st.session_state._max_daken

with st.container(border=True):
    st.subheader("Daken")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_daken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_daken", on_change=set_daken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_daken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_daken", on_change=set_max_daken)


# #### Hoofddraagconstructie

# In[ ]:


def set_hoofddraagconstructie():
    # Callback function to save the role selection to Session State
    st.session_state.hoofddraagconstructie = st.session_state._hoofddraagconstructie
    
def set_max_hoofddraagconstructie():
    # Callback function to save the role selection to Session State
    st.session_state.max_hoofddraagconstructie = st.session_state._max_hoofddraagconstructie

with st.container(border=True):
    st.subheader("Hoofddraagconstructie")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_hoofddraagconstructie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_hoofddraagconstructie", on_change=set_hoofddraagconstructie)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_hoofddraagconstructie = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_hoofddraagconstructie", on_change=set_max_hoofddraagconstructie)


# #### Na-isolatie binnen

# In[ ]:


def set_isolatie():
    # Callback function to save the role selection to Session State
    st.session_state.isolatie = st.session_state._isolatie
    
def set_max_isolatie():
    # Callback function to save the role selection to Session State
    st.session_state.max_isolatie = st.session_state._max_isolatie

with st.container(border=True):
    st.subheader("Na-isolatie binnen")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_isolatie = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_isolatie", on_change=set_isolatie)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_isolatie = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_isolatie", on_change=set_max_isolatie)


# #### Riolering en HWA

# In[ ]:


def set_riolering():
    # Callback function to save the role selection to Session State
    st.session_state.riolering = st.session_state._riolering
    
def set_max_riolering():
    # Callback function to save the role selection to Session State
    st.session_state.max_riolering = st.session_state._max_riolering

with st.container(border=True):
    st.subheader("Riolering en HWA")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_riolering = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_riolering", on_change=set_riolering)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_riolering = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_riolering", on_change=set_max_riolering)


# #### Terreininrichting

# In[ ]:


def set_terreininrichting():
    # Callback function to save the role selection to Session State
    st.session_state.terreininrichting = st.session_state._terreininrichting
    
def set_max_terreininrichting():
    # Callback function to save the role selection to Session State
    st.session_state.max_terreininrichting = st.session_state._max_terreininrichting

with st.container(border=True):
    st.subheader("Terreininrichting")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_terreininrichting = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_terreininrichting", on_change=set_terreininrichting)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_terreininrichting = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_terreininrichting", on_change=set_max_terreininrichting)


# #### Verwarming en koeling

# In[ ]:


def set_verwarming():
    # Callback function to save the role selection to Session State
    st.session_state.verwarming = st.session_state._verwarming
    
def set_max_verwarming():
    # Callback function to save the role selection to Session State
    st.session_state.max_verwarming = st.session_state._max_verwarming

with st.container(border=True):
    st.subheader("Verwarming en koeling")
 
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_koeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_verwarming", on_change=set_verwarming)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_verwarming = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_verwarming", on_change=set_max_verwarming)


# #### Luchtbehandeling

# In[ ]:


def set_luchtbehandeling():
    # Callback function to save the role selection to Session State
    st.session_state.luchtbehandeling = st.session_state._luchtbehandeling
    
def set_max_luchtbehandeling():
    # Callback function to save the role selection to Session State
    st.session_state.max_luchtbehandeling = st.session_state._max_luchtbehandeling

with st.container(border=True):
    st.subheader("Luchtbehandeling")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luchtbehandeling = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_luchtbehandeling", on_change=set_luchtbehandeling)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_luchtbehandeling = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_luchtbehandeling", on_change=set_max_luchtbehandeling)


# #### Vaste gebouwvoorzieningen

# In[ ]:


def set_gebouwvoorzieningen():
    # Callback function to save the role selection to Session State
    st.session_state.gebouwvoorzieningen = st.session_state._gebouwvoorzieningen
    
def set_max_gebouwvoorzieningen():
    # Callback function to save the role selection to Session State
    st.session_state.max_gebouwvoorzieningen = st.session_state._max_gebouwvoorzieningen

with st.container(border=True):
    st.subheader("Vaste gebouwvoorzieningen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_gebouwvoorzieningen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_gebouwvoorzieningen", on_change=set_gebouwvoorzieningen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_gebouwvoorzieningen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_gebouwvoorzieningen", on_change=set_max_gebouwvoorzieningen)


# #### Binnenwanden

# In[ ]:


def set_binnenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwanden = st.session_state._binnenwanden
    
def set_max_binnenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.max_binnenwanden = st.session_state._max_binnenwanden

with st.container(border=True):
    st.subheader("Binnenwanden")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_binnenwanden = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_binnenwanden", on_change=set_binnenwanden)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_binnenwanden = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_binnenwanden", on_change=set_max_binnenwanden)


# #### Trappen en hellingen

# In[ ]:


def set_trappen():
    # Callback function to save the role selection to Session State
    st.session_state.trappen = st.session_state._trappen
    
def set_max_trappen():
    # Callback function to save the role selection to Session State
    st.session_state.max_trappen = st.session_state._max_trappen

with st.container(border=True):
    st.subheader("Trappen en hellingen")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_trappen = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_trappen", on_change=set_trappen)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_trappen = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_trappen", on_change=set_max_trappen)


# #### Luiken en vensters

# In[ ]:


def set_luiken():
    # Callback function to save the role selection to Session State
    st.session_state.luiken = st.session_state._luiken
    
def set_max_luiken():
    # Callback function to save the role selection to Session State
    st.session_state.max_luiken = st.session_state._max_luiken

with st.container(border=True):
    st.subheader("Luiken en vensters")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_luiken = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_luiken", on_change=set_luiken)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_luiken = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_luiken", on_change=set_max_luiken)


# #### Balustrades en leuningen

# In[ ]:


def set_balustrades():
    # Callback function to save the role selection to Session State
    st.session_state.balustrades = st.session_state._balustrades
    
def set_max_balustrades():
    # Callback function to save the role selection to Session State
    st.session_state.max_balustrades = st.session_state._max_balustrades


with st.container(border=True):
    st.subheader("**Balustrades en leuningen**")
   
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_balustrades = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_balustrades", on_change=set_balustrades)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_balustrades = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_balustrades", on_change=set_max_balustrades)


# #### Warm- en koud water installaties

# In[ ]:


def set_water():
    # Callback function to save the role selection to Session State
    st.session_state.water = st.session_state._water
    
def set_max_water():
    # Callback function to save the role selection to Session State
    st.session_state.max_water = st.session_state._max_water

with st.container(border=True):
    st.subheader("Warm- en koud water installaties")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_water = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_water", on_change=set_water)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_water = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_water", on_change=set_max_water)


# #### Elektrische installaties

# In[ ]:


def set_elektra():
    # Callback function to save the role selection to Session State
    st.session_state.elektra = st.session_state._elektra
    
def set_max_elektra():
    # Callback function to save the role selection to Session State
    st.session_state.max_elektra = st.session_state._max_elektra

with st.container(border=True):
    st.subheader("Elektrische installaties")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_elektra = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_elektra", on_change=set_elektra)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_elektra = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_elektra", on_change=set_max_elektra)


# #### Beveiliging

# In[ ]:


def set_beveiliging():
    # Callback function to save the role selection to Session State
    st.session_state.beveiliging = st.session_state._beveiliging
    
def set_max_beveiliging():
    # Callback function to save the role selection to Session State
    st.session_state.max_beveiliging = st.session_state._max_beveiliging


with st.container(border=True):
    st.subheader("Beveiliging")
    
    st.markdown("**Hoe veel producten zijn er al geïmplementeerd in het project?**")
    b_beveiliging = st.number_input("Vul hoeveel producten er al geimplementeerd zijn in", min_value=0, key="_beveiliging", on_change=set_beveiliging)
    
    st.markdown("**Hoe veel producten kunnen er maximaal geïmplementeerd worden?**")
    st.markdown("Vul hieronder in hoeveel producten er maximaal in een productgroep geïmplementeerd kunnen worden.")
    max_beveiliging = st.slider("Vul een max voor het aantal te implementeren producten in", 0, 200, 100, key="_max_beveiliging", on_change=set_max_beveiliging)


# #### Optimalisatie

# In[ ]:


def set_optimalisatie():
    # Callback function to save the role selection to Session State
    st.session_state.optimalisatie = st.session_state._optimalisatie


# In[ ]:


with st.container(border = True):
    st.page_link("pages/2functies.py", label = "Klik hier om de optimalisatie te starten")

