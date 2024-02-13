#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
from menu import menu


# In[ ]:


if "project" not in st.session_state:
    st.session_state.project = None
    
st.session_state._project = st.session_state.project

def set_project():
    # Callback function to save the role selection to Session State
    st.session_state.project = st.session_state._project

st.header("Projecten Eigen Haard")
st.selectbox(
    'Om wat voor soort project gaat het?',
    ['Nieuwbouw woningen', 'Renovatie'], 
    index=None,
    placeholder="Selecteer een soort project",
    key="_project", 
    on_change=set_project, 
)
menu()

# st.page_link("dashboard.py", label="Home")
# st.page_link("pages/buitenkozijnen.py", label="Buitenkozijnen, -ramen, -deuren en -puien")


# In[ ]:


if st.session_state.project is not None:    
    st.markdown("**Budget**")
    st.markdown("Vul het budget in voor het huidige project.")
    budget = st.number_input("Vul het budget in", value=None, placeholder="Typ een bedrag")

    


# In[ ]:


if st.session_state.project is not None:    
    st.markdown("**Weging onderdelen**")
    st.markdown("Hebben onderstaande onderdelen een zwaardere weging? De weging van de onderdelen staat standaard op 1. Als er onderdelen zijn die zwaarder wegen kunnen die hieronder aangepast worden.")

    st.markdown("**Aanschafprijs**")
    aanschafprijs = st.number_input("Weging", min_value=1, key=1)

    st.markdown("**Onderhoudsprijs**")
    onderhoudsprijs = st.number_input("Weging", min_value=1, key=2)

    st.markdown("**Mate van losmaakbaarheid**")
    losmaakbaarheid = st.number_input("Weging", min_value=1, key=3)

    st.markdown("**Toepassingsmogelijkheden**")
    toepassingsmogelijkheden = st.number_input("Weging", min_value=1, key=4)

    st.markdown("**Woonbeleving**")
    woonbeleving = st.number_input("Weging", min_value=1, key=5)

    st.markdown("**Milieubelasting**")
    milieubelasting = st.number_input("Weging", min_value=1, key=6)

    st.markdown("**Flexibiliteit tbv toekomstbestendigheid en innovatie**")
    flexibiliteit = st.number_input("Weging", min_value=1, key=7)

    st.markdown("**Mate van standaardisering**")
    standaardisering = st.number_input("Weging", min_value=1, key=8)


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


