#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu


# In[ ]:


productgroepen = ["buitenkozijnen", "lift", "binnenkozijnen", "binnenwandafwerkingen", "vloerafwerkingen", "plafonds", "sanitair", "keuken", "buitenwanden", "vloeren", "daken", "hoofddraagconstructie", "isolatie", "riolering", "terreininrichting", "verwarming", "luchtbehandeling", "gebouwvoorziening", "binnenwanden", "trappen", "luiken", "balustrades", "water", "elektra", "beveiliging"]


# In[ ]:


# # Lijst van sessievariabelen
# session_vars = [
#     "balustrades", "beveiliging", "binnenkozijnen", "binnenwandafwerking",
#     "binnenwanden", "buitenkozijnen", "buitenwanden", "daken", "elektra",
#     "gebouwvoorzieningen", "hoofddraagconstructie", "isolatie", "keuken",
#     "lift", "luchtbehandeling", "luiken", "plafonds", "riolering", "sanitair",
#     "terreininrichting", "trappen", "verwarming", "vloerafwerking", "vloeren",
#     "water", "budget", "project", "optimalisatie"
# ]

# # Loop door de sessievariabelen en initialiseer ze indien nodig
# for var_name in session_vars:
#     if var_name not in st.session_state:
#         st.session_state[var_name] = None

#     # Maak een koppeling met de 'private' versie met een underscore ervoor
#     st.session_state[f"_{var_name}"] = st.session_state[var_name]

# menu()


# #### algemene state sessions

# In[ ]:


if "project" not in st.session_state:
    st.session_state.project = None
    
st.session_state._project = st.session_state.project
    
if "optimalisatie" not in st.session_state:
    st.session_state.optimalisatie = None
    
st.session_state._optimalisatie = st.session_state.optimalisatie

if "budget" not in st.session_state:
    st.session_state.budget = None

st.session_state._budget = st.session_state.budget

menu()

# st.page_link("dashboard.py", label="Home")
# st.page_link("pages/buitenkozijnen.py", label="Buitenkozijnen, -ramen, -deuren en -puien")


# #### productgroepen state sessions

# In[ ]:


if "balustrades" not in st.session_state:
    st.session_state.balustrades = None

st.session_state._balustrades = st.session_state.balustrades

if "beveiliging" not in st.session_state:
    st.session_state.beveiliging = None

st.session_state._beveiliging = st.session_state.beveiliging

if "binnenkozijnen" not in st.session_state:
    st.session_state.binnenkozijnen = None

st.session_state._binnenkozijnen = st.session_state.binnenkozijnen

if "binnenwandafwerking" not in st.session_state:
    st.session_state.binnenwandafwerking = None

st.session_state._binnenwandafwerking = st.session_state.binnenwandafwerking

if "binnenwanden" not in st.session_state:
    st.session_state.binnenwanden = None

st.session_state._binnenwanden = st.session_state.binnenwanden

if "buitenkozijnen" not in st.session_state:
    st.session_state.buitenkozijnen = None

st.session_state._buitenkozijnen = st.session_state.buitenkozijnen

if "buitenwanden" not in st.session_state:
    st.session_state.buitenwanden = None

st.session_state._buitenwanden = st.session_state.buitenwanden

if "daken" not in st.session_state:
    st.session_state.daken = None

st.session_state._daken = st.session_state.daken

if "elektra" not in st.session_state:
    st.session_state.elektra = None

st.session_state._elektra = st.session_state.elektra

if "gebouwvoorzieningen" not in st.session_state:
    st.session_state.gebouwvoorzieningen = None

st.session_state._gebouwvoorzieningen = st.session_state.gebouwvoorzieningen

if "hoofddraagconstructie" not in st.session_state:
    st.session_state.hoofddraagconstructie = None

st.session_state._hoofddraagconstructie = st.session_state.hoofddraagconstructie

if "isolatie" not in st.session_state:
    st.session_state.isolatie = None

st.session_state._isolatie = st.session_state.isolatie

if "keuken" not in st.session_state:
    st.session_state.keuken = None

st.session_state._keuken = st.session_state.keuken

if "lift" not in st.session_state:
    st.session_state.lift = None

st.session_state._lift = st.session_state.lift

if "luchtbehandeling" not in st.session_state:
    st.session_state.luchtbehandeling = None

st.session_state._luchtbehandeling = st.session_state.luchtbehandeling

if "luiken" not in st.session_state:
    st.session_state.luiken = None

st.session_state._luiken = st.session_state.luiken

if "plafonds" not in st.session_state:
    st.session_state.plafonds = None

st.session_state._plafonds = st.session_state.plafonds

if "riolering" not in st.session_state:
    st.session_state.riolering = None

st.session_state._riolering = st.session_state.riolering

if "sanitair" not in st.session_state:
    st.session_state.sanitair = None

st.session_state._sanitair = st.session_state.sanitair

if "terreininrichting" not in st.session_state:
    st.session_state.terreininrichting = None

st.session_state._terreininrichting = st.session_state.terreininrichting

if "trappen" not in st.session_state:
    st.session_state.trappen = None

st.session_state._trappen = st.session_state.trappen

if "verwarming" not in st.session_state:
    st.session_state.verwarming = None

st.session_state._verwarming = st.session_state.verwarming

if "vloerafwerking" not in st.session_state:
    st.session_state.vloerafwerking = None

st.session_state._vloerafwerking = st.session_state.vloerafwerking

if "vloeren" not in st.session_state:
    st.session_state.vloeren = None

st.session_state._vloeren = st.session_state.vloeren

if "water" not in st.session_state:
    st.session_state.water = None

st.session_state._water = st.session_state.water


# #### themas state sessions

# In[ ]:


if "aanschafprijs" not in st.session_state:
    st.session_state.aanschafprijs = None

st.session_state._aanschafprijs = st.session_state.aanschafprijs

if "onderhoudsprijs" not in st.session_state:
    st.session_state.onderhoudsprijs = None

st.session_state._onderhoudsprijs = st.session_state.onderhoudsprijs

if "losmaakbaarheid" not in st.session_state:
    st.session_state.losmaakbaarheid = None

st.session_state._losmaakbaarheid = st.session_state.losmaakbaarheid

if "toepassingsmogelijkheden" not in st.session_state:
    st.session_state.toepassingsmogelijkheden = None

st.session_state._toepassingsmogelijkheden = st.session_state.toepassingsmogelijkheden

if "woonbeleving" not in st.session_state:
    st.session_state.woonbeleving = None

st.session_state._woonbeleving = st.session_state.woonbeleving

if "milieubelasting" not in st.session_state:
    st.session_state.milieubelasting = None

st.session_state._milieubelasting = st.session_state.milieubelasting

if "flexibiliteit" not in st.session_state:
    st.session_state.flexibiliteit = None

st.session_state._flexibiliteit = st.session_state.flexibiliteit

if "standaardisering" not in st.session_state:
    st.session_state.standaardisering = None

st.session_state._standaardisering = st.session_state.standaardisering


# In[1]:


# def set_session_var(var_name):
#     # Callback functie om de selectie op te slaan in de sessievariabele
#     st.session_state[var_name] = st.session_state[f"_{var_name}"]
    

# st.title("Projecten Eigen Haard")
# st.selectbox(
#     'Om wat voor soort project gaat het?',
#     ['Nieuwbouw woningen', 'Renovatie'], 
#     index=None,
#     placeholder="Selecteer een soort project",
#     key="_project", 
#     on_change=lambda: set_session_var("project"), 
# )


# if st.session_state.project is not None: 
#     with st.container(border=True):
#         st.subheader("**Budget**")
#         st.markdown("Vul het budget in voor het huidige project.")
#         st.number_input("Vul het budget in", value=None, placeholder="Typ een bedrag", key="_budget", on_change=lambda: set_session_var("budget"))


# In[ ]:


def set_project():
    # Callback function to save the role selection to Session State
    st.session_state.project = st.session_state._project
    
st.title("Projecten Eigen Haard")
st.selectbox(
    'Om wat voor soort project gaat het?',
    ['Nieuwbouw woningen', 'Renovatie'], 
    index=None,
    placeholder="Selecteer een soort project",
    key="_project", 
    on_change=set_project, 
)


# In[ ]:


def set_budget():
    # Callback function to save the role selection to Session State
    st.session_state.budget = st.session_state._budget

if st.session_state.project is not None: 
    with st.container(border=True):
        st.subheader("**Budget**")
        st.markdown("Vul het budget in voor het huidige project.")
        st.number_input("Vul het budget in", value=None, placeholder="Typ een bedrag", key="_budget", on_change=set_budget)



# In[ ]:


if st.session_state.project is not None:
    with st.container(border=True):
        st.subheader("**Weging onderdelen**")
        st.markdown("Hebben onderstaande onderdelen een zwaardere weging? De weging van de onderdelen staat standaard op 1. Als er onderdelen zijn die zwaarder wegen kunnen die hieronder aangepast worden.")

        st.markdown("**Aanschafprijs**")
        aanschafprijs = st.number_input("Weging", min_value=1, key="_aanschafprijs", on_change=set_aanschafprijs)

        st.markdown("**Onderhoudsprijs**")
        onderhoudsprijs = st.number_input("Weging", min_value=1, key="_onderhoudsprijs", on_change=set_onderhoudsprijs)

        st.markdown("**Mate van losmaakbaarheid**")
        losmaakbaarheid = st.number_input("Weging", min_value=1, key="_losmaakbaarheid", on_change=set_losmaakbaarheid)

        st.markdown("**Toepassingsmogelijkheden**")
        toepassingsmogelijkheden = st.number_input("Weging", min_value=1, key="_toepassingsmogelijkheden", on_change=set_toepassingsmogelijkheden)

        st.markdown("**Woonbeleving**")
        woonbeleving = st.number_input("Weging", min_value=1, key="_woonbeleving", on_change=set_woonbeleving)

        st.markdown("**Milieubelasting**")
        milieubelasting = st.number_input("Weging", min_value=1, key="_milieubelasting", on_change = set_milieubelasting)

        st.markdown("**Flexibiliteit tbv toekomstbestendigheid en innovatie**")
        flexibiliteit = st.number_input("Weging", min_value=1, key="_flexibiliteit", on_change = set_flexibiliteit)

        st.markdown("**Mate van standaardisering**")
        standaardisering = st.number_input("Weging", min_value=1, key="_standaardisering", on_change = set_standaardisering)


# In[ ]:


# if option2 == 'Begin fase':
#     col1, col2 = st.columns(2)
#     st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
   
    
# option2 = st.selectbox(
#     'In welke fase van het project zit je',
#     ('Begin fase', 'Midden'))



# In[ ]:


# if option2 == 'Begin fase':
#     col1, col2 = st.columns(2)
#     st.markdown("**wat is de range van producten die in een productgroep geïmplementeerd kunnen worden?**")
#     with col1:
#         v_buitenkozijnen = st.slider('Buitenkozijnen, -ramen, -deuren en -puien',0, 100, (2, 10))
#         v_lift = st.slider('Lift',0, 100, (2, 10))
#         v_binnenkozijnen = st.slider('Binnenkozijnen en deuren',0, 100, (2, 10))
#         v_binnenwandafwerking = st.slider('Binnenwandafwerkingen',0, 100, (2, 10))
#         v_vloerafwerking = st.slider('Vloerafwerkingen',0, 100, (2, 10))
#         v_plafonds = st.slider('Plafonds',0, 100,(2, 10))
#         v_sanitair = st.slider('Sanitair',0, 100, (2, 10))
#         v_keuken = st.slider('Keuken',0, 100, (2, 10))
#         v_buitenwanden = st.slider('Buitenwanden',0, 100, (2, 10))
#         v_vloeren = st.slider('Vloeren',0, 100, (2, 10))
#         v_daken = st.slider('Daken',0, 100, (2, 10))
#         v_hoofddraagconstructie = st.slider('Hoofddraagconstructie',0, 100, (2, 10))
#         v_isolatie = st.slider('Na-isolatie binnen',0, 100, (2, 10))
    
#     with col2:
#         v_riolering = st.slider('Riolering en HWA',0, 100, (2, 10))
#         v_terreininrichting = st.slider('Terreininrichting',0, 100, (2, 10))
#         v_verwarming = st.slider('Verwarming en koeling',0, 100, (2, 10))
#         v_luchtbehandeling = st.slider('Luchtbehandeling',0, 100, (2, 10))
#         v_gebouwvoorzieningen = st.slider('Vaste gebouwvoorzieningen',0, 100, (2, 10))
#         v_binnenwanden = st.slider('Binnenwanden',0, 100, (2, 10))
#         v_trappen = st.slider('Trappen en hellingen',0, 100, (2, 10))
#         v_luiken = st.slider('Luiken en vensters',0, 100, (2, 10))
#         v_balustrades = st.slider('Balustrades en leuningen',0, 100, (2, 10))
#         v_water = st.slider('Warm- en koud water installaties',0, 100, (2, 10))
#         v_elektra = st.slider('Elektrische installaties',0, 100, (2, 10))
#         v_beveiliging = st.slider('Beveiliging',0, 100, (2, 10))


# In[ ]:


# if option2 == 'Midden':
    
#     st.markdown("**Op welke productgroepen kan niet bespaard worden?**")
#     with st.container(border=True):
#         col3, col4 = st.columns(2)

#         with col3:
#             buitenkozijnen = st.checkbox('Buitenkozijnen, -ramen, -deuren en -puien')
#             lift = st.checkbox('Lift')
#             binnenkozijnen = st.checkbox('Binnenkozijnen en deuren')
#             binnenwandafwerkingen = st.checkbox('Binnenwandafwerkingen')
#             vloerafwerkingen = st.checkbox('Vloerafwerkingen')
#             plafonds = st.checkbox('Plafonds')
#             sanitair = st.checkbox('Sanitair')
#             keuken = st.checkbox('Keuken')
#             buitenwanden = st.checkbox('Buitenwanden')
#             vloeren = st.checkbox('Vloeren')
#             daken = st.checkbox('Daken')
#             hoofddraagconstructie = st.checkbox('Hoofddraagconstructie')
#             isolatie = st.checkbox('Na-isolatie binnen')

#         with col4:
#             riolering = st.checkbox('Riolering en HWA')
#             terreininrichting = st.checkbox('Terreininrichting')
#             verwarming = st.checkbox('Verwarming en koeling')
#             luchtbehandeling = st.checkbox('Luchtbehandeling')
#             gebouwvoorzieningen = st.checkbox('Vaste gebouwvoorzieningen')
#             binnenwanden = st.checkbox('Binnenwanden')
#             trappen = st.checkbox('Trappen en hellingen')
#             luiken = st.checkbox('Luiken en vensters')
#             balustrades = st.checkbox('Balustrades en leuningen')
#             water = st.checkbox('Warm- en koud water installaties')
#             elektra = st.checkbox('Elektrische installaties')
#             beveiliging = st.checkbox('Beveiliging')

#     st.markdown("**Het aantal producten per productgroep wat momenteel geimplementeerd is in het project:**")
#     with st.container(border=True):     
#         col5, col6 = st.columns(2)
#         with col5:
#             n_buitenkozijnen = st.number_input("Buitenkozijnen, -ramen, -deuren en -puien", min_value=0)
#             n_lift = st.number_input("Lift", min_value=0)
#             n_binnenkozijnen = st.number_input("Binnenkozijnen en deuren", min_value=0)
#             n_binnenwandafwerkingen = st.number_input("Binnenwandafwerkingen", min_value=0)
#             n_vloerafwerkingen = st.number_input("Vloerafwerkingen", min_value=0)
#             n_plafonds = st.number_input("Plafonds", min_value=0)
#             n_sanitair = st.number_input("Sanitair", min_value=0)
#             n_keuken = st.number_input("Keuken", min_value=0)
#             n_buitenwanden = st.number_input("Buitenwanden", min_value=0)
#             n_vloeren = st.number_input("Vloeren", min_value=0)
#             n_daken = st.number_input("Daken", min_value=0)
#             n_hoofddraagconstructie = st.number_input("Hoofddraagconstructie", min_value=0)
#             n_isolatie = st.number_input("Na-isolatie binnen", min_value=0)

#         with col6:
#             n_riolering = st.number_input("Riolering en HWA", min_value=0)
#             n_terreininrichting = st.number_input("Terreininrichting", min_value=0)
#             n_verwarming = st.number_input("Verwarming en koeling", min_value=0)
#             n_luchtbehandeling = st.number_input("Luchtbehandeling", min_value=0)
#             n_gebouwvoorzieningen = st.number_input("Vaste gebouwvoorzieningen", min_value=0)
#             n_binnenwanden = st.number_input("Binnenwanden", min_value=0)
#             n_trappen = st.number_input("Trappen en hellingen", min_value=0)
#             n_luiken = st.number_input("Luiken en vensters", min_value=0)
#             n_balustrades = st.number_input("Balustrades en leuningen", min_value=0)
#             n_water = st.number_input("Warm- en koud water installaties", min_value=0)
#             n_elektra = st.number_input("Elektrische installaties", min_value=0)
#             n_beveiliging = st.number_input("Beveiliging", min_value=0)


