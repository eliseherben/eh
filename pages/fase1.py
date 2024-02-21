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

def set_min_max_buitenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_buitenkozijnen = st.session_state._min_max_buitenkozijnen
    
with st.container(border=True):
    st.subheader("Buitenkozijnen, -ramen, -deuren en -puien")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_buitenkozijnen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_buitenkozijnen", on_change=set_min_max_buitenkozijnen)


# #### Lift

# In[ ]:


def set_lift():
    # Callback function to save the role selection to Session State
    st.session_state.lift = st.session_state._lift
    
def set_min_max_lift():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_lift = st.session_state._min_max_lift

with st.container(border=True):
    st.subheader("Lift")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_lift = st.slider('Vul max en min te implementeren producten in',0 , 20, (0, 20), key="_min_max_lift", on_change=set_min_max_lift)


# #### Binnenkozijnen en deuren

# In[ ]:


def set_binnenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.binnenkozijnen = st.session_state._binnenkozijnen
    
def set_min_max_binnenkozijnen():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_binnenkozijnen = st.session_state._min_max_binnenkozijnen

with st.container(border=True):
    st.subheader("Binnenkozijnen en deuren")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenkozijnen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_binnenkozijnen", on_change=set_min_max_binnenkozijnen)


# #### Binnenwandafwerkingen

# In[ ]:


def set_binnenwandafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwandafwerking = st.session_state._binnenwandafwerking
    
def set_min_max_binnenwandafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_binnenwandafwerking = st.session_state._min_max_binnenwandafwerking

with st.container(border=True):
    st.subheader("Binnenwandafwerkingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenwandafwerkingen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_binnenwandafwerking", on_change=set_min_max_binnenwandafwerking)


# #### Vloerafwerkingen

# In[ ]:


def set_vloerafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.vloerafwerking = st.session_state._vloerafwerking
    
def set_min_max_vloerafwerking():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_vloerafwerking = st.session_state._min_max_vloerafwerking

with st.container(border=True):
    st.subheader("Vloerafwerkingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_vloerafwerking = st.slider('Vul max en min te implementeren producten in', 0, 20, (0, 20), key="_min_max_vloerafwerking", on_change=set_min_max_vloerafwerking)


# #### Plafonds

# In[ ]:


def set_plafonds():
    # Callback function to save the role selection to Session State
    st.session_state.plafonds = st.session_state._plafonds
    
def set_min_max_plafonds():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_plafonds = st.session_state._min_max_plafonds

with st.container(border=True):
    st.subheader("Plafonds")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_plafonds = st.slider('Vul max en min te implementeren producten in', 0, 20, (0, 20), key="_min_max_plafonds", on_change=set_min_max_plafonds)


# #### Sanitair

# In[ ]:


def set_sanitair():
    # Callback function to save the role selection to Session State
    st.session_state.sanitair = st.session_state._sanitair
    
def set_min_max_sanitair():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_sanitair = st.session_state._min_max_sanitair

with st.container(border=True):
    st.subheader("Sanitair")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_sanitair = st.slider('Vul max en min te implementeren producten in', 0, 20, (0, 20), key="_min_max_sanitair", on_change=set_min_max_sanitair)


# #### Keuken

# In[ ]:


def set_keuken():
    # Callback function to save the role selection to Session State
    st.session_state.keuken = st.session_state._keuken
    
def set_min_max_keuken():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_keuken = st.session_state._min_max_keuken

with st.container(border=True):
    st.subheader("Keuken")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_keuken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_keuken", on_change=set_min_max_keuken)


# #### Buitenwanden

# In[ ]:


def set_buitenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.buitenwanden = st.session_state._buitenwanden
    
def set_min_max_buitenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_buitenwanden = st.session_state._min_max_buitenwanden

with st.container(border=True):
    st.subheader("Buitenwanden")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_buitenwanden = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_buitenwanden", on_change=set_min_max_buitenwanden)


# #### Vloeren

# In[ ]:


def set_vloeren():
    # Callback function to save the role selection to Session State
    st.session_state.vloeren = st.session_state._vloeren
    
def set_min_max_vloeren():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_vloeren = st.session_state._min_max_vloeren

with st.container(border=True):
    st.subheader("Vloeren")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_vloeren = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_vloeren", on_change=set_min_max_vloeren)


# #### Daken

# In[ ]:


def set_daken():
    # Callback function to save the role selection to Session State
    st.session_state.daken = st.session_state._daken
    
def set_min_max_daken():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_daken = st.session_state._min_max_daken

with st.container(border=True):
    st.subheader("Daken")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_daken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_daken", on_change=set_min_max_daken)


# #### Hoofddraagconstructie

# In[ ]:


def set_hoofddraagconstructie():
    # Callback function to save the role selection to Session State
    st.session_state.hoofddraagconstructie = st.session_state._hoofddraagconstructie
    
def set_min_max_hoofddraagconstructie():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_hoofddraagconstructie = st.session_state._min_max_hoofddraagconstructie

with st.container(border=True):
    st.subheader("Hoofddraagconstructie")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_hoofddraagconstructie = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_hoofddraagconstructie", on_change=set_min_max_hoofddraagconstructie)


# #### Na-isolatie binnen

# In[ ]:


def set_isolatie():
    # Callback function to save the role selection to Session State
    st.session_state.isolatie = st.session_state._isolatie

def set_min_max_isolatie():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_isolatie = st.session_state._min_max_isolatie
    
with st.container(border=True):
    st.subheader("Na-isolatie binnen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_isolatie = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_isolatie", on_change=set_min_max_isolatie)


# #### Riolering en HWA

# In[ ]:


def set_riolering():
    # Callback function to save the role selection to Session State
    st.session_state.riolering = st.session_state._riolering
    
def set_min_max_riolering():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_riolering = st.session_state._min_max_riolering

with st.container(border=True):
    st.subheader("Riolering en HWA")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_riolering = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_riolering", on_change=set_min_max_riolering)


# #### Terreininrichting

# In[ ]:


def set_terreininrichting():
    # Callback function to save the role selection to Session State
    st.session_state.terreininrichting = st.session_state._terreininrichting
    
def set_min_max_terreininrichting():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_terreininrichting = st.session_state._min_max_terreininrichting

with st.container(border=True):
    st.subheader("Terreininrichting")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_terreininrichting = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_terreininrichting", on_change=set_min_max_terreininrichting)


# #### Verwarming en koeling

# In[ ]:


def set_verwarming():
    # Callback function to save the role selection to Session State
    st.session_state.verwarming = st.session_state._verwarming
    
def set_min_max_verwarming():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_verwarming = st.session_state._min_max_verwarming

with st.container(border=True):
    st.subheader("Verwarming en koeling")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_verwarming = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_verwarming", on_change=set_min_max_verwarming)


# #### Luchtbehandeling

# In[ ]:


def set_luchtbehandeling():
    # Callback function to save the role selection to Session State
    st.session_state.luchtbehandeling = st.session_state._luchtbehandeling

def set_min_max_luchtbehandeling():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_luchtbehandeling = st.session_state._min_max_luchtbehandeling
    
with st.container(border=True):
    st.subheader("Luchtbehandeling")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_luchtbehandeling = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_luchtbehandeling", on_change=set_min_max_luchtbehandeling)


# #### Vaste gebouwvoorzieningen

# In[ ]:


def set_gebouwvoorzieningen():
    # Callback function to save the role selection to Session State
    st.session_state.gebouwvoorzieningen = st.session_state._gebouwvoorzieningen
    
def set_min_max_gebouwvoorzieningen():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_gebouwvoorzieningen = st.session_state._min_max_gebouwvoorzieningen

with st.container(border=True):
    st.subheader("Vaste gebouwvoorzieningen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_gebouwvoorzieningen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_gebouwvoorzieningen", on_change=set_min_max_gebouwvoorzieningen)


# #### Binnenwanden

# In[ ]:


def set_binnenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.binnenwanden = st.session_state._binnenwanden
    
def set_min_max_binnenwanden():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_binnenwanden = st.session_state._min_max_binnenwanden

with st.container(border=True):
    st.subheader("Binnenwanden")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_binnenwanden = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_binnenwanden", on_change=set_min_max_binnenwanden)


# #### Trappen en hellingen

# In[ ]:


def set_trappen():
    # Callback function to save the role selection to Session State
    st.session_state.trappen = st.session_state._trappen
    
def set_min_max_trappen():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_trappen = st.session_state._min_max_trappen

with st.container(border=True):
    st.subheader("Trappen en hellingen")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_trappen = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_trappen", on_change=set_min_max_trappen)


# #### Luiken en vensters

# In[ ]:


def set_luiken():
    # Callback function to save the role selection to Session State
    st.session_state.luiken = st.session_state._luiken
    
def set_min_max_luiken():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_luiken = st.session_state._min_max_luiken

with st.container(border=True):
    st.subheader("Luiken en vensters")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_luiken = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_luiken", on_change=set_min_max_luiken)


# #### Balustrades en leuningen

# In[ ]:


def set_balustrades():
    # Callback function to save the role selection to Session State
    st.session_state.balustrades = st.session_state._balustrades

def set_min_max_balustrades():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_balustrades = st.session_state._min_max_balustrades

with st.container(border=True):
    st.subheader("**Balustrades en leuningen**")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_balustrades = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_balustrades", on_change=set_min_max_balustrades)


# #### Warm- en koud water installaties

# In[ ]:


def set_water():
    # Callback function to save the role selection to Session State
    st.session_state.water = st.session_state._water
    
def set_min_max_water():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_water = st.session_state._min_max_water

with st.container(border=True):
    st.subheader("Warm- en koud water installaties")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_water = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_water", on_change=set_min_max_water)


# #### Elektrische installaties

# In[ ]:


def set_elektra():
    # Callback function to save the role selection to Session State
    st.session_state.elektra = st.session_state._elektra
    
def set_min_max_elektra():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_elektra = st.session_state._min_max_elektra

with st.container(border=True):
    st.subheader("Elektrische installaties")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_elektra = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_elektra", on_change=set_min_max_elektra)


# #### Beveiliging

# In[ ]:


def set_beveiliging():
    # Callback function to save the role selection to Session State
    st.session_state.beveiliging = st.session_state._beveiliging

def set_min_max_beveiliging():
    # Callback function to save the role selection to Session State
    st.session_state.min_max_beveiliging = st.session_state._min_max_beveiliging
    
with st.container(border=True):
    st.subheader("Beveiliging")
    st.markdown("**Wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
    st.markdown("Vul hieronder in hoeveel producten er in een productgroep geïmplementeerd kunnen worden. Hierbij kan er een maximum en minimum aangegeven worden.")
    v_beveiliging = st.slider('Vul max en min te implementeren producten in',0, 20, (0, 20), key="_min_max_beveiliging", on_change=set_min_max_beveiliging)


# #### Optimalisatie

# In[ ]:


def set_optimalisatie():
    # Callback function to save the role selection to Session State
    st.session_state.optimalisatie = st.session_state._optimalisatie


# In[ ]:


with st.container(border = True):
    st.page_link("pages/optimalisatie.py", label = "Klik hier om de optimalisatie te starten")

