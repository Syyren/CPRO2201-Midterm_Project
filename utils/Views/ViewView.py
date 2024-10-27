#module that returns the partial view view

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import getAllTasks
from ..Controllers.PersonalTaskController import getAllPersonalTasks
from ..Controllers.WorkTaskController import getAllWorkTasks
from .EditView import editView
from ..Scripts.QOL import applyCSS, cancelButton, printList

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

def deleteTask(task: Task):
    st.write(f"Are you sure you would like to delete \"{task.getTitle()}\"?")

#returns a string that's formatted depending on the type of task
def taskString(task : Task, extra_data : str = "<p></p>"):
    due_date = "<p>Due: No date assigned.</p>"
    if task.getDueDate() != None:
        due_date = f"<p>Due: {task.getDueDate().strftime("%a, %b %d, %Y at %I:%M%p")}</p>"
    string = f'''
    <div class="card">
        <p class="title">{task.getTitle()}</p>
        <p>\"{task.getDescription()}\"</p>
        {extra_data}
        {due_date}
        <p class="created">Created on: {task.getCreationDate().strftime("%a, %b %d, %Y at %I:%M%p")}</p>
    </div>
    '''
    return string

def taskLayout(task_type : str, type_list : list):
    for task in type_list:
        col1, col2 = st.columns([1,1])
        with col1:
            edit = st.button(f"Edit {task.getTitle()}", key=f"checkbox_{hash(task.getId())}")
        if edit:
            with col2:
                edit = cancelButton(task)
            editView(task, task_type)
        else:
            taskDisplay(task, task_type)
            print(f"{task_type} task pulled: {task.getTitle()}")

#function that writes details for a task
def taskDisplay(task : Task, task_type : str):
    REG = "Regular"
    PER = "Personal"
    WOR = "Work"
    if task_type == REG:
        st.markdown(taskString(task), unsafe_allow_html=True)
    elif task_type == PER:
        friends = ""
        if len(task.getFriends()) > 0:
            friends = f"<p>With: {printList(task.getFriends())}</p>"
        st.markdown(taskString(task, friends), unsafe_allow_html=True)
    elif task_type == WOR:
        collaborators = ""
        if len(task.getCollaborators()) > 0:
                collaborators = f"<p>Collaborators: {printList(task.getCollaborators())}</p>"
        st.markdown(taskString(task, collaborators), unsafe_allow_html=True)

#function that checks a list and then prints the tasks accordingly
def taskPrint(type_list : list):
    if len(type_list) == 0:
        st.error("No tasks available")
        print("Selected empty list")
    elif type(type_list[0]) is Task:
        taskLayout("Regular", type_list)
    elif type(type_list[0]) is PersonalTask:
        taskLayout("Personal", type_list)
    elif type(type_list[0]) is WorkTask:
        taskLayout("Work", type_list)