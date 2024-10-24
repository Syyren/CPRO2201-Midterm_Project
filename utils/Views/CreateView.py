#module that returns the partial create view

import streamlit as st

#function that defines the view when create is selected, allows user to make new task
def createView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio("Select type of task", (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")

        with st.form("reg_task_form"):
            title = st.text_input("Title"),
            description = st.text_input("Description")
            due_date = None
            show_optional = st.checkbox("Date?:")
            if show_optional:
                due_date = st.date_input("Please choose your task date.")
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write(f"Title: {title} Description: {description} Due Date: {due_date}")
        if st.checkbox("Date?"):
                due_date = st.date_input("Please choose your task date.")