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

