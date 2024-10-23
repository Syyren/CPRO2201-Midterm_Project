#file for scripts that do convenient things

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

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

def taskPrint(type_list : list):
    if len(type_list) == 0:
        print("Empty List")
    elif type(type_list[0]) is Task:
        for task in type_list:
            printRegTask(task)
    elif type(type_list[0]) is PersonalTask:
        for task in type_list:
            printPersonalTask(task)
    elif type(type_list[0]) is WorkTask:
        for task in type_list:
            printWorkTask(task)

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