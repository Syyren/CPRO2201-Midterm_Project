#file for scripts that do convenient things

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

#function that applies CSS to
def applyCSS():
    with open("utils/Views/ViewViewStyle.css") as stylesheet:
        css = stylesheet.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

#function that writes details for a regular task
def printRegTask(task : Task):
    st.markdown(f'''
    <div class="card">
        <p class="title">{task.getTitle()}</p>
        <p>{task.getDescription()}</p>
        <p>Created on: {task.getCreationDate().strftime("%a, %b %d, %Y at %I:%M%p")}</p>
    </div>
    ''', unsafe_allow_html=True)

#function that writes details for a personal task
def printPersonalTask(task : PersonalTask):
    friends = ""
    if len(task.getFriends()) > 0:
            friends = f"<p>Friends: {printList(task.getFriends())}</p>"
    st.markdown(f'''
    <div class="card">
        <p class="title">{task.getTitle()}</p>
        <p>{task.getDescription()}</p>
        {friends}
    </div>
    ''', unsafe_allow_html=True)

#function that writes details for a work task
def printWorkTask(task : WorkTask):
    collaborators = ""
    if len(task.getCollaborators()) > 0:
            collaborators = f"<p>Collaborators: {printList(task.getCollaborators())}</p>"
    st.markdown(f'''
    <div class="card">
        <p class="title">{task.getTitle()}</p>
        <p>{task.getDescription()}</p>
        {collaborators}
    </div>
    ''', unsafe_allow_html=True)

#function that checks a list and then prints the tasks accordingly
def taskPrint(type_list : list):
    if len(type_list) == 0:
        st.error("No tasks available")
        print("Selected empty list")
    elif type(type_list[0]) is Task:
        for task in type_list:
            printRegTask(task)
            print(f"Regular task pulled: {task.getTitle()}")
    elif type(type_list[0]) is PersonalTask:
        for task in type_list:
            printPersonalTask(task)
            print(f"Personal task pulled: {task.getTitle()}")
    elif type(type_list[0]) is WorkTask:
        for task in type_list:
            printWorkTask(task)
            print(f"Work task pulled: {task.getTitle()}")

#function that prints a list in a nice readable way
def printList(list : list):
    string = ""
    for index, item in enumerate(list):
        if len(list) == 1:
            string = item
        else:
            if index > 0 and index == (len(list) - 1):
                string += " and "
            elif index > 0:
                string += ", "
            string += item
    return string