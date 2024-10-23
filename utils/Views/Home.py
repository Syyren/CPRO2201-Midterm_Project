#module that establishes the "view" as we are using an application front end.

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

REG = "Regular"
PER = "Personal"
WOR = "Work"

test_task1 = Task("Groceries", "Go to store: Eggs, Bacon, Celery")
test_task2 = Task("Finish Dishes", "Make sure they sparkle")

test_ptask1 = PersonalTask("See a Movie", "Go see the film", ["Jessica", "Charlie"])
test_ptask2 = PersonalTask("Date Night", "Going to dinner", ["Stevie"])

test_wtask1 = WorkTask("Finish Report", "Must do")
test_wtask2 = WorkTask("Meeting", "At the Casino", ["Rob"])

regular_tasks = [test_task1, test_task2]
personal_tasks = [test_ptask1, test_ptask2]
work_tasks = [test_wtask1, test_wtask2]

#function that will log in a user to access the tasks page. Currently, just sets a session state to true.
def userLogin():
    st.session_state.clicked = True

#function that writes details for a regular task
def printRegTask(task : Task):
    st.write(f"Task: {task.getTitle()}")
    st.write(f"Description: {task.getDescription()}")

#function that writes details for a personal task
def printPersonalTask(task : PersonalTask):
    st.write(f"Task: {task.getTitle()}")
    st.write(f"Description: {task.getDescription()}")
    if len(task.getFriends()) > 0:
        st.write(f"Friends: {printList(task.getFriends())}")

#function that writes details for a work task
def printWorkTask(task : WorkTask):
    st.write(f"Task: {task.getTitle()}")
    st.write(f"Description: {task.getDescription()}")
    if len(task.getCollaborators()) > 0:
        st.write(f"Collaborators: {printList(task.getCollaborators())}")

#function that prints a list in a nice readable way
def printList(list : list):
    string = ""
    for index, item in enumerate(list):
        if len(list) == 1:
            string = item
        else:
            if index > 0 and index == len(list) - 1:
                string += " and "
            elif index > 0:
                string += ", "
            string += item
    return string

#function that defines the view when create is selected, allows user to make new task
def createView():
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio(
            "Select type of task",
            (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")
        
#function that defines the view when view task is selected, allows user to view and delete their tasks
def viewView():

    left_column, right_column = st.columns([1, 2])

    with left_column:
        task_types = st.multiselect("Tasks",
        options=[REG, PER, WOR],)
    
    with right_column:
        if len(task_types) > 0:
            task_list = []
            for task_type in task_types:
                if task_type == REG:
                    task_list.append(regular_tasks)
                elif task_type == PER:
                    task_list.append(personal_tasks)
                elif task_type == WOR:
                    task_list.append(work_tasks)
            st.write(f"Viewing details for your {printList(task_types)} tasks.")
            for type_list in task_list:
                if isinstance(type_list[0], Task):
                    for task in type_list:
                        printRegTask(task)
                if isinstance(type_list[0], PersonalTask):
                    for task in type_list:
                        printPersonalTask(task)
                if isinstance(type_list[0], WorkTask):
                    for task in type_list:
                        printWorkTask(task)
        else:
            st.write("Please select the type of tasks you'd like to view.")
    
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
    