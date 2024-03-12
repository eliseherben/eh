#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st


# In[ ]:


def authenticated_menu():

    # st.sidebar.page_link("inleiding.py", label = "Inleiding")
    
    st.sidebar.page_link("dashboard.py", label = "Introductie")
#     if st.session_state.project == 'Nieuwbouw woningen':
#         st.sidebar.page_link("pages/productgroepen.py", label = "Productgroepen")

#     if st.session_state.project == 'Renovatie':
#         st.sidebar.page_link("pages/productgroepen.py", label = "Productgroepen")
        
    if st.session_state.optimalisatie:
        st.sidebar.page_link("pages/2functies.py", label = "Optimalisatie")
        
    if st.session_state.fase == 'Begin fase':
        st.sidebar.page_link("pages/inleiding.py", label = "Inleiding")
        
    if st.session_state.fase == 'Budget te veel':
        st.sidebar.page_link("pages/implementeren.py", label = "Productgroepen")
        
    if st.session_state.fase == 'Budget te weinig':
        st.sidebar.page_link("pages/fase1.py", label = "Productgroepen")

def unauthenticated_menu():
    # st.sidebar.page_link("inleiding.py", label = "Inleiding")
    st.sidebar.page_link("dashboard.py", label = "Introductie")
        
def menu():
    if "project" not in st.session_state or st.session_state.project is None:
        unauthenticated_menu()
        return
    authenticated_menu()
    
def menu_with_redirect():
    if "project" not in st.session_state or st.session_state.project is None:
        st.switch_page("dashboard.py")
    menu()

