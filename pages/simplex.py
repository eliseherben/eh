#!/usr/bin/env python
# coding: utf-8

# In[21]:


# pip install pulp


# In[22]:


import streamlit as st
import pandas as pd
import plotly.express as px
import pulp as pl
from menu import menu_with_redirect
menu_with_redirect()


# als de impact cijfers integers zijn dan kunnen de weighted dingen niet integers zijn, om te voorkomen dat er 0 uit komt bij een van de opties
# 

# In[24]:


st.title("Eigen Haard")
tab1, tab2, tab3 = st.tabs(["Input", "Optimalisatie", "Aanpassingen"])


# **input tab**

# In[25]:


with tab1:
    st.markdown("**Soort project**")
    st.selectbox(
    "Om wat voor soort project gaat het?",
    ['Nieuwbouw woningen', 'Renovatie', 'Planmatig onderhoud', 'Mutatie onderhoud', 'Dagelijks onderhoud'],
    index=None,
    placeholder="Selecteer een soort project"
    )
    
    st.markdown("**Projectfase**")
    st.selectbox(
    "Wat is de fase van het project?",
    ['Projectdefinitie', 'Structuurontwerp', 'Voorontwerp', 'Definitief ontwerp', 'Technisch ontwerp bestek', 'Uitvoeringsgereed ontwerp', 'Gebruik'],
    index = None,
    placeholder = "Selecteer de fase van het project"
    )
    
    st.markdown("**Budget**")
    st.number_input("Vul het budget in voor het huidige project", value=None, placeholder="Typ een bedrag")
    
    st.markdown("**Wegingen**")
    st.markdown("Hieronder kan er per thema aangegeven worden of deze zwaarder of minder zwaar meeweegt tijdens dit project. "
    "Als een thema neutraal is kan deze op '0' blijven staan. Als een thema zwaarder meeweegt kan deze op +1 of +2 staan, "
    "als een thema minder zwaar meeweegt kan deze op -1 of -2 gezet worden. ")
    weging_woonbeleving = st.number_input("De weging in voor het thema 'Woonbeleving' in dit project", value=0, min_value = -2, max_value = 2)
    weging_duurzaam = st.number_input("De weging in voor het thema 'Duurzaam' in dit project", value=0, min_value = -2, max_value = 2)
    weging_kosten = st.number_input("De weging in voor het thema 'Kosten' in dit project", value=0, min_value = -2, max_value = 2)
    weging_onderhoud = st.number_input("De weging in voor het thema 'Onderhoud' in dit project", value=0, min_value = -2, max_value = 2)
    weging_kwaliteit = st.number_input("De weging in voor het thema 'Kwaliteit' in dit project", value=0, min_value = -2, max_value = 2)

    # if weging_woonbeleving == 0:
    #     weging_woonbeleving +
    
    st.markdown("**Productgroepen**")
    st.markdown("Hierbij kan er aangegeven worden wat het aandeel van de productgroepen momenteel in het project is. Dit is uitgedrukt in percentages. ")
    st.number_input("Het aandeel van de productgroep 'Keuken' in dit project", value=0, min_value = 0, max_value = 100)
    st.number_input("Het aandeel van de productgroep 'Sanitair' in dit project", value=0, min_value = 0, max_value = 100)
    st.number_input("Het aandeel van de productgroep 'Na-isolatie' in dit project", value=0, min_value = 0, max_value = 100)



# **optimalisatie op basis van impact waardes van materialenlijst**

# In[36]:


data = {
    "productgroep": ['21 Buitenwanden', '22 Binnenwanden', '23 Vloeren', '24 Trappen en hellingen', '27 Daken', '28 Hoofddraagconstructie', 
                     '31 Buitenkozijnen, -ramen, -deuren, en -puien', '32 Binnenkozijnen en -deuren', '33 Luiken en vensters', 
                     '34 Balustrades en leuningen', '42 Binnenwandafwerkingen', '43 Vloerafwerkingen', '45 Plafonds', '48 Na-isolatie', 
                     '52 Riolering en HWA', '53 Warm- en koud water installaties', '56 Verwarming en koeling', '57 Luchtbehandeling', 
                     '61 Elektrische installaties', '64 Vaste gebouwvoorziening', '65 Beveiliging', '66 Lift', '73 Keuken', '74 Sanitair', 
                     '90 Terreininrichting'],
    "impact duurzaam": [0.5, 0.6, 0, 0, 0.786, 0, 0.257, 0.188, 0.2, 0, 0.154, 0.15, 0, 1, 0.158, 0, 0.091, 0, 0.667, 0, 0, 0, 0.2, 0.182, 0], 
    "impact kosten": [0.042, 0.1, -0.25, 0.111, 0.143, 0, 0.086, 0.063, 0, 0, 0.231, 0, 0, 0, 0.158, 0, 0, 0.083, 0.5, 0.182, 0, 0, -0.2, 0.182, 0.111], 
    "impact woonbeleving": [0, 0, 0.25, 0.111, 0, 0, 0.029, 0.188, 0, 0, 0.385, 0.35, 0.25, 0, 0.053, 0.111, 0.091, 0.167, 0, 0.364, 0, 0, 0.2, 0, 0], 
    "impact kwaliteit": [0.167, 0, 0, 0.111, 0.071, 0, 0.2, 0.125, 0, 0, 0.077, 0.6, 0.25, 0, 0.053, 0.222, 0.091, 0.083, 0.667, 0.545, 0, 1, 0.2, 0, 0], 
    "impact onderhoud": [0.042, 0, 0.25, 0, 0.214, 0, 0.086, 0, 0, 0, 0.308, 0.4, 0, 0, 0, 0, 0.091, 0.083, 0.667, 0, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

duurzaam = df[['productgroep', 'impact duurzaam']]
duurzaam = duurzaam.sort_values(by='impact duurzaam', ascending=False)
duurzaam = duurzaam.reset_index(drop=True)

kosten = df[['productgroep', 'impact kosten']]
kosten = kosten.sort_values(by='impact kosten', ascending=False)
kosten = kosten.reset_index(drop=True)

woonbeleving = df[['productgroep', 'impact woonbeleving']]
woonbeleving = woonbeleving.sort_values(by='impact woonbeleving', ascending=False)
woonbeleving = woonbeleving.reset_index(drop=True)

kwaliteit = df[['productgroep', 'impact kwaliteit']]
kwaliteit = kwaliteit.sort_values(by='impact kwaliteit', ascending=False)
kwaliteit = kwaliteit.reset_index(drop=True)

onderhoud = df[['productgroep', 'impact onderhoud']]
onderhoud = onderhoud.sort_values(by='impact onderhoud', ascending=False)
onderhoud = onderhoud.reset_index(drop=True)


# In[37]:


with tab2: 
    st.markdown('**Duurzaam**')
    st.markdown(
    f"""
    De productgroepen die het meeste impact maken op het thema 'Duurzaam':
    - {duurzaam['productgroep'].iloc[0]}
    - {duurzaam['productgroep'].iloc[1]}
    - {duurzaam['productgroep'].iloc[2]}
    """
    )
    st.markdown('**Kosten**')
    st.markdown(
    f"""
    De productgroepen die het meeste impact maken op het thema 'Kosten':
    - {kosten['productgroep'].iloc[0]}
    - {kosten['productgroep'].iloc[1]}
    - {kosten['productgroep'].iloc[2]}
    """
    )
    st.markdown('**Woonbeleving**')
    st.markdown(
    f"""
    De productgroepen die het meeste impact maken op het thema 'Woonbeleving':
    - {woonbeleving['productgroep'].iloc[0]}
    - {woonbeleving['productgroep'].iloc[1]}
    - {woonbeleving['productgroep'].iloc[2]}
    """
    )
    st.markdown('**Kwaliteit**')
    st.markdown(
    f"""
    De productgroepen die het meeste impact maken op het thema 'Kwaliteit':
    - {kwaliteit['productgroep'].iloc[0]}
    - {kwaliteit['productgroep'].iloc[1]}
    - {kwaliteit['productgroep'].iloc[2]}
    """
    )
    st.markdown('**Onderhoud**')
    st.markdown(
    f"""
    De productgroepen die het meeste impact maken op het thema 'Onderhoud':
    - {onderhoud['productgroep'].iloc[0]}
    - {onderhoud['productgroep'].iloc[1]}
    - {onderhoud['productgroep'].iloc[2]}
    """
    )


# In[43]:


# Creëer een LP probleem
prob = pl.LpProblem("Eigen Haard", pl.LpMaximize)

# Definieer de variabelen
buitenwanden = pl.LpVariable("buitenwanden", lowBound=1)
binnenwanden = pl.LpVariable("binnenwanden", lowBound=1)
vloeren = pl.LpVariable("vloeren", lowBound=1)
trappen_hellingen = pl.LpVariable("trappen_hellingen", lowBound=1)
daken = pl.LpVariable("daken", lowBound=1)
hoofddraagconstructie = pl.LpVariable("hoofddraagconstructie", lowBound=1)
buitenkozijnen = pl.LpVariable("buitenkozijnen", lowBound=1)
binnenkozijnen = pl.LpVariable("binnenkozijnen", lowBound=1)
luiken_vensters = pl.LpVariable("luiken_vensters", lowBound=1)
balustrades_leuningen = pl.LpVariable("balustrades_leuningen", lowBound=1)
binnenwandafwerkingen = pl.LpVariable("binnenwandafwerkingen", lowBound=1)
vloerafwerkingen = pl.LpVariable("vloerafwerkingen", lowBound=1)
plafonds = pl.LpVariable("plafonds", lowBound=1)
na_isolatie = pl.LpVariable("na_isolatie", lowBound=1)
riolering_hwa = pl.LpVariable("riolering_hwa", lowBound=1)
water_installaties = pl.LpVariable("water_installaties", lowBound=1)
verwarming_koeling = pl.LpVariable("verwarming_koeling", lowBound=1)
luchtbehandeling = pl.LpVariable("luchtbehandeling", lowBound=1)
elektrische_installaties = pl.LpVariable("elektrische_installaties", lowBound=1)
gebouwvoorzieningen = pl.LpVariable("gebouwvoorzieningen", lowBound=1)
beveiliging = pl.LpVariable("beveiliging", lowBound=1)
lift = pl.LpVariable("lift", lowBound=1)
keuken = pl.LpVariable("keuken", lowBound=1)
sanitair = pl.LpVariable("sanitair", lowBound=1)
terreininrichting = pl.LpVariable("terreininrichting", lowBound=1)

variabelen = [buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, binnenkozijnen, luiken_vensters, 
              balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, riolering_hwa, water_installaties, 
              verwarming_koeling, luchtbehandeling, elektrische_installaties, gebouwvoorzieningen, beveiliging, lift, keuken, sanitair, terreininrichting]

#Impact themas op productgroepen
impact_duurzaamheid = [0.5, 0.6, 0, 0, 0.786, 0, 0.257, 0.188, 0.2, 0, 0.154, 0.15, 0, 1, 0.158, 0, 0.091, 0, 0.667, 0, 0, 0, 0.2, 0.182, 0]
duurzaamheid = pl.lpSum(variabelen[i] * impact_duurzaamheid[i] for i in range(25))

impact_prijs = [0.042, 0.1, -0.25, 0.111, 0.143, 0, 0.086, 0.063, 0, 0, 0.231, 0, 0, 0, 0.158, 0, 0, 0.083, 0.5, 0.182, 0, 0, -0.2, 0.182, 0.111]
prijs = pl.lpSum(variabelen[i] * impact_prijs[i] for i in range(25))

impact_woonbeleving = [0, 0, 0.25, 0.111, 0, 0, 0.029, 0.188, 0, 0, 0.385, 0.35, 0.25, 0, 0.053, 0.111, 0.091, 0.167, 0, 0.364, 0, 0, 0.2, 0, 0]
woonbeleving = pl.lpSum(variabelen[i] * impact_woonbeleving[i] for i in range(25))

impact_kwaliteit = [0.167, 0, 0, 0.111, 0.071, 0, 0.2, 0.125, 0, 0, 0.077, 0.6, 0.25, 0, 0.053, 0.222, 0.091, 0.083, 0.667, 0.545, 0, 1, 0.2, 0, 0]
kwaliteit = pl.lpSum(variabelen[i] * impact_kwaliteit[i] for i in range(25))

impact_onderhoud = [0.042, 0, 0.25, 0, 0.214, 0, 0.086, 0, 0, 0, 0.308, 0.4, 0, 0, 0, 0, 0.091, 0.083, 0.667, 0, 0, 1, 0, 0, 0]
onderhoud = pl.lpSum(variabelen[i] * impact_onderhoud[i] for i in range(25))
print(prijs) 

prob += weging_duurzaamheid * duurzaamheid - weging_kosten * prijs + weging_woonbeleving * woonbeleving + weging_kwaliteit * kwaliteit + weging_onderhoud * onderhoud
# prob += 2 * keuken + 3 * sanitair + 4 * buitenwanden + 6 * binnenwanden + 5 * elektra

# Voeg beperkingen toe (voorbeeldbeperkingen)
prob += buitenkozijnen + lift + binnenkozijnen + binnenwandafwerkingen + vloerafwerkingen + plafonds + sanitair + keuken + buitenwanden + vloeren + daken + hoofddraagconstructie + na_isolatie + riolering_hwa + terreininrichting + verwarming_koeling + luchtbehandeling + gebouwvoorzieningen + binnenwanden + trappen_hellingen + luiken_vensters + balustrades_leuningen+ water_installaties + elektrische_installaties + beveiliging == 100

# prob += buitenkozijnen >= 14
# prob += lift >= 1
# prob += binnenkozijnen >= 6
# prob += binnenwandafwerkingen >= 4
# prob += vloerafwerkingen >= 7
# prob += plafonds >= 3
# prob += sanitair >= 3
# prob += keuken >= 2
# prob += buitenwanden >= 8 
# prob += vloeren >= 1
# prob += daken >= 7
# prob += hoofddraagconstructie >= 1
# prob += na_isolatie >= 2
# prob += riolering_hwa >= 6 
# prob += terreininrichting >= 3
# prob += verwarming_koeling >= 4
# prob += luchtbehandeling >= 4
# prob += gebouwvoorzieningen >= 4
# prob += binnenwanden >= 3
# prob += trappen_hellingen >= 3
# prob += luiken_vensters >= 2
# prob += balustrades_leuningen >= 1
# prob += water_installaties  >= 3
# prob += elektrische_installaties >= 2
# prob += beveiliging >= 2

# Los het probleem op
status = prob.solve()

# Maak een lege lijst om de variabelen en hun waarden op te slaan
variabelen_waarden = []

# Voeg de variabelen en hun waarden toe aan de lijst
for var in variabelen:
    variabelen_waarden.append((var.name, var.varValue))

# Maak een DataFrame van de lijst
df = pd.DataFrame(variabelen_waarden, columns=['Productgroep', 'Waarde'])

# Toon de DataFrame
print(df)

# Toon de resultaten
print("Optimale oplossing:")

print(pl.LpStatus[status])
print("buitenkozijnen = ", buitenkozijnen.varValue)
print("lift = ", lift.varValue)
print("binnenkozijnen = ", binnenkozijnen.varValue)
print("binnenwandafwerkingen = ", binnenwandafwerkingen.varValue)
print("vloerafwerkingen = ", vloerafwerkingen.varValue)
print("plafonds = ", plafonds.varValue)
print("sanitair = ", sanitair.varValue)
print("keuken = ", keuken.varValue)
print("buitenwanden = ", buitenwanden.varValue)
print("daken = ", daken.varValue)
print("vloeren = ", vloeren.varValue)
print("hoofddraagconstructie = ", hoofddraagconstructie.varValue)
print("na_isolatie = ", na_isolatie.varValue)
print("riolering_hwa = ", riolering_hwa.varValue)
print("terreininrichting = ", terreininrichting.varValue)
print("verwarming_koeling = ", verwarming_koeling.varValue)
print("luchtbehandeling = ", luchtbehandeling.varValue)
print("gebouwvoorzieningen =", gebouwvoorzieningen.varValue)
print("binnenwanden =", binnenwanden.varValue)
print("trappen_hellingen =", trappen_hellingen.varValue)
print("luiken_vensters =", luiken_vensters.varValue)
print("balustrades_leuningen =", balustrades_leuningen.varValue)
print("water_installaties =", water_installaties.varValue)
print("elektrische_installaties =", elektrische_installaties.varValue)
print("beveiliging =", beveiliging.varValue)

print("Maximale waarde van de doelfunctie:", prob.objective.value())
print(prob.objective.value())


# In[ ]:


with tab2:
    st.markdown("**In dit project, is het optimaal om het aandeel van de productgroepen als volgt in te delen:**")
    
    for index, row in df.iterrows():
        st.markdown(f"- De productgroep {row['Productgroep']} is {row['Waarde']}% van het totale project")
    
    fig1 = px.pie(values=df['Waarde'], names=df['Productgroep'], color_discrete_sequence=px.colors.sequential.RdBu)
    
    st.plotly_chart(fig1)


# **aanpassingen**

# In[4]:


with tab3:
    try:
        st.markdown("Hieronder kunnen de verschillende aandelen van productgroepen aangepast worden, om daarvan de invloed te zien op de verschillende thema's")
    
        def max_sliders(waardes):
            max_waarde = 100 - sum(waardes)
            return max_waarde
        
        waardes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
        buitenwanden_max = max_sliders(waardes)
        buitenwanden = st.slider('Het aandeel van de productgroep Buitenwanden', 0, buitenwanden_max, 0)
        
        binnenwanden_max = max_sliders([buitenwanden, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        binnenwanden = st.slider('Het aandeel van de productgroep Binnenwanden', 0, binnenwanden_max, 0)
    
        vloeren_max = max_sliders([buitenwanden, binnenwanden, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        vloeren = st.slider('Het aandeel van de productgroep Vloeren', 0, vloeren_max, 0)
    
        trappen_hellingen_max = max_sliders([buitenwanden, binnenwanden, vloeren, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        trappen_hellingen = st.slider('Het aandeel van de productgroep Trappen en hellingen', 0, trappen_hellingen_max, 0)
    
        daken_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        daken = st.slider('Het aandeel van de productgroep Daken', 0, daken_max, 0)
    
        hoofddraagconstructie_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, 
                                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        hoofddraagconstructie = st.slider('Het aandeel van de productgroep Hoofddraagconstructie', 0, hoofddraagconstructie_max, 0)
    
        buitenkozijnen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, 
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        buitenkozijnen = st.slider('Het aandeel van de productgroep Buitenkozijnen', 0, buitenkozijnen_max, 0)
    
        binnenkozijnen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        binnenkozijnen = st.slider('Het aandeel van de productgroep Binnenkozijnen', 0, binnenkozijnen_max, 0)
    
        luiken_vensters_max =  max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, binnenkozijnen, 
                                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        luiken_vensters = st.slider('Het aandeel van de productgroep Luiken en vensters', 0, luiken_vensters_max, 0)
        
        balustrades_leuningen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, binnenkozijnen, 
                                       luiken_vensters, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        balustrades_leuningen = st.slider('Het aandeel van de productgroep Balustrades', 0, balustrades_leuningen_max, 0)
        
        binnenwandafwerkingen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                                 binnenkozijnen, luiken_vensters, balustrades_leuningen, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        binnenwandafwerkingen = st.slider('Het aandeel van de productgroep Binnenwandafwerkingen', 0, binnenwandafwerkingen_max, 0)
        
        vloerafwerkingen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        vloerafwerkingen = st.slider('Het aandeel van de productgroep Vloerafwerkingen', 0, vloerafwerkingen_max, 0)
        
        plafonds_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, 
                                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        plafonds = st.slider('Het aandeel van de productgroep Plafonds', 0, plafonds_max, 0)
        
        na_isolatie_max =  max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, 
                                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        na_isolatie = st.slider('Het aandeel van de productgroep Na-isolatie', 0, na_isolatie_max, 0)
        
        riolering_hwa_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        riolering_hwa = st.slider('Het aandeel van de productgroep Riolering en HWA', 0, riolering_hwa_max, 0)
        
        water_installaties_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        water_installaties = st.slider('Het aandeel van de productgroep Warm- en koud water installaties', 0, water_installaties_max, 0)
        
        verwarming_koeling_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        verwarming_koeling = st.slider('Het aandeel van de productgroep Verwarming en koeling', 0, verwarming_koeling_max, 0)
    
        luchtbehandeling_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, 0, 0, 0, 0, 0, 0, 0, 0])
        luchtbehandeling = st.slider('Het aandeel van de productgroep Luchtbehandeling', 0, luchtbehandeling_max, 0)
        
        elektrische_installaties_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, 0, 0, 0, 0, 0, 0, 0])
        elektrische_installaties = st.slider('Het aandeel van de productgroep Elektrische installaties', 0, elektrische_installaties_max, 0)
        
        gebouwvoorzieningen_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               0, 0, 0, 0, 0, 0])
        gebouwvoorzieningen = st.slider('Het aandeel van de productgroep Gebouwvoorzieningen', 0, gebouwvoorzieningen_max, 0)
        
        beveiliging_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               gebouwvoorzieningen, 0, 0, 0, 0, 0])
        beveiliging = st.slider('Het aandeel van de productgroep Beveiliging', 0, beveiliging_max, 0)
        
        lift_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               gebouwvoorzieningen, beveiliging, 0, 0, 0, 0])
        lift = st.slider('Het aandeel van de productgroep Lift', 0, lift_max, 0)
        
        keuken_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               gebouwvoorzieningen, beveiliging, lift, 0, 0, 0])
        keuken = st.slider('Het aandeel van de productgroep Keuken', 0, keuken_max, 0)
        
        sanitair_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               gebouwvoorzieningen, beveiliging, lift, keuken, 0, 0])
        sanitair = st.slider('Het aandeel van de productgroep Sanitair', 0, sanitair_max, 0)
        
        terreininrichting_max = max_sliders([buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, 
                                            binnenkozijnen, luiken_vensters, balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, 
                                             riolering_hwa, water_installaties, verwarming_koeling, luchtbehandeling, elektrische_installaties, 
                                               gebouwvoorzieningen, beveiliging, lift, keuken, sanitair, 0])
        terreininrichting = st.slider('Het aandeel van de productgroep Terreininrichting', 0, terreininrichting_max, 0)
    
    except RangeError:
         st.error("Er is een fout opgetreden: De totale aandeel van productgroepen kan samen maar 100% zijn.")


# In[ ]:


with tab3:
    col1, col2 = st.columns(2)

    with col2:
        st.markdown("**aanpassing**")
        variabelen = [buitenwanden, binnenwanden, vloeren, trappen_hellingen, daken, hoofddraagconstructie, buitenkozijnen, binnenkozijnen, luiken_vensters, 
                      balustrades_leuningen, binnenwandafwerkingen, vloerafwerkingen, plafonds, na_isolatie, riolering_hwa, water_installaties, 
                      verwarming_koeling, luchtbehandeling, elektrische_installaties, gebouwvoorzieningen, beveiliging, lift, keuken, sanitair, terreininrichting]
        productgroep = ['buitenwanden', 'binnenwanden', 'vloeren', 'trappen_hellingen', 'daken', 'hoofddraagconstructie', 'buitenkozijnen', 
                        'binnenkozijnen', 'luiken_vensters', 'balustrades_leuningen', 'binnenwandafwerkingen', 'vloerafwerkingen', 'plafonds', 
                        'na_isolatie', 'riolering_hwa', 'water_installaties', 'verwarming_koeling', 'luchtbehandeling', 
                        'elektrische_installaties', 'gebouwvoorzieningen', 'beveiliging', 'lift', 'keuken', 'sanitair', 'terreininrichting']
        for i in range(25):
            st.markdown(f"- {productgroep[i]}: {variabelen[i]}%")
        
        #Impact themas op productgroepen
        impact_duurzaamheid = [0.5, 0.6, 0, 0, 0.786, 0, 0.257, 0.188, 0.2, 0, 0.154, 0.15, 0, 1, 0.158, 0, 0.091, 0, 0.667, 0, 0, 0, 0.2, 0.182, 0]
        duurzaamheid = sum([variabelen[i] * impact_duurzaamheid[i] for i in range(25)])
        st.markdown(f"score duurzaamheid: {duurzaamheid}")
        
        impact_prijs = [0.042, 0.1, -0.25, 0.111, 0.143, 0, 0.086, 0.063, 0, 0, 0.231, 0, 0, 0, 0.158, 0, 0, 0.083, 0.5, 0.182, 0, 0, -0.2, 0.182, 0.111]
        prijs = sum([variabelen[i] * impact_prijs[i] for i in range(25)])
        st.markdown(f"score prijs: {prijs}")  
    
        impact_woonbeleving = [0, 0, 0.25, 0.111, 0, 0, 0.029, 0.188, 0, 0, 0.385, 0.35, 0.25, 0, 0.053, 0.111, 0.091, 0.167, 0, 0.364, 0, 0, 0.2, 0, 0]
        woonbeleving = sum([variabelen[i] * impact_woonbeleving[i] for i in range(25)])
        st.markdown(f"score woonbeleving: {woonbeleving}")  
        
        impact_kwaliteit = [0.167, 0, 0, 0.111, 0.071, 0, 0.2, 0.125, 0, 0, 0.077, 0.6, 0.25, 0, 0.053, 0.222, 0.091, 0.083, 0.667, 0.545, 0, 1, 0.2, 0, 0]
        kwaliteit = sum([variabelen[i] * impact_kwaliteit[i] for i in range(25)])
        st.markdown(f"score kwaliteit: {kwaliteit}")  
        
        impact_onderhoud = [0.042, 0, 0.25, 0, 0.214, 0, 0.086, 0, 0, 0, 0.308, 0.4, 0, 0, 0, 0, 0.091, 0.083, 0.667, 0, 0, 1, 0, 0, 0]
        onderhoud = sum([variabelen[i] * impact_onderhoud[i] for i in range(25)])
        st.markdown(f"score onderhoud: {onderhoud}")  

    with col1:
        st.markdown("**optimalisatie**")
        for index, row in df.iterrows():
            st.markdown(f"- {row['Productgroep']}: {row['Waarde']}%")
        for index, row in df.interrows():
            st.markdown(f"score duurzaamheid: {sum([row['Waarde'] * impact_duurzaamheid[i] for i in range(25)])")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




