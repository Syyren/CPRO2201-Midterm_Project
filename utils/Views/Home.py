#module that establishes the "view" as we are using an application front end.

import streamlit as st
from ..Models.Task import Task

test_task = Task("Groceries", "Go to store: Eggs, Bacon, Celery")

def testDisplay():
    if st.checkbox('Show message'):
        st.write(f'Task: {test_task.getTitle()}')
        st.write(f'Description: {test_task.getDescription()}')