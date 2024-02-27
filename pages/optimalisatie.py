#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from menu import menu_with_redirect
import random
import pandas as pd
menu_with_redirect()


# In[ ]:


st.title("Optimalisatie")


# ### Simulated annealing

# In[ ]:


# import random
# import math

# # Define the objective functions
# def f1(x):
#     result = 6*x[0] + 9*x[1] + 2*x[2] + 7*x[3] + 4*x[4] + 4*x[5] + 6*x[6] + x[7] + 4*x[8] + 7*x[9] + 9*x[10] + 10*x[11] + 4*x[12] + 2*x[13] + 6*x[14] + 6*x[15] + 2*x[16] + x[17] + 5*x[18] + 4*x[19] + 4*x[20] + 10*x[21] + 2*x[22] + 2.5*x[23] + 9*x[24]
#     return -result 

# def f2(x):
#     result = 4.5*x[0] + 2*x[1] + 6*x[2] + 4*x[3] + 4*x[4] + 5*x[5] + 10*x[6] + 3*x[7] + 6*x[8] + x[9] + x[10] + x[11] + 4*x[12] + 9*x[13] + 7.5*x[14] + 4*x[15] + 2*x[16] + x[17] + 3*x[18] + 4*x[19] + 3*x[20] + 2.5*x[21] + 4*x[22] + 6*x[23] + 5*x[24]
#     return -result 

# def f3(x):
#     result = 9.5*x[0] + 3*x[1] + 9*x[2] + 4.5*x[3] + x[4] + 3*x[5] + 9*x[6] + 9*x[7] + 4*x[8] + 6*x[9] + 8*x[10] + 2*x[11] + 9*x[12] + 4*x[13] + 6*x[14] + 6*x[15] + 4*x[16] + 6*x[17] + 7*x[18] + 4*x[19] + 6*x[20] + 6*x[21] + 8*x[22] + 7*x[23] + 4*x[24]
#     return result 

# def f4(x):
#     result = 8*x[0] + 2.5*x[1] + 8*x[2] + 5*x[3] + 6*x[4] + 3*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 7*x[10] + 7.5*x[11] + 8*x[12] + 6*x[13] + 6*x[14] + 4*x[15] + 7*x[16] + 7*x[17] + 7*x[18] + 4*x[19] + 4*x[20] + 7.5*x[21] + 6*x[22] + 5*x[23] + 3*x[24]
#     return result 

# def f5(x):
#     result = 9.5*x[0] + 10*x[1] + 4*x[2] + 8*x[3] + 6*x[4] + 7*x[5] + 6*x[6] + 8*x[7] + 6.5*x[8] + 4*x[9] + x[10] + 5*x[11] + 5*x[12] + 4*x[13] + 8*x[14] + 6*x[15] + 6*x[16] + 6*x[17] + 8*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 2*x[22] + 4*x[23] + 6*x[24]
#     return result 

# def f6(x):
#     result = 7.5*x[0] + 7.5*x[1] + 8*x[2] + 7.5*x[3] + 6*x[4] + 7.5*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 4*x[10] + 2*x[11] + 5*x[12] + 2.5*x[13] + 6*x[14] + 3*x[15] + 8*x[16] + 8*x[17] + 6*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 7*x[22] + 5*x[23] + 6*x[24]
#     return -result 

# def f7(x):
#     result = 4*x[0] + x[1] + 4*x[2] + 2*x[3] + 6*x[4] + 3*x[5] + x[6] + 4*x[7] + 4*x[8] + 4*x[9] + 2*x[10] + 4*x[11] + 6*x[12] + 2.5*x[13] + 3*x[14] + 2.5*x[15] + 4*x[16] + 4*x[17] + 4*x[18] + x[19] + 3*x[20] + 4*x[21] + 4*x[22] + 2.5*x[23] + 4*x[24]
#     return result 

# def f8(x):
#     result = 4*x[0] + x[1] + 9*x[2] + 8*x[3] + 5*x[4] + 6*x[5] + 9*x[6] + 9*x[7] + 6*x[8] + 4*x[9] + 2*x[10] + x[11] + x[12] + 5*x[13] + 2*x[14] + 2*x[15] + 8*x[16] + 6*x[17] + 7*x[18] + 2.5*x[19] + 4*x[20] + 2*x[21] + 4*x[22] + 7*x[23] + 3*x[24]
#     return result 
    
# # Check if solution x dominates solution y
# def dominates(x, y):
#     return all(xi >= yi for xi, yi in zip(x, y)) and any(xi > yi for xi, yi in zip(x, y))

# # Simulated annealing function
# def pareto_simulated_annealing(objective_functions, initial_solution, max_iterations, max_temperature, min_temperature, cooling_rate):
#     current_solution = initial_solution
#     temperature = max_temperature

#     pareto_set = [current_solution]

#     for _ in range(max_iterations):
#         new_solution = [current_solution[i] + random.randint(-1, 1) for i in range(25)]  # Perturb the current solution with random integers
        
#         #restricties geimplementeerde producten
#         new_solution[0] = max(st.session_state.buitenkozijnen, new_solution[0])  
#         new_solution[1] = max(st.session_state.lift, new_solution[1])  
#         new_solution[2] = max(st.session_state.binnenkozijnen, new_solution[2])  
#         new_solution[3] = max(st.session_state.binnenwandafwerking, new_solution[3])  
#         new_solution[4] = max(st.session_state.vloerafwerking, new_solution[4])  
#         new_solution[5] = max(st.session_state.plafonds, new_solution[5])  
#         new_solution[6] = max(st.session_state.sanitair, new_solution[6])  
#         new_solution[7] = max(st.session_state.keuken, new_solution[7])  
#         new_solution[8] = max(st.session_state.buitenwanden, new_solution[8])  
#         new_solution[9] = max(st.session_state.vloeren, new_solution[9])  
#         new_solution[10] = max(st.session_state.daken, new_solution[10])  
#         new_solution[11] = max(st.session_state.hoofddraagconstructie, new_solution[11])  
#         new_solution[12] = max(st.session_state.isolatie, new_solution[12])  
#         new_solution[13] = max(st.session_state.riolering, new_solution[13])  
#         new_solution[14] = max(st.session_state.terreininrichting, new_solution[14])  
#         new_solution[15] = max(st.session_state.verwarming, new_solution[15])  
#         new_solution[16] = max(st.session_state.luchtbehandeling, new_solution[16])  
#         new_solution[17] = max(st.session_state.gebouwvoorzieningen, new_solution[17])  
#         new_solution[18] = max(st.session_state.binnenwanden, new_solution[18])  
#         new_solution[19] = max(st.session_state.trappen, new_solution[19])  
#         new_solution[20] = max(st.session_state.luiken, new_solution[20])  
#         new_solution[21] = max(st.session_state.balustrades, new_solution[21])  
#         new_solution[22] = max(st.session_state.water, new_solution[22])  
#         new_solution[23] = max(st.session_state.elektra, new_solution[23])  
#         new_solution[24] = max(st.session_state.beveiliging, new_solution[24])  
        
#         new_objectives = [objective(new_solution) for objective in objective_functions]
#         dominated = False
#         if (new_objectives[0] + new_objectives[1]) <= st.session_state.budget:
#             for sol in pareto_set:
#                 if dominates(new_objectives, [objective(sol) for objective in objective_functions]):
#                     pareto_set.remove(sol)
#                 if dominates([objective(sol) for objective in objective_functions], new_objectives):
#                     dominated = True
#                     break
#             if not dominated:
#                 pareto_set.append(new_solution)

#         temperature *= cooling_rate
#         if temperature < min_temperature:
#             break

#     return pareto_set

# # Example usage
# initial_solution = [random.randint(0, 20) for _ in range(25)]  # Initial solution with random integers
# objective_functions = [f1, f2, f3, f4, f5, f6]
# pareto_front = pareto_simulated_annealing(objective_functions, initial_solution, max_iterations=1000, max_temperature=100, min_temperature=0.01, cooling_rate=0.95)

# productgroepen = ["Buitenkozijnen, -ramen, -deuren en -puien", "Lift", "Binnenkozijnen en deuren", 
#                   "Binnenwandafwerkingen", "Vloerafwerkingen", "Plafonds", "Sanitair", "Keuken", "Buitenwanden", 
#                  "Vloeren", "Daken", "Hoofddraagconstructie", "Na-isolatie binnen", "Riolering en HWA", "Terreininrichting", 
#                  "Verwarming en koeling", "Luchtbehandeling", "Vaste gebouwvoorzieningen", "Binnenwanden", 
#                  "Trappen en hellingen", "Luiken en vensters", "Balustrades en leuningen", "Warm- en koud water installaties", 
#                  "Elektrische installaties", "Beveiliging"]

# st.markdown("## Pareto Front:")
# i = 0
# for solution in pareto_front:
#     i = i + 1
#     j = 0
#     st.markdown(f"### Oplossing {i}")
#     for product in productgroepen:
#         st.markdown(f"Aantal producten in de productgroep {product} {solution[j]}")
#         j = j + 1
#     st.markdown(solution)
#     st.markdown("#### Objective Values:")
#     st.markdown(f"- aanschafkosten: {f1(solution)} ")
#     st.markdown(f"- onderhoudskosten: {f2(solution)}")
#     st.markdown(f"- mate van losmaakbaarheid: {f3(solution)}")
#     st.markdown(f"- toepassingsmogelijkheden: {f4(solution)}")
#     st.markdown(f"- woonbeleving: {f5(solution)}")
#     st.markdown(f"- milieubelasting: {f6(solution)}")
#     st.markdown(f"- flexibiliteit tbv toekomstbestendigheid en innovatie: {f7(solution)}")
#     st.markdown(f"- mate van standaardisering: {f8(solution)}")


# In[ ]:


# def startoplossingen()
#     oplossingen = []
#     while len(oplossingen) < 10:
#         oplossing = [random.randint(0, 20) for _ in range(25)]
#         oplossingen.append(oplossing)


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

# In[16]:


def dominates(x, y):
    if x[0] <= y[0] and x[1] <= y[1] and x[2] >= y[2] and x[3] >= y[3] and x[4] >= y[4] and x[5] <= y[5] and x[6] >= y[6] and x[7] >= y[7] and (x[0] < y[0] or x[1] < y[1] or x[2] > y[2] or x[3] > y[3] or x[4] > y[4] or x[5] < y[5] or x[6] > y[6] or x[7] > y[7]):
        st.markdown(x[0])
        st.markdown(y[0])
        st.markdown(f"is {x[0]} kleiner of gelijk aan {y[0]} {x[0] <= y[0]}")
        st.markdown(x[0] < y[0])

        st.markdown(x[1])
        st.markdown(y[1])
        st.markdown(f"is {x[1]} kleiner of gelijk aan {y[1]} {x[1] <= y[1]}")
        st.markdown(x[1] < y[1])

        st.markdown(x[2])
        st.markdown(y[2])
        st.markdown(f"is {x[2]} groter of gelijk aan {y[2]} {x[2] >= y[2]}")
        st.markdown(x[2] > y[2])

        st.markdown(x[3])
        st.markdown(y[3])
        st.markdown(f"is {x[3]} groter of gelijk aan {y[3]} {x[3] >= y[3]}")
        st.markdown(x[3] > y[3])

        st.markdown(x[4])
        st.markdown(y[4])
        st.markdown(f"is {x[4]} groter of gelijk aan {y[4]} {x[4] >= y[4]}")
        st.markdown(x[4] > y[4])

        st.markdown(x[5])
        st.markdown(y[5])
        st.markdown(f"is {x[5]} kleiner of gelijk aan {y[5]} {x[5] <= y[5]}")
        st.markdown(x[5] < y[5])

        st.markdown(x[6])
        st.markdown(y[6])
        st.markdown(f"is {x[6]} groter of gelijk aan {y[6]} {x[6] >= y[6]}")
        st.markdown(x[6] > y[6])

        st.markdown(x[7])
        st.markdown(y[7])
        st.markdown(f"is {x[7]} groter of gelijk aan {y[7]} {x[7] >= y[7]}")
        st.markdown(x[7] > y[7])
        st.markdown("---")
    

    return x[0] <= y[0] and x[1] <= y[1] and x[2] >= y[2] and x[3] >= y[3] and x[4] >= y[4] and x[5] <= y[5] and x[6] >= y[6] and x[7] >= y[7] and (x[0] < y[0] or x[1] < y[1] or x[2] > y[2] or x[3] > y[3] or x[4] > y[4] or x[5] < y[5] or x[6] > y[6] or x[7] > y[7])


# In[15]:


def f1(x):
    result = 6*x[0] + 9*x[1] + 2*x[2] + 7*x[3] + 4*x[4] + 4*x[5] + 6*x[6] + x[7] + 4*x[8] + 7*x[9] + 9*x[10] + 10*x[11] + 4*x[12] + 2*x[13] + 6*x[14] + 6*x[15] + 2*x[16] + x[17] + 5*x[18] + 4*x[19] + 4*x[20] + 10*x[21] + 2*x[22] + 2.5*x[23] + 9*x[24]
    return result 

def f2(x):
    result = 4.5*x[0] + 2*x[1] + 6*x[2] + 4*x[3] + 4*x[4] + 5*x[5] + 10*x[6] + 3*x[7] + 6*x[8] + x[9] + x[10] + x[11] + 4*x[12] + 9*x[13] + 7.5*x[14] + 4*x[15] + 2*x[16] + x[17] + 3*x[18] + 4*x[19] + 3*x[20] + 2.5*x[21] + 4*x[22] + 6*x[23] + 5*x[24]
    return result 

def f3(x):
    result = 9.5*x[0] + 3*x[1] + 9*x[2] + 4.5*x[3] + x[4] + 3*x[5] + 9*x[6] + 9*x[7] + 4*x[8] + 6*x[9] + 8*x[10] + 2*x[11] + 9*x[12] + 4*x[13] + 6*x[14] + 6*x[15] + 4*x[16] + 6*x[17] + 7*x[18] + 4*x[19] + 6*x[20] + 6*x[21] + 8*x[22] + 7*x[23] + 4*x[24]
    return result 

def f4(x):
    result = 8*x[0] + 2.5*x[1] + 8*x[2] + 5*x[3] + 6*x[4] + 3*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 7*x[10] + 7.5*x[11] + 8*x[12] + 6*x[13] + 6*x[14] + 4*x[15] + 7*x[16] + 7*x[17] + 7*x[18] + 4*x[19] + 4*x[20] + 7.5*x[21] + 6*x[22] + 5*x[23] + 3*x[24]
    return result 

def f5(x):
    result = 9.5*x[0] + 10*x[1] + 4*x[2] + 8*x[3] + 6*x[4] + 7*x[5] + 6*x[6] + 8*x[7] + 6.5*x[8] + 4*x[9] + x[10] + 5*x[11] + 5*x[12] + 4*x[13] + 8*x[14] + 6*x[15] + 6*x[16] + 6*x[17] + 8*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 2*x[22] + 4*x[23] + 6*x[24]
    return result 

def f6(x):
    result = 7.5*x[0] + 7.5*x[1] + 8*x[2] + 7.5*x[3] + 6*x[4] + 7.5*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 4*x[10] + 2*x[11] + 5*x[12] + 2.5*x[13] + 6*x[14] + 3*x[15] + 8*x[16] + 8*x[17] + 6*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 7*x[22] + 5*x[23] + 6*x[24]
    return result 

def f7(x):
    result = 4*x[0] + x[1] + 4*x[2] + 2*x[3] + 6*x[4] + 3*x[5] + x[6] + 4*x[7] + 4*x[8] + 4*x[9] + 2*x[10] + 4*x[11] + 6*x[12] + 2.5*x[13] + 3*x[14] + 2.5*x[15] + 4*x[16] + 4*x[17] + 4*x[18] + x[19] + 3*x[20] + 4*x[21] + 4*x[22] + 2.5*x[23] + 4*x[24]
    return result 

def f8(x):
    result = 4*x[0] + x[1] + 9*x[2] + 8*x[3] + 5*x[4] + 6*x[5] + 9*x[6] + 9*x[7] + 6*x[8] + 4*x[9] + 2*x[10] + x[11] + x[12] + 5*x[13] + 2*x[14] + 2*x[15] + 8*x[16] + 6*x[17] + 7*x[18] + 2.5*x[19] + 4*x[20] + 2*x[21] + 4*x[22] + 7*x[23] + 3*x[24]
    return result 

def uitkomsten(oplossing):
    # Controleer of aanschafprijs en onderhoudskosten binnen het budget vallen
    if f1(oplossing) + f2(oplossing) <= st.session_state.budget:
#         aanschafprijs = st.session_state.aanschafprijs * f1(oplossing)
#         onderhoudsprijs = st.session_state.onderhoudsprijs * f2(oplossing)
#         losmaakbaarheid = st.session_state.losmaakbaarheid * f3(oplossing)
#         toepassingsmogelijkheden = st.session_state.toepassingsmogelijkheden * f4(oplossing)
#         woonbeleving = st.session_state.woonbeleving * f5(oplossing)
#         milieubelasting = st.session_state.milieubelasting * f6(oplossing)
#         flexibiliteit = st.session_state.flexibiliteit * f7(oplossing)
#         standaardisering = st.session_state.standaardisering * f8(oplossing)

        aanschafprijs = f1(oplossing)
        onderhoudsprijs = f2(oplossing)
        losmaakbaarheid = f3(oplossing)
        toepassingsmogelijkheden = f4(oplossing)
        woonbeleving = f5(oplossing)
        milieubelasting = f6(oplossing)
        flexibiliteit = f7(oplossing)
        standaardisering = f8(oplossing)
        
        return -aanschafprijs - onderhoudsprijs + losmaakbaarheid + toepassingsmogelijkheden + woonbeleving - milieubelasting + flexibiliteit + standaardisering
    else:
        # Als aanschafprijs + onderhoudskosten hoger zijn dan het budget, retourneer een grote negatieve waarde
        return -float('inf')

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
    
    oplossing = [random.randint(0, 200) for _ in range(25)]
    for _ in range(9):
        nieuwe_oplossing = [random.randint(0, 20) for _ in range(25)]
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
                    
        nieuwe_uitkomsten = [f1(nieuwe_oplossing), f2(nieuwe_oplossing), f3(nieuwe_oplossing), f4(nieuwe_oplossing), f5(nieuwe_oplossing), f6(nieuwe_oplossing), f7(nieuwe_oplossing), f8(nieuwe_oplossing)]
        dominated = False
        for sol in populatie:
            if dominates(nieuwe_uitkomsten, [f1(sol), f2(sol), f3(sol), f4(sol), f5(sol), f6(sol), f7(sol), f8(sol)]):
                st.markdown(f"nieuwe {nieuwe_oplossing} dominates een oude {sol}")
                populatie.remove(sol)
            if dominates([f1(sol), f2(sol), f3(sol), f4(sol), f5(sol), f6(sol), f7(sol), f8(sol)], nieuwe_uitkomsten):
                st.markdown(f"oude {sol} dominates de nieuwe {nieuwe_oplossing}")
                dominated = True
                break
        if not dominated:
            populatie.append(nieuwe_oplossing)
    
    for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), uitkomsten(populatie[x]))
    populatie.sort(key=lambda uitkomst: uitkomst[1], reverse = True)
    st.markdown(populatie)

    return populatie


# In[ ]:


def ouders_maken(populatie):
    ouders = []
    beste = [i for i in populatie[0:5]]
    slechtste = [i for i in populatie[5:]] 
    i = 0
    while i < 4:    
        ouders.append(random.choice(beste))
        i = i + 1

    j = 0
    while j < 2:
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
test = [tuple(i[0]) for i in startpopulatie]


for i in range(len(test)):
    st.markdown(test[i])
    st.markdown(f"f1 {f1(test[i])}")
    st.markdown(f"f2 {f2(test[i])}")
    st.markdown(f"f3 {f3(test[i])}")
    st.markdown(f"f4 {f4(test[i])}")
    st.markdown(f"f5 {f5(test[i])}")
    st.markdown(f"f6 {f6(test[i])}")
    st.markdown(f"f7 {f7(test[i])}")
    st.markdown(f"f8 {f8(test[i])}")
iteraties = 0
while iteraties < 5:
    populatie = [tuple(i[0]) for i in startpopulatie]
    ouders = ouders_maken(populatie)
    populatie = [i for i in populatie[0:4]]
    kinderen = kinderen_maken(ouders)
    for a in kinderen:
        populatie.append(tuple(a))
    for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), uitkomsten(populatie[x]))
    populatie.sort(key=lambda uitkomst: uitkomst[1], reverse = True)
    iteraties = iteraties + 1


# In[ ]:


st.markdown("### Genetic algorithm:")
i = 0
st.markdown(populatie)

populatie = [tuple(i[0]) for i in populatie]

for x in range(len(populatie)):
        populatie[x] = (list(populatie[x]), f1(populatie[x]), f2(populatie[x]), f3(populatie[x]), f4(populatie[x]), f5(populatie[x]), f7(populatie[x]), f8(populatie[x]))

if st.session_state.doelstelling == 'Aanschafprijs':
    populatie.sort(key=lambda aanschafprijs: aanschafprijs[1])
if st.session_state.doelstelling == 'Onderhoudsprijs':
    populatie.sort(key=lambda onderhoudsprijs: onderhoudsprijs[2])
if st.session_state.doelstelling == 'Mate van losmaakbaarheid':
    populatie.sort(key=lambda losmaakbaarheid: losmaakbaarheid[3], reverse=True)
if st.session_state.doelstelling == 'Toepassingsmogelijkheden':
    populatie.sort(key=lambda toepassingsmogelijkheden: toepassingsmogelijkheden[4], reverse=True)
if st.session_state.doelstelling == 'Woonbeleving':
    populatie.sort(key=lambda woonbeleving: woonbeleving[5], reverse=True)
if st.session_state.doelstelling == 'Milieubelasting':
    populatie.sort(key=lambda milieubelasting: milieubelasting[6])
if st.session_state.doelstelling == 'Flexibiliteit tbv toekomstbestendigheid en innovatie':
    populatie.sort(key=lambda flexibiliteit: flexibiliteit[7], reverse=True)
if st.session_state.doelstelling == 'Mate van standaardisering':
    populatie.sort(key=lambda standaardisering: standaardisering[8], reverse=True)
    
populatie = [tuple(i[0]) for i in populatie]

    
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
    st.markdown(f"- onderhoudskosten: {f2(solution)}")
    st.markdown(f"- mate van losmaakbaarheid: {f3(solution)}")
    st.markdown(f"- toepassingsmogelijkheden: {f4(solution)}")
    st.markdown(f"- woonbeleving: {f5(solution)}")
    st.markdown(f"- milieubelasting: {f6(solution)}")
    st.markdown(f"- flexibiliteit tbv toekomstbestendigheid en innovatie: {f7(solution)}")
    st.markdown(f"- mate van standaardisering: {f8(solution)}")


# In[ ]:


# def f1(x):
#     result = 6*x[0] + 9*x[1] + 2*x[2] + 7*x[3] + 4*x[4] + 4*x[5] + 6*x[6] + x[7] + 4*x[8] + 7*x[9] + 9*x[10] + 10*x[11] + 4*x[12] + 2*x[13] + 6*x[14] + 6*x[15] + 2*x[16] + x[17] + 5*x[18] + 4*x[19] + 4*x[20] + 10*x[21] + 2*x[22] + 2.5*x[23] + 9*x[24]
#     return result 

# def f2(x):
#     result = 4.5*x[0] + 2*x[1] + 6*x[2] + 4*x[3] + 4*x[4] + 5*x[5] + 10*x[6] + 3*x[7] + 6*x[8] + x[9] + x[10] + x[11] + 4*x[12] + 9*x[13] + 7.5*x[14] + 4*x[15] + 2*x[16] + x[17] + 3*x[18] + 4*x[19] + 3*x[20] + 2.5*x[21] + 4*x[22] + 6*x[23] + 5*x[24]
#     return result 

# def f3(x):
#     result = 9.5*x[0] + 3*x[1] + 9*x[2] + 4.5*x[3] + x[4] + 3*x[5] + 9*x[6] + 9*x[7] + 4*x[8] + 6*x[9] + 8*x[10] + 2*x[11] + 9*x[12] + 4*x[13] + 6*x[14] + 6*x[15] + 4*x[16] + 6*x[17] + 7*x[18] + 4*x[19] + 6*x[20] + 6*x[21] + 8*x[22] + 7*x[23] + 4*x[24]
#     return result 

# def f4(x):
#     result = 8*x[0] + 2.5*x[1] + 8*x[2] + 5*x[3] + 6*x[4] + 3*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 7*x[10] + 7.5*x[11] + 8*x[12] + 6*x[13] + 6*x[14] + 4*x[15] + 7*x[16] + 7*x[17] + 7*x[18] + 4*x[19] + 4*x[20] + 7.5*x[21] + 6*x[22] + 5*x[23] + 3*x[24]
#     return result 

# def f5(x):
#     result = 9.5*x[0] + 10*x[1] + 4*x[2] + 8*x[3] + 6*x[4] + 7*x[5] + 6*x[6] + 8*x[7] + 6.5*x[8] + 4*x[9] + x[10] + 5*x[11] + 5*x[12] + 4*x[13] + 8*x[14] + 6*x[15] + 6*x[16] + 6*x[17] + 8*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 2*x[22] + 4*x[23] + 6*x[24]
#     return result 

# def f6(x):
#     result = 7.5*x[0] + 7.5*x[1] + 8*x[2] + 7.5*x[3] + 6*x[4] + 7.5*x[5] + 8*x[6] + 8*x[7] + 6*x[8] + 7*x[9] + 4*x[10] + 2*x[11] + 5*x[12] + 2.5*x[13] + 6*x[14] + 3*x[15] + 8*x[16] + 8*x[17] + 6*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 7*x[22] + 5*x[23] + 6*x[24]
#     return result 

# def f7(x):
#     result = 4*x[0] + x[1] + 4*x[2] + 2*x[3] + 6*x[4] + 3*x[5] + x[6] + 4*x[7] + 4*x[8] + 4*x[9] + 2*x[10] + 4*x[11] + 6*x[12] + 2.5*x[13] + 3*x[14] + 2.5*x[15] + 4*x[16] + 4*x[17] + 4*x[18] + x[19] + 3*x[20] + 4*x[21] + 4*x[22] + 2.5*x[23] + 4*x[24]
#     return result 

# def f8(x):
#     result = 4*x[0] + x[1] + 9*x[2] + 8*x[3] + 5*x[4] + 6*x[5] + 9*x[6] + 9*x[7] + 6*x[8] + 4*x[9] + 2*x[10] + x[11] + x[12] + 5*x[13] + 2*x[14] + 2*x[15] + 8*x[16] + 6*x[17] + 7*x[18] + 2.5*x[19] + 4*x[20] + 2*x[21] + 4*x[22] + 7*x[23] + 3*x[24]
#     return result 

# def uitkomsten(oplossing):
#     # Controleer of aanschafprijs en onderhoudskosten binnen het budget vallen
#     if f1(oplossing) + f2(oplossing) <= st.session_state.budget:
# #         aanschafprijs = st.session_state.aanschafprijs * f1(oplossing)
# #         onderhoudsprijs = st.session_state.onderhoudsprijs * f2(oplossing)
# #         losmaakbaarheid = st.session_state.losmaakbaarheid * f3(oplossing)
# #         toepassingsmogelijkheden = st.session_state.toepassingsmogelijkheden * f4(oplossing)
# #         woonbeleving = st.session_state.woonbeleving * f5(oplossing)
# #         milieubelasting = st.session_state.milieubelasting * f6(oplossing)
# #         flexibiliteit = st.session_state.flexibiliteit * f7(oplossing)
# #         standaardisering = st.session_state.standaardisering * f8(oplossing)

#         aanschafprijs = f1(oplossing)
#         onderhoudsprijs = f2(oplossing)
#         losmaakbaarheid = f3(oplossing)
#         toepassingsmogelijkheden = f4(oplossing)
#         woonbeleving = f5(oplossing)
#         milieubelasting = f6(oplossing)
#         flexibiliteit = f7(oplossing)
#         standaardisering = f8(oplossing)
        
#         return -aanschafprijs - onderhoudsprijs + losmaakbaarheid + toepassingsmogelijkheden + woonbeleving - milieubelasting + flexibiliteit + standaardisering
#     else:
#         # Als aanschafprijs + onderhoudskosten hoger zijn dan het budget, retourneer een grote negatieve waarde
#         return -float('inf')

# def startoplossingen():
#     oplossingen = []
#     while len(oplossingen) < 10:
#         oplossing = [random.randint(0, 20) for _ in range(25)]
#         if st.session_state.fase == 'Budget te veel':
#             for i, s, m in zip(range(len(oplossing)), sessions, maximaal):
#                 if oplossing[i] < s:
#                     oplossing[i] = s
#                 elif oplossing[i] > m:
#                     oplossing[i] = m
#                 else:
#                     oplossing[i] = oplossing[i]
#         else:
#             for i, m in zip(range(len(oplossing)), minmax):
#                 if oplossing[i] < m[0]:
#                     oplossing[i] = m[0]
#                 elif oplossing[i] > m[1]:
#                     oplossing[i] = m[1]
#                 else:
#                     oplossing[i] = oplossing[i]
#         oplossingen.append((oplossing, uitkomsten(oplossing)))
#     oplossingen.sort(key=lambda uitkomsten: uitkomsten[1], reverse=True)
#     return oplossingen


# In[25]:


# import random
# import pandas as pd
# import streamlit as st

# def startoplossing():
#     startoplossing = [random.randint(0, 20) for _ in range(25)]
# #     if st.session_state.fase == 'Budget te veel':
# #         for i, s, m in zip(range(len(startoplossing)), sessions, maximaal):
# #             if startoplossing[i] < s:
# #                 startoplossing[i] = s
# #             elif startoplossing[i] > m:
# #                 startoplossing[i] = m
# #             else:
# #                 startoplossing[i] = startoplossing[i]
# #     else:
# #         for i, m in zip(range(len(startoplossing)), minmax):
# #             if startoplossing[i] < m[0]:
# #                 startoplossing[i] = m[0]
# #             elif startoplossing[i] > m[1]:
# #                 startoplossing[i] = m[1]
# #             else:
# #                 startoplossing[i] = startoplossing[i]
#     return startoplossing
                   
# def startpopulatie(startoplossing):
#     huidige_oplossing = startoplossing
    
#     populatie = [huidige_oplossing]
    
#     oplossing = [random.randint(0, 20) for _ in range(25)]
#     for _ in range(9):
#         nieuwe_oplossing = [random.randint(0, 20) for _ in range(25)]
# #         if st.session_state.fase == 'Budget te veel':
# #             for i, s, m in zip(range(len(nieuwe_oplossing)), sessions, maximaal):
# #                 if nieuwe_oplossing[i] < s:
# #                     nieuwe_oplossing[i] = s
# #                 elif nieuwe_oplossing[i] > m:
# #                     nieuwe_oplossing[i] = m
# #                 else:
# #                     nieuwe_oplossing[i] = nieuwe_oplossing[i]
# #         else:
# #             for i, m in zip(range(len(nieuwe_oplossing)), minmax):
# #                 if nieuwe_oplossing[i] < m[0]:
# #                     nieuwe_oplossing[i] = m[0]
# #                 elif nieuwe_oplossing[i] > m[1]:
# #                     nieuwe_oplossing[i] = m[1]
# #                 else:
# #                     nieuwe_oplossing[i] = nieuwe_oplossing[i]
                    
#         nieuwe_uitkomsten = [f1(nieuwe_oplossing), f2(nieuwe_oplossing), f3(nieuwe_oplossing), f4(nieuwe_oplossing), f5(nieuwe_oplossing), f6(nieuwe_oplossing), f7(nieuwe_oplossing), f8(nieuwe_oplossing)]
#         dominated = False
#         for sol in populatie:
#             if dominates(nieuwe_uitkomsten, [f1(sol), f2(sol), f3(sol), f4(sol), f5(sol), f6(sol), f7(sol), f8(sol)]):
#                 populatie.remove(sol)
#             if dominates([f1(sol), f2(sol), f3(sol), f4(sol), f5(sol), f6(sol), f7(sol), f8(sol)], nieuwe_uitkomsten):
#                 dominated = True
#                 break
#         if not dominated:
#             populatie.append(nieuwe_oplossing)
            
#     return populatie

# def uitkomst(oplossing):
#     aanschafprijs = f1(oplossing)
#     onderhoudsprijs = f2(oplossing)
#     losmaakbaarheid = f3(oplossing)
#     toepassingsmogelijkheden = f4(oplossing)
#     woonbeleving = f5(oplossing)
#     milieubelasting = f6(oplossing)
#     flexibiliteit = f7(oplossing)
#     standaardisering = f8(oplossing)

#     return -aanschafprijs - onderhoudsprijs + losmaakbaarheid + toepassingsmogelijkheden + woonbeleving - milieubelasting + flexibiliteit + standaardisering

# startoplossing = startoplossing()
# populatie = startpopulatie(startoplossing)
# for i in range(len(populatie)):
#     print(populatie[i])
#     print(f"f1 {f1(populatie[i])}")
#     print(f"f2 {f2(populatie[i])}")
#     print(f"f3 {f3(populatie[i])}")
#     print(f"f4 {f4(populatie[i])}")
#     print(f"f5 {f5(populatie[i])}")
#     print(f"f6 {f6(populatie[i])}")
#     print(f"f7 {f7(populatie[i])}")
#     print(f"f8 {f8(populatie[i])}")
#     print(uitkomst(populatie[i]))
#     print("")

