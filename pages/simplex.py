#!/usr/bin/env python
# coding: utf-8

# In[5]:


# pip install pulp


# In[4]:


import streamlit as st
import pandas as pd
import plotly.express as px
from pulp import *


# In[ ]:


# Creëer een LP probleem
prob = LpProblem("Maximize", LpMaximize)

# Definieer de variabelen
keuken = LpVariable("keuken", lowBound=0)
sanitair = LpVariable("sanitair", lowBound=0)
buitenwanden = LpVariable("buitenwanden", lowBound=0)
binnenwanden = LpVariable("binnenwanden", lowBound=0)
elektra = LpVariable("elektra", lowBound=0)

#Impact themas op productgroepen
prijs_keuken = 2
prijs_sanitair = 5
prijs_buitenwanden = 6
prijs_binnenwanden = 4
prijs_elektra = 8

woonbeleving_keuken = 5
woonbeleving_sanitair = 4
woonbeleving_buitenwanden = 6
woonbeleving_binnenwanden = 2
woonbeleving_elektra = 4

duurzaamheid_keuken = 7
duurzaamheid_sanitair = 5
duurzaamheid_buitenwanden = 7
duurzaamheid_binnenwanden = 3
duurzaamheid_elektra = 4

# Definieer de doelfunctie
prijs = (prijs_keuken * keuken + prijs_sanitair * sanitair + prijs_buitenwanden * buitenwanden + 
         prijs_binnenwanden * binnenwanden + prijs_elektra * elektra)

woonbeleving = (woonbeleving_keuken * keuken + woonbeleving_sanitair * sanitair + woonbeleving_buitenwanden * buitenwanden +
                woonbeleving_binnenwanden * binnenwanden + woonbeleving_elektra * elektra)

duurzaamheid = (duurzaamheid_keuken * keuken + duurzaamheid_sanitair * sanitair + duurzaamheid_buitenwanden * buitenwanden +
                duurzaamheid_binnenwanden * binnenwanden + duurzaamheid_elektra * elektra)

#wegingen doelfuncties
weging_prijs = 2
weging_woonbeleving = 1
weging_duurzaamheid = 1

prob += -prijs + woonbeleving + duurzaamheid
# prob += 2 * keuken + 3 * sanitair + 4 * buitenwanden + 6 * binnenwanden + 5 * elektra

# Voeg beperkingen toe (voorbeeldbeperkingen)
prob += keuken + sanitair + buitenwanden + binnenwanden + elektra == 100
prob += keuken >= 14
prob += sanitair >= 3
prob += buitenwanden >= 24
prob += binnenwanden >= 11
prob += elektra >= 1

# Los het probleem op
status = prob.solve()

# Toon de resultaten
print("Optimale oplossing:")

print(LpStatus[status])
print("keuken = ", keuken.varValue)
print("sanitair =", sanitair.varValue)
print("buitenwanden =", buitenwanden.varValue)
print("binnenwanden =", binnenwanden.varValue)
print("elektra =", elektra.varValue)

print("Maximale waarde van de doelfunctie:", prob.objective.value())


# In[ ]:


st.title("Eigen Haard")
tab1, tab2, tab3 = st.tabs(["Input", "Optimalisatie", "Aanpassingen"])


# In[ ]:


with tab1:
    st.markdown("**Soort project**")
    st.selectbox(
    'Om wat voor soort project gaat het?',
    ['Nieuwbouw woningen', 'Renovatie'],
    index=None,
    placeholder="Selecteer een soort project"
    )
    
    st.markdown("**Projectfase**")
    st.selectbox(
    "Wat is de fase van het project?",
    ["Initiële fase", "Ontwerp fase"],
    index = None,
    placeholder = "Selecteer de fase van het project"
    )
    
    st.markdown("**Budget**")
    st.number_input("Vul het budget in voor het huidige project", value=None, placeholder="Typ een bedrag")
    
    st.markdown("**Wegingen**")
    st.markdown("Hieronder kan er per thema aangegeven worden of deze zwaarder of minder zwaar meeweegt tijdens dit project. "
    "Als een thema neutraal is kan deze op '0' blijven staan. Als een thema zwaarder meeweegt kan deze op +1 of +2 staan, "
    "als een thema minder zwaar meeweegt kan deze op -1 of -2 gezet worden. ")
    st.number_input("De weging in voor het thema 'Woonbeleving' in dit project", value=0, min_value = -2, max_value = 2)
    st.number_input("De weging in voor het thema 'Duurzaam' in dit project", value=0, min_value = -2, max_value = 2)
    st.number_input("De weging in voor het thema 'Prijs' in dit project", value=0, min_value = -2, max_value = 2)
    
    st.markdown("**Productgroepen**")
    st.markdown("Hierbij kan er aangegeven worden wat het aandeel van de productgroepen momenteel in het project is. Dit is uitgedrukt in percentages. ")
    st.number_input("Het aandeel van de productgroep 'Keuken' in dit project", value=0, min_value = 0, max_value = 100)
    st.number_input("Het aandeel van de productgroep 'Sanitair' in dit project", value=0, min_value = 0, max_value = 100)
    st.number_input("Het aandeel van de productgroep 'Na-isolatie' in dit project", value=0, min_value = 0, max_value = 100)



# In[ ]:


with tab2:
    st.markdown("In dit project, is het optimaal om het aandeel van de productgroepen als volgt in te delen:")
    st.markdown('''
    - De productgroep Keukens 20% van het totale project
    
    - De productgroep Sanitair 15% van het totale project
    
    - De productgroep Na-isolatie 7% van het totale project
    
    - De productgroep Trappen 15% van het totale project
    
    - De productgroep Vloeren 8% van het totale project
    
    - De productgroep Buitenwanden 15% van het totale project
    
    - De productgroep Vloerafwerking 20% van het totale project''')
    
    fig1 = px.pie(values=[20, 15, 7, 15, 8, 15, 20], names=['Keuken', 'Sanitair', 'Na-isolatie', 'Trappen', 'Vloeren', 'Buitenwanden', 'Vloerafwerking'], color_discrete_sequence=px.colors.sequential.RdBu)
    
    st.plotly_chart(fig1)
    
    st.markdown("Hierbij wordt rekening gehouden met de volgende wegingen van de thema's")
    
    
    # Maak een lijnplot met Plotly Express
    fig = px.bar(x=['Prijs', 'Woonbeleving', 'Mate van losmaakbaarheid', 'Toepassingsmogelijkheden'], y=[-1, 2, -2, 1], color=[-1, 2, -2, 1], color_continuous_scale='blues', range_color=(-2, 2))
    fig.update_yaxes(range=[-2, 2], tickvals=[-2, -1, 0, 1, 2], tickmode='array')
    st.plotly_chart(fig)


# In[ ]:


with tab3:
    st.markdown("Hieronder kunnen de verschillende aandelen van productgroepen aangepast worden, om daarvan de invloed te zien op de verschillende thema's")
    keukens = st.slider('Het aandeel van de productgroep Keukens', 0, 100, 20)
    sanitair = st.slider('Het aandeel van de productgroep Sanitair', 0, 100, 15)
    isolatie = st.slider('Het aandeel van de productgroep Na-isolatie', 0, 100, 7)
    trappen = st.slider('Het aandeel van de productgroep Trappen', 0, 100, 15)
    vloeren = st.slider('Het aandeel van de productgroep Vloeren', 0, 100, 8)
    buitenwanden = st.slider('Het aandeel van de productgroep Buitenwanden', 0, 100, 15)
    vloerafwerking = st.slider('Het aandeel van de productgroep Vloerafwerking', 0, 100, 20)

