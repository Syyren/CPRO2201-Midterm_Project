#module that establishes the "view" as we are using an application front end.

import streamlit as st
from ..Models.Task import Task

test_task = Task("Groceries", "Go to store: Eggs, Bacon, Celery")

def testDisplay():

    sidebar = st.sidebar.title("Task Menu")
    option = st.sidebar.selectbox("Choose an option", ["Create Task", "View Tasks"])

    left_column, right_column = st.columns(2)

    with left_column:
        st.button('Press me!')

    with right_column:
        task_type = st.radio(
            "Type of Task",
            ("Regular", "Personal", "Work"))
    st.write(f"Please enter the details for your {task_type} task!")
    if st.checkbox('Show message'):
        st.write(f'Task: {test_task.getTitle()}')
        st.write(f'Description: {test_task.getDescription()}')
    