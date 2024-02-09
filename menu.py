#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# In[ ]:


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("dashboard.py", label="Introductie")
    if st.session_state.project == 'Nieuwbouw woningen':
        st.sidebar.page_link("pages/buitenkozijnen.py", label="Buitenkozijnen, -ramen, -deuren en -puien")
        st.sidebar.page_link("pages/lift.py", label="Lift")
        st.sidebar.page_link("pages/binnenkozijnen.py", label="Binnenkozijnen en deuren")
        st.sidebar.page_link("pages/binnenwandafwerkingen.py", label="Binnenwandafwerkingen")
        st.sidebar.page_link("pages/vloerafwerkingen.py", label="Vloerafwerkingen")
        st.sidebar.page_link("pages/plafonds.py", label="Plafonds")
        st.sidebar.page_link("pages/sanitair.py", label="Sanitair")
        st.sidebar.page_link("pages/keuken.py", label="Keuken")
        st.sidebar.page_link("pages/buitenwanden.py", label="Buitenwanden")
        st.sidebar.page_link("pages/vloeren.py", label="Vloeren")
        st.sidebar.page_link("pages/daken.py", label="Daken")
        st.sidebar.page_link("pages/hoofddraagconstructie.py", label="Hoofddraagconstructie")
        st.sidebar.page_link("pages/isolatie.py", label="Na-isolatie binnen")
        st.sidebar.page_link("pages/riolering.py", label="Riolering en HWA")
        st.sidebar.page_link("pages/terreininrichting.py", label="Terreininrichting")
        st.sidebar.page_link("pages/verwarming.py", label="Verwarming en koeling")
        st.sidebar.page_link("pages/luchtbehandeling.py", label="Luchtbehandeling")
        st.sidebar.page_link("pages/gebouwvoorzieningen.py", label="Vaste gebouwvoorzieningen")
        st.sidebar.page_link("pages/binnenwanden.py", label="Binnenwanden")
        st.sidebar.page_link("pages/trappen.py", label="Trappen en hellingen")
        st.sidebar.page_link("pages/luiken.py", label="Luiken en vensters")
        st.sidebar.page_link("pages/balustrades.py", label="Balustrades en leuningen")
        st.sidebar.page_link("pages/water.py", label="Warm- en koud water installaties")
        st.sidebar.page_link("pages/elektra.py", label="Elektrische installaties")
        st.sidebar.page_link("pages/beveiliging.py", label="Beveiliging")
        
    if st.session_state.project == 'Renovatie':
        st.sidebar.page_link("pages/productgroepen.py", label="Productgroepen")

        
def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("dashboard.py", label="Introductie")
        
def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "project" not in st.session_state or st.session_state.project is None:
        unauthenticated_menu()
        return
    authenticated_menu()
    
def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "project" not in st.session_state or st.session_state.project is None:
        st.switch_page("dashboard.py")
    menu()

