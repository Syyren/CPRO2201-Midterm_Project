#module that returns the partial create view

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import createTask
from ..Controllers.PersonalTaskController import createPersonalTask
from ..Controllers.WorkTaskController import createWorkTask

#function that defines the view when create is selected, allows user to make new task
def createView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio("Select type of task", (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")
        if task_type == REG:
            with st.form("reg_task_form"):
                title = st.text_input("Title"),
                description = st.text_input("Description")
                due_date = st.date_input("Please choose your task date.")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.write(f"Title: {title} Description: {description} Due Date: {due_date}")
        elif task_type == PER:
            with st.form("per_task_form"):
                title = st.text_input("Title"),
                description = st.text_input("Description")
                due_date = st.date_input("Please choose your task date.")
                submitted = st.form_submit_button("Submit")
                friend_slider = st.select_slider("How many friends will be there?", 0, 5, 0)
                friends = []
                for i in range(friend_slider):
                    friend_name = st.text_input(f"Friend {i + 1}'s Name")
                    friends.append(friend_name)
                if submitted:
                    st.write(f"Title: {title} Description: {description} Due Date: {due_date}")
                    if friends:
                        st.write("Friends:")
                        for friend in friends:
                            st.write(friend)
        elif task_type == WOR:
            with st.form("wor_task_form"):
                title = st.text_input("Title"),
                description = st.text_input("Description")
                due_date = st.date_input("Please choose your task date.")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.write(f"Title: {title} Description: {description} Due Date: {due_date}")