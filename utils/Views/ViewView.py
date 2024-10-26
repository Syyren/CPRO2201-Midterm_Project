#module that returns the partial view view

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import getAllTasks
from ..Controllers.PersonalTaskController import getAllPersonalTasks
from ..Controllers.WorkTaskController import getAllWorkTasks
from ..Scripts.QOL import printList, taskPrint, applyCSS

#function that defines the view when view task is selected, allows user to view and delete their tasks
def viewView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    applyCSS()
    regular_tasks = getAllTasks()
    personal_tasks = getAllPersonalTasks()
    work_tasks = getAllWorkTasks()

    left_column, right_column = st.columns([1, 2])

    with left_column:
        task_types = st.multiselect("Tasks", options=[REG, PER, WOR],)
    
    with right_column:
        if len(task_types) > 0:
            #clears the list after every refresh
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
                taskPrint(type_list)
        else:
            st.write("Please select the type of tasks you'd like to view.")