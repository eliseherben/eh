# -*- coding: utf-8 -*-
"""Opbouw.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WlvpuyevshddWkngPkbqDbm9rAZwQlBh
"""

import streamlit as st
import pandas as pd

streamlit.title("Eigen Haard")
tab1, tab2, tab3 = st.tabs(["Input", "Optimalisatie", "Aanpassingen"])

with tab1:
  st.markdown("**Soort project")
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
  st.number_input("Vul het budget in voor het huidige project", value=None, placeholder="Typ een bedrag", key="_budget", on_change=set_budget)

  st.markdown("**Wegingen**")
  st.markdown("Hieronder kan er per thema aangegeven worden of deze zwaarder of minder zwaar meeweegt tijdens dit project."
   "Als een thema neutraal is kan deze op '0' blijven staan. Als een thema zwaader meeweegt kan deze op +1 of +2 staan, "
   "als een thema minder zwaar meeweegt kan deze op -1 of -2 gezet worden. ")
  st.number_input("Vul de weging in voor het thema 'Woonbeleving' in dit project", value=0, min_value = -2, max_value = 2")
  st.number_input("Vul de weging in voor het thema 'Duurzaam' in dit project", value=0, min_value = -2, max_value = 2")
  st.number_input("Vul de weging in voor het thema 'Prijs' in dit project", value=0, min_value = -2, max_value = 2")