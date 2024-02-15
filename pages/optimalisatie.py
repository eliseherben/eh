#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from menu import menu_with_redirect
menu_with_redirect()


# In[ ]:


st.title("Optimalisatie")


# In[1]:


import random
import math

# Define the objective functions
def f1(x, minimize=True):
    result = 6*x[0] + 9*x[1] + 2*x[2] + 7*x[3] + 4*x[4] + 4*x[5] + 6*x[6] + x[7] + 4*x[8] + 7*x[9] + 9*x[10] + 10*x[11] + 4*x[12] + 2*x[13] + 6*x[14] + 6*x[15] + 2*x[16] + x[17] + 5*x[18] + 4*x[19] + 4*x[20] + 10*x[21] + 2*x[22] + 2.5*x[23] + 9*x[24]
    return result if minimize else -result

def f2(x, minimize=True):
    result = 4.5*x[0] + 2*x[1] + 6*x[2] + 4*x[3] + 4*x[4] + 5*x[5] + 10*x[6] + 3*x[7] + 6*x[8] + x[9] + x[10] + x[11] + 4*x[12] + 9*x[13] + 7.5*x[14] + 4*x[15] + 2*x[16] + x[17] + 3*x[18] + 4*x[19] + 3*x[20] + 2.5*x[21] + 4*x[22] + 6*x[23] + 5*x[24]
    return result if minimize else -result

def f3(x, maximize=True):
    result = 9.5*x[0] + 3*x[1] + 9*x[2] + 4.5*x[3] + x[4] + 3*x[5] + 9*x[6] + 9*x[7] + 4*x[8] + 6*x[9] + 8*x[10] + 2*x[11] + 9*x[12] + 4*x[13] + 6*x[14] + 6*x[15] + 4*x[16] + 6*x[17] + 7*x[18] + 4*x[19] + 6*x[20] + 6*x[21] + 8*x[22] + 7*x[23] + 4*x[24]
    return result if maximize else -result

def f4(x, maximize=True):
    result = 9.5*x[0] + 10*x[1] + 4*x[2] + 8*x[3] + 6*x[4] + 7*x[5] + 6*x[6] + 8*x[7] + 6.5*x[8] + 4*x[9] + x[10] + 5*x[11] + 5*x[12] + 4*x[13] + 8*x[14] + 6*x[15] + 6*x[16] + 6*x[17] + 8*x[18] + 3*x[19] + 4*x[20] + 4*x[21] + 2*x[22] + 4*x[23] + 6*x[24]
    return result if maximize else -result
    
# Check if solution x dominates solution y
def dominates(x, y):
    return all(xi >= yi for xi, yi in zip(x, y)) and any(xi > yi for xi, yi in zip(x, y))

# Simulated annealing function
def pareto_simulated_annealing(objective_functions, initial_solution, max_iterations, max_temperature, min_temperature, cooling_rate):
    current_solution = initial_solution
    temperature = max_temperature

    pareto_set = [current_solution]

    for _ in range(max_iterations):
        new_solution = [current_solution[i] + random.randint(-1, 1) for i in range(25)]  # Perturb the current solution with random integers
        new_objectives = [objective(new_solution) for objective in objective_functions]
        dominated = False
        if (new_objectives[0] + new_objectives[1]) <= st.session_state.budget:
            for sol in pareto_set:
                if dominates(new_objectives, [objective(sol) for objective in objective_functions]):
                    pareto_set.remove(sol)
                if dominates([objective(sol) for objective in objective_functions], new_objectives):
                    dominated = True
                    break
            if not dominated:
                pareto_set.append(new_solution)

        temperature *= cooling_rate
        if temperature < min_temperature:
            break

    return pareto_set

# Example usage
initial_solution = [random.randint(0, 20) for _ in range(25)]  # Initial solution with random integers
objective_functions = [f1, f2, f3, f4]
pareto_front = pareto_simulated_annealing(objective_functions, initial_solution, max_iterations=1000, max_temperature=100, min_temperature=0.01, cooling_rate=0.95)

st.markdown("## Pareto Front:")
i = 0
for solution in pareto_front:
    i = i + 1
    st.markdown(f"### Oplossing {1}")
    st.markdown(solution)
    st.markdown("#### Objective Values:")
    st.markdown(f"- aanschafkosten: {f1(solution)} ")
    st.markdown(f"- onderhoudskosten: {f2(solution)}")
    st.markdown(f"- mate van losmaakbaarheid: {f3(solution)}")
    st.markdown(f"- woonbeleving: {f4(solution)}")



# In[ ]:


st.markdown(st.session_state.balustrades)
st.markdown(st.session_state.water)
st.markdown(st.session_state.isolatie)

