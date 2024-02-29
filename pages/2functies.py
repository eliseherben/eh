#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from menu import menu_with_redirect
import random
import pandas as pd
import plotly.express as px
menu_with_redirect()


# In[ ]:


st.title("Optimalisatie")


# ### Genetic algorithm

# In[ ]:


productgroepen = ["Buitenkozijnen, -ramen, -deuren en -puien", "Lift", "Binnenkozijnen en deuren", 
                  "Binnenwandafwerkingen", "Vloerafwerkingen", "Plafonds", "Sanitair", "Keuken", "Buitenwanden", 
                 "Vloeren", "Daken", "Hoofddraagconstructie", "Na-isolatie binnen", "Riolering en HWA", "Terreininrichting", 
                 "Verwarming en koeling", "Luchtbehandeling", "Vaste gebouwvoorzieningen", "Binnenwanden", 
                 "Trappen en hellingen", "Luiken en vensters", "Balustrades en leuningen", "Warm- en koud water installaties", 
                 "Elektrische installaties", "Beveiliging"]


# In[ ]:


sessions = [st.session_state.buitenkozijnen, st.session_state.lift, st.session_state.binnenkozijnen, 
            st.session_state.binnenwandafwerking, st.session_state.vloerafwerking, st.session_state.plafonds, 
            st.session_state.sanitair, st.session_state.keuken, st.session_state.buitenwanden, st.session_state.vloeren, 
            st.session_state.daken, st.session_state.hoofddraagconstructie, st.session_state.isolatie, 
            st.session_state.riolering, st.session_state.terreininrichting, st.session_state.verwarming, 
            st.session_state.luchtbehandeling, st.session_state.gebouwvoorzieningen, st.session_state.binnenwanden, 
            st.session_state.trappen, st.session_state.luiken, st.session_state.balustrades, st.session_state.water, 
            st.session_state.elektra, st.session_state.beveiliging]


# In[ ]:


maximaal = [st.session_state.max_buitenkozijnen, st.session_state.max_lift, st.session_state.max_binnenkozijnen, 
            st.session_state.max_binnenwandafwerking, st.session_state.max_vloerafwerking, st.session_state.max_plafonds, 
            st.session_state.max_sanitair, st.session_state.max_keuken, st.session_state.max_buitenwanden, 
            st.session_state.max_vloeren, st.session_state.max_daken, st.session_state.max_hoofddraagconstructie, 
            st.session_state.max_isolatie, st.session_state.max_riolering, st.session_state.max_terreininrichting, 
            st.session_state.max_verwarming, st.session_state.max_luchtbehandeling, st.session_state.max_gebouwvoorzieningen, 
            st.session_state.max_binnenwanden, st.session_state.max_trappen, st.session_state.max_luiken, 
            st.session_state.max_balustrades, st.session_state.max_water, st.session_state.max_elektra, 
            st.session_state.max_beveiliging]


# In[ ]:


minmax = [st.session_state.min_max_buitenkozijnen, st.session_state.min_max_lift, st.session_state.min_max_binnenkozijnen, 
            st.session_state.min_max_binnenwandafwerking, st.session_state.min_max_vloerafwerking, st.session_state.min_max_plafonds, 
            st.session_state.min_max_sanitair, st.session_state.min_max_keuken, st.session_state.min_max_buitenwanden, 
            st.session_state.min_max_vloeren, st.session_state.min_max_daken, st.session_state.min_max_hoofddraagconstructie, 
            st.session_state.min_max_isolatie, st.session_state.min_max_riolering, st.session_state.min_max_terreininrichting, 
            st.session_state.min_max_verwarming, st.session_state.min_max_luchtbehandeling, st.session_state.min_max_gebouwvoorzieningen, 
            st.session_state.min_max_binnenwanden, st.session_state.min_max_trappen, st.session_state.min_max_luiken, 
            st.session_state.min_max_balustrades, st.session_state.min_max_water, st.session_state.min_max_elektra, 
            st.session_state.min_max_balustrades, st.session_state.min_max_water, st.session_state.min_max_elektra, 
            st.session_state.min_max_beveiliging]


# **startpopulatie**

# In[ ]:


def dominates(x, y):
    return (x[0] <= y[0] and x[1] <= y[1] and x[2] >= y[2] and x[3] >= y[3] and 
            x[4] >= y[4] and x[5] <= y[5] and x[6] >= y[6] and x[7] >= y[7] and 
            (x[0] < y[0] or x[1] < y[1] or x[2] > y[2] or x[3] > y[3] or 
             x[4] > y[4] or x[5] < y[5] or x[6] > y[6] or x[7] > y[7]))


# In[ ]:


def f1(x):
    return (6 * x[0] + 9 * x[1] + 2 * x[2] + 7 * x[3] + 4 * x[4] + 4 * x[5] + 6 * x[6] + x[7] + 4 * x[8] + 7 * x[9] + 
            9 * x[10] + 10 * x[11] + 4 * x[12] + 2 * x[13] + 6 * x[14] + 6 * x[15] + 2 * x[16] + x[17] + 5 * x[18] + 
            4 * x[19] + 4 * x[20] + 10 * x[21] + 2 * x[22] + 2.5 * x[23] + 9 * x[24]) 
 
def f5(x):
    return (9.5 * x[0] + 10 * x[1] + 4 * x[2] + 8 * x[3] + 6 * x[4] + 7 * x[5] + 6 * x[6] + 8 * x[7] + 6.5 * x[8] + 4 * x[9] + 
            x[10] + 5 * x[11] + 5 * x[12] + 4 * x[13] + 8 * x[14] + 6 * x[15] + 6 * x[16] + 6 * x[17] + 8 * x[18] + 3 * x[19] + 
            4 * x[20] + 4 * x[21] + 2 * x[22] + 4 * x[23] + 6 * x[24]) 


def uitkomsten(oplossing):
    aanschafprijs = f1(oplossing)
    woonbeleving = f5(oplossing)
    return -aanschafprijs + woonbeleving 

def startoplossing():
    startoplossing = [random.randint(0, 200) for _ in range(25)]
    if st.session_state.fase == 'Budget te veel':
        for i, s, m in zip(range(len(startoplossing)), sessions, maximaal):
            if startoplossing[i] < s:
                startoplossing[i] = s
            elif startoplossing[i] > m:
                startoplossing[i] = m
            else:
                startoplossing[i] = startoplossing[i]
    else:
        for i, m in zip(range(len(startoplossing)), minmax):
            if startoplossing[i] < m[0]:
                startoplossing[i] = m[0]
            elif startoplossing[i] > m[1]:
                startoplossing[i] = m[1]
            else:
                startoplossing[i] = startoplossing[i]
    return startoplossing
                   
def startpopulatie(startoplossing):
    huidige_oplossing = startoplossing
    
    populatie = [huidige_oplossing]
    
    for _ in range(19):
        nieuwe_oplossing = [random.randint(0, 200) for _ in range(25)]
        if st.session_state.fase == 'Budget te veel':
            for i, s, m in zip(range(len(nieuwe_oplossing)), sessions, maximaal):
                if nieuwe_oplossing[i] < s:
                    nieuwe_oplossing[i] = s
                elif nieuwe_oplossing[i] > m:
                    nieuwe_oplossing[i] = m
                else:
                    nieuwe_oplossing[i] = nieuwe_oplossing[i]
        else:
            for i, m in zip(range(len(nieuwe_oplossing)), minmax):
                if nieuwe_oplossing[i] < m[0]:
                    nieuwe_oplossing[i] = m[0]
                elif nieuwe_oplossing[i] > m[1]:
                    nieuwe_oplossing[i] = m[1]
                else:
                    nieuwe_oplossing[i] = nieuwe_oplossing[i]
                    
        nieuwe_uitkomsten = [f1(nieuwe_oplossing), f5(nieuwe_oplossing)]
        dominated = False
        for sol in populatie:
            if dominates(nieuwe_uitkomsten, [f1(sol), f5(sol)]):
                st.markdown(f"nieuwe {nieuwe_oplossing} dominates een oude {sol}")
                st.markdown(populatie)
                populatie.remove(sol)
            if dominates([f1(sol), f5(sol)], nieuwe_uitkomsten):
                st.markdown(f"oude {sol} dominates de nieuwe {nieuwe_oplossing}")
                dominated = True
                break
        if not dominated:
            populatie.append(nieuwe_oplossing)
    
    for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), uitkomsten(populatie[x]))
    populatie.sort(key=lambda uitkomst: uitkomst[1], reverse = True)

    return populatie


# In[ ]:


def ouders_maken(populatie):
    ouders = []
    beste = [i for i in populatie[0:10]]
    slechtste = [i for i in populatie[10:]] 
    i = 0
    while i < 7:    
        ouders.append(random.choice(beste))
        i = i + 1

    j = 0
    while j < 3:
        ouders.append(random.choice(slechtste))
        j = j + 1
    return ouders


# In[ ]:


def kinderen_maken(ouders):
    kinderen = []
    while len(ouders) != 0:
        parent1 = random.choice(ouders)
        ouders.remove(parent1)
        parent2 = random.choice(ouders)
        ouders.remove(parent2)
        for k in range(2):
            kind = []
            if st.session_state.fase == 'Budget te veel':
                for i, s, m in zip(range(25), sessions, maximaal):
                    if random.randint(0, 10) == 1:
                        kind.append(random.randint(s, m))
                        i = i + 1
                    else:
                        kind.append(random.choice([parent1[i], parent2[i]]))
            else:
                for i, m in zip(range(25), minmax):
                    if random.randint(0, 10) == 1:
                        kind.append(random.randint(m[0], m[1]))
                        i = i + 1
                    else:
                        kind.append(random.choice([parent1[i], parent2[i]]))
            kinderen.append(kind)
            k = k + 1
    return kinderen


# In[ ]:


startoplossing = startoplossing()
startpopulatie = startpopulatie(startoplossing)

iteraties = 0
while iteraties < 5:
    populatie = [tuple(i[0]) for i in startpopulatie]
    ouders = ouders_maken(populatie)
    populatie = [i for i in populatie[0:10]]
    kinderen = kinderen_maken(ouders)
    for a in kinderen:
        populatie.append(tuple(a))
    for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), uitkomsten(populatie[x]))
    populatie.sort(key=lambda uitkomst: uitkomst[1], reverse = True)
    iteraties = iteraties + 1


# In[ ]:


populatie = [tuple(i[0]) for i in populatie]
st.markdown(f"{populatie} {len(populatie)}")

for pareto in populatie:
    uitkomsten_pareto = [f1(pareto), f5(pareto)]
    for sol in populatie:
        if dominates(uitkomsten_pareto, [f1(sol), f5(sol)]):
            st.markdown(f"pareto {pareto} dominates sol {sol}")
            populatie.remove(sol)
        if dominates([f1(sol), f5(sol)], uitkomsten_pareto):
            st.markdown(f"pareto {pareto} dominates sol {sol}")
            populatie.remove(pareto)

st.markdown(f"{populatie} {len(populatie)}")


# In[ ]:


aanschafprijs = []
onderhoudsprijs = []
losmaakbaarheid = []
toepassingsmogelijkheden = []
woonbeleving = []
milieubelasting = []
flexibiliteit = []
standaardisering = []

for oplossing in populatie:
    aanschafprijs.append(f1(oplossing))
    woonbeleving.append(f5(oplossing))
    
dict = {'Oplossing': populatie, 'Aanschafprijs': aanschafprijs, 'Woonbeleving': woonbeleving} 

df = pd.DataFrame(dict)
st.dataframe(df)  # Same as st.write(df)


# In[ ]:


x_kolom = st.selectbox("Selecteer een optie voor de x-as", df.columns[1:])
y_kolom = st.selectbox("Selecteer een optie voor de y-as", df.columns[1:])


fig = px.scatter(df, x=x_kolom, y=y_kolom, hover_data={"Oplossing": True})
st.plotly_chart(fig)


# In[ ]:


for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), f1(populatie[x]), f2(populatie[x]), f3(populatie[x]), f4(populatie[x]), f5(populatie[x]), f7(populatie[x]), f8(populatie[x]))

if st.session_state.doelstelling == 'Aanschafprijs':
    populatie.sort(key=lambda aanschafprijs: aanschafprijs[1])
if st.session_state.doelstelling == 'Woonbeleving':
    populatie.sort(key=lambda woonbeleving: woonbeleving[5], reverse=True)


# In[ ]:


populatie = [tuple(i[0]) for i in populatie]

st.markdown("### Genetic algorithm:")
i = 0
    
for solution in populatie:
    i = i + 1
    j = 0
    st.markdown(f"#### Oplossing {i}")
    st.markdown(f"totale score: {uitkomsten(solution)}")
    for product in productgroepen:
        st.markdown(f"Aantal producten in de productgroep {product} {solution[j]}")
        j = j + 1
    st.markdown(f"{solution} {len(solution)}")
    st.markdown("#### Objective Values:")
    st.markdown(f"- aanschafkosten: {f1(solution)} ")
    st.markdown(f"- woonbeleving: {f5(solution)}")


# In[ ]:




