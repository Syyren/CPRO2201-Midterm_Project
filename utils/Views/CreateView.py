#module that returns the partial create view

import streamlit as st
from datetime import datetime
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import createTask
from ..Controllers.PersonalTaskController import createPersonalTask
from ..Controllers.WorkTaskController import createWorkTask
from ..Scripts.QOL import printList

#dialogue window that pops up to notify the user the task is submitted
@st.dialog("Submission Successful")
def success(task_title : str):
    st.write(f"Task with title: {task_title} was created successfully.")
    btn = st.button("OK", )
    if btn:
        st.rerun()

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

#generates the form for the user to fill out depending on what they
def formGenerator(form_name, 
                  date_check_text = "Set a due date?",
                  title_txt = "Title*",
                  desc_txt = "Description",
                  due_txt = "Date",
                  time_txt = "Time",
                  submit_txt = "Submit",
                  REG = "Regular", PER = "Personal", WOR = "Work"):
    #declaring the checkbox to be on when the form is initialized
    date_check = st.checkbox(date_check_text, value=True)
    #checking the form type and dynamically generating elements based on the type
    if form_name == PER:
        friend_slider = st.slider("Friends", 0, 5, 0)
    elif form_name == WOR:
        collaborator_slider = st.slider("Collaborators", 0, 8, 0)
    with st.form(f"{form_name}_Form"):
        title = st.text_input(title_txt)
        description = st.text_input(desc_txt)
        #determining more elements based on whether the user wants to include a date or not
        due = None
        if date_check:
            due_date = st.date_input(due_txt)
            due_time = st.time_input(time_txt)
            due = datetime.combine(due_date, due_time)
        #generating fields based off a slider for friends/collaborators
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
            len_hour = st.slider("Hours", 0, 12, 0)
            len_mins = st.slider("Minutes", 0, 60, 0)
        submitted = st.form_submit_button(submit_txt)
        #this triggers once the submit button is launched
        if submitted:
            #error handling
            if title == "":
                st.error("Title can't be blank!")
                return
            #creating the various tasks based on the type they are using the form name variable
            #Regular Task
            elif form_name == REG:
                task = Task(title, description)
                if due:
                    task.setDueDate(due)
                createTask(task)
            #Personal Task
            elif form_name == PER:
                task = PersonalTask(title, description)
                if len(friends) > 0:
                    task.setFriends(friends)
                if due:
                    task.setDueDate(due)
                createPersonalTask(task)
            #Work Task
            elif form_name == WOR:
                task = WorkTask(title, description)
                if len(collaborators) > 0:
                    task.setCollaborators(collaborators)
                if due:
                    task.setDueDate(due)
                task.setLengthWithValues(len_hour, len_mins)
                createWorkTask(task)
            #displays a confirmation pop up that it fully executed
            success(task.getTitle())