#module that's basically a confirmation window

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import deleteTask
from ..Controllers.PersonalTaskController import deletePersonalTask
from ..Controllers.WorkTaskController import deleteWorkTask

#pop up that prompts the user if they want to delete their task or not
@st.dialog("Delete")
def deleteView(task : Task, 
               task_type : str, 
               REG : str = "Regular",
               PER : str = "Personal",
               WOR : str = "Work"):
    st.write(f"Would you like to delete \"{task.getTitle()}\"?")
    btn = False
    if task_type == REG:
        btn = st.button("Yes", on_click=deleteTask, args=(task,))
    elif task_type == PER:
        btn = st.button("Yes", on_click=deletePersonalTask, args=(task,))
    elif task_type == WOR:
        btn = st.button("Yes", on_click=deleteWorkTask, args=(task,))
    if btn:
        st.rerun()