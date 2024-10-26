#module that returns the partial create view

import streamlit as st
import datetime
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import createTask
from ..Controllers.PersonalTaskController import createPersonalTask
from ..Controllers.WorkTaskController import createWorkTask
from ..Scripts.QOL import printList

def taskSubmitted(title : str, description : str, due_date : datetime):
    st.write(f"Task Submitted:")
    st.write(f"Title: {title}")
    st.write(f"Description: {description}")
    st.write(f"Due Date: {due_date}")

def formGenerator(form_name, 
                  date_check_text = "Is there a due date?",
                  title_txt = "Title*",
                  desc_txt = "Description",
                  due_txt = "Due Date",
                  submit_txt = "Submit",
                  PER = "Personal",
                  WOR = "Work"):
    date_check = st.checkbox(date_check_text)
    if form_name == PER:
        friend_slider = st.slider("Friends", 0, 5, 0)
    elif form_name == WOR:
        collaborator_slider = st.slider("Collaborators", 0, 8, 0)
    with st.form(f"{form_name}_Form"):
        title = st.text_input(title_txt),
        description = st.text_input(desc_txt)
        due_date = None
        if date_check:
            due_date = st.date_input(due_txt)
        if form_name == PER:
            friends = []
            for i in range(friend_slider):
                friend_name = st.text_input(f"Friend {i + 1}'s Name")
                if friend_name:
                    friends.append(friend_name)
        elif form_name == WOR:
            collaborators = []
            for i in range(collaborator_slider):
                collaborator_name = st.text_input(f"Collaborator {i + 1}'s Name")
                if collaborator_name:
                    collaborators.append(collaborator_name)
        submitted = st.form_submit_button(submit_txt)
        if submitted:
            taskSubmitted(title, description, due_date)
            if form_name == PER:
                if len(friends) > 0:
                    st.write(f"Friends: {printList(friends)}")
            elif form_name == WOR:
                if len(collaborators) > 0:
                    st.write(f"Collaborators: {printList(collaborators)}")

#function that defines the view when create is selected, allows user to make new task
def createView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio("Select type of task", (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")
        if task_type == REG:
            formGenerator(REG)
        elif task_type == PER:
            formGenerator(PER)
        elif task_type == WOR:
            formGenerator(WOR)