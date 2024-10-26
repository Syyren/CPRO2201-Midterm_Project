#module that establishes the "view" as we are using an application front end.

import streamlit as st
from .ViewView import viewView
from .CreateView import createView

#function that will log in a user to access the tasks page. Currently, just sets a session state to true.
def userLogin():
    st.session_state.clicked = True
    
#function that defines the main display for the application, displays a login screen until user logs in
def mainDisplay():
    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
        
    if st.session_state.clicked:
        create_task = "Create Task"
        view_tasks = "View Tasks"
        sidebar = st.sidebar.title("Task Menu")
        option = st.sidebar.selectbox("Please select an option:", [create_task, view_tasks])
        if option == create_task:
            createView()
        elif option == view_tasks:
            viewView()
    else:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
                st.write("Thank you for choosing TaskMan!")
                email = st.text_input("Email")
                st.button("Login", on_click=userLogin)
    