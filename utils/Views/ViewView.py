#module that returns the partial view view

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Scripts.QOL import printList, taskPrint, applyCSS

#simulating the methods from the controller to get a list of the user's various tasks
def getTasks():
    test_task1 = Task("Groceries", "Go to store: Eggs, Bacon, Celery")
    test_task2 = Task("Finish Dishes", "Make sure they sparkle")
    test_task1.setDueDate(2024, 10, 24, 4, 30)
    regular_tasks = [test_task1, test_task2]
    return regular_tasks

def getPersonalTasks():
    test_task1 = PersonalTask("See a Movie", "Go see the film", ["Jessica", "Charlie", "Beffica"])
    test_task2 = PersonalTask("Date Night", "Going to dinner", ["Stevie"])
    personal_tasks = [test_task1, test_task2]
    return personal_tasks

def getWorkTasks():
    test_task1 = WorkTask("Finish Report", "Must do", ["Ben", "Corey", "Shirley", "Jeff", "Cameron"])
    test_task2 = WorkTask("Meeting", "At the Casino", ["Rob"])
    work_tasks = [test_task1, test_task2]
    return work_tasks

#function that defines the view when view task is selected, allows user to view and delete their tasks
def viewView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    applyCSS()
    regular_tasks = getTasks()
    personal_tasks = getPersonalTasks()
    work_tasks = getWorkTasks()

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