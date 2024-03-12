# -*- coding: utf-8 -*-
"""Inleiding

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TVSOjHS7mdyrTd2NFzp8hrJ-SKwIyFzj
"""

import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
from menu import menu


#pip install streamlit

st.title("Inleiding tool")
st.subheader("**Doelfuncties**")
st.markdown("**Variabelen**")
st.markdown("Xn = Het aandeel van productgroep n binnen het bouwproject")
st.markdown("X1 = Het aandeel van de productgroep buitenkozijnen, -ramen, -deuren en -puien")

st.markdown("**aanschafprijs**")
st.markdown("6 * x[0] + 9 * x[1] + 2 * x[2] + 7 * x[3] + 4 * x[4] + 4 * x[5] + 6 * x[6] + x[7] + 4 * x[8] + 7 * x[9] + "
            "9 * x[10] + 10 * x[11] + 4 * x[12] + 2 * x[13] + 6 * x[14] + 6 * x[15] + 2 * x[16] + x[17] + 5 * x[18] + "
            "4 * x[19] + 4 * x[20] + 10 * x[21] + 2 * x[22] + 2.5 * x[23] + 9 * x[24]")

labels = ["Buitenkozijnen, -ramen, -deuren en -puien", "Lift", "Binnenkozijnen en deuren",
                  "Binnenwandafwerkingen", "Vloerafwerkingen", "Plafonds", "Sanitair", "Keuken", "Buitenwanden",
                 "Vloeren", "Daken", "Hoofddraagconstructie", "Na-isolatie binnen", "Riolering en HWA", "Terreininrichting",
                 "Verwarming en koeling", "Luchtbehandeling", "Vaste gebouwvoorzieningen", "Binnenwanden",
                 "Trappen en hellingen", "Luiken en vensters", "Balustrades en leuningen", "Warm- en koud water installaties",
                 "Elektrische installaties", "Beveiliging"]
values = [10, 10, 8, 9, 4, 7, 6, 2, 4, 3, 2, 1, 2, 3, 4, 5, 3, 7, 3, 2, 1, 1, 1, 1, 1]
print(sum(values))

fig = px.pie(values=values, names=labels)
st.plotly_chart(fig)

