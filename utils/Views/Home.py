#module that establishes the "view" as we are using an application front end.

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

test_task1 = Task("Groceries", "Go to store: Eggs, Bacon, Celery")
test_task2 = Task("Finish Dishes", "Make sure they sparkle")

test_ptask1 = PersonalTask("See a Movie", "Go see the film", ["Jessica", "Charlie"])
test_ptask2 = PersonalTask("Date Night", "Going to dinner", ["Stevie"])

test_wtask1 = WorkTask("Finish Report", "Must do")
test_wtask2 = WorkTask("Meeting", "At the Casino", ["Rob"])

regular_tasks = [test_task1, test_task2]
personal_tasks = [test_ptask1, test_ptask2]
work_tasks = [test_wtask1, test_wtask2]

REG = "Regular"
PER = "Personal"
WOR = "Work"

def userLogin():
    st.session_state.clicked = True

def createView():
    left_column, right_column = st.columns([2, 1])
    
    with right_column:
        task_type = st.radio(
            "Select type of task",
            (REG, PER, WOR))
    
    with left_column:
        st.write(f"Please enter the details for your {task_type} task.")

def viewView():

    left_column, right_column = st.columns([2, 1])
        
    with right_column:
        
        task_types = st.multiselect("Tasks",
        options=[REG, PER, WOR],)
    
    with left_column:
        if len(task_types) > 0:
            tasks = []
            for task_type in task_types:
                if task_type == REG:
                    tasks.append(regular_tasks)
                elif task_type == PER:
                    tasks.append(personal_tasks)
                elif task_type == WOR:
                    tasks.append(work_tasks)
            st.write(f"Viewing details for your {task_types} tasks.")
            for task in tasks:
                if task is Task:
                    st.write(f"Task: {task.getTitle()}")
                    st.write(f"Description: {task.getDescription()}")
                elif task is PersonalTask:
                    st.write(f"Task: {task.getTitle()}")
                    st.write(f"Description: {task.getDescription()}")
                    if len(task.getFriends()) > 0:
                        st.write("Friends:")
                        for friend in task.getFriends():
                            st.write(f"- {friend}")
                elif task is WorkTask:
                    st.write(f"Task: {task.getTitle()}")
                    st.write(f"Description: {task.getDescription()}")
                    if len(task.getCollaborators()) > 0:
                        st.write("Collaborators")
                        for collaborator in task.getCollaborators():
                            st.write(f"- {collaborator}")

        else:
            st.write("Please select the type of tasks you'd like to view.")
    

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
                input_col, button_col = st.columns([4, 1])
                with input_col:
                    email = st.text_input("Email")
                with button_col:
                    st.markdown(
                    """
                    <style>
                    .stButton button {
                        margin-top: 10px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
        )
                    st.button("Login", on_click=userLogin)
    