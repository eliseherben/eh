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
        st.sidebar.page_link("pages/binnenkozijnen.py", label="Lift")
        st.sidebar.page_link("pages/binnenwandafwerkingen.py", label="Lift")
        st.sidebar.page_link("pages/vloerafwerkingen.py", label="Lift")
        st.sidebar.page_link("pages/plafonds.py", label="Lift")
        st.sidebar.page_link("pages/sanitair.py", label="Lift")
        st.sidebar.page_link("pages/keuken.py", label="Lift")
        st.sidebar.page_link("pages/buitenwanden.py", label="Lift")
        st.sidebar.page_link("pages/vloeren.py", label="Lift")
        st.sidebar.page_link("pages/daken.py", label="Lift")
        st.sidebar.page_link("pages/hoofddraagconstructie.py", label="Lift")
        st.sidebar.page_link("pages/isolate.py", label="Lift")
        st.sidebar.page_link("pages/riolering.py", label="Lift")
        st.sidebar.page_link("pages/terreininrichting.py", label="Lift")
        st.sidebar.page_link("pages/verwarming.py", label="Lift")
        st.sidebar.page_link("pages/luchtbehandeling.py", label="Lift")
        st.sidebar.page_link("pages/gebouwvoorzieningen.py", label="Lift")
        st.sidebar.page_link("pages/binnenwanden.py", label="Lift")
        st.sidebar.page_link("pages/trappen.py", label="Lift")
        st.sidebar.page_link("pages/luiken.py", label="Lift")
        st.sidebar.page_link("pages/balustrades.py", label="Lift")
        st.sidebar.page_link("pages/water.py", label="Lift")
        st.sidebar.page_link("pages/elektra.py", label="Lift")
        st.sidebar.page_link("pages/beveiliging.py", label="Lift")

        
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

