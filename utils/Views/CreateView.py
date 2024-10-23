import streamlit as st

#function that defines the view when create is selected, allows user to make new task
def createView():
    REG = "Regular"
    PER = "Personal"
    WOR = "Work"
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio(
            "Select type of task",
            (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")