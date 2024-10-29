#module that returns the partial view view

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import getAllTasks
from ..Controllers.PersonalTaskController import getAllPersonalTasks
from ..Controllers.WorkTaskController import getAllWorkTasks
from .EditView import editView
from .DeleteView import deleteView
from ..Scripts.QOL import applyCSS, printList

#function that defines the view when view task is selected, allows user to view and delete their tasks
def viewView(REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    #applying the css and creating various lists based on the tasks
    applyCSS()
    regular_tasks = getAllTasks()
    personal_tasks = getAllPersonalTasks()
    work_tasks = getAllWorkTasks()
    #for layout
    col1, col2 = st.columns([1, 2])
    with col1:
        #selects the task type
        task_types = st.multiselect("Tasks", options=[REG, PER, WOR],)
    with col2:
        #generates the list of tasks or prints a select prompt
        if len(task_types) > 0:
            task_list = []
            for task_type in task_types:
                if task_type == REG:
                    task_list.append(regular_tasks)
                elif task_type == PER:
                    task_list.append(personal_tasks)
                elif task_type == WOR:
                    task_list.append(work_tasks)
            st.write(f"Viewing details for your \"{printList(task_types)}\" tasks.")
            for type_list in task_list:
                taskPrint(type_list)
        else:
            st.write("Please select the type of tasks you'd like to view.")

#returns a string that's formatted depending on the type of task
def taskString(task : Task, extra_data : str = "<p></p>"):
    due_date = "<p>Due: No date assigned.</p>"
    check = task.getDueDate()
    if check:
        due_date = f"<p>Due: {check.strftime("%a, %b %d, %Y at %I:%M%p")}</p>"
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

#function that generates the layout before gathering the edit view
def taskLayout(task_type : str, type_list : list):
    for task in type_list:
        task.displayAttributes()
        taskDisplay(task, task_type)
        col1, col2 = st.columns([1,1])
        with col1:
            edit = st.button(f"Edit \"{task.getTitle()}", key=f"edit_{hash(task.getId())}\"")
            if edit:
                editView(task, task_type)
        with col2:
            delete = st.button(f"Delete \"{task.getTitle()}", key=f"delete_{hash(task.getId())}\"")
            if delete:
                deleteView(task, task_type)

#function that writes details for a task
def taskDisplay(task : Task,
                task_type : str,
                REG = "Regular",
                PER = "Personal",
                WOR = "Work"):
    if task_type == REG:
        st.markdown(taskString(task), unsafe_allow_html=True)
    elif task_type == PER:
        friends = ""
        if len(task.getFriends()) > 0:
            friends = f"<p>With: {printList(task.getFriends())}</p>"
        st.markdown(taskString(task, friends), unsafe_allow_html=True)
    elif task_type == WOR:
        extra_data = ""
        if len(task.getCollaborators()) > 0:
                extra_data = f"<p>Collaborators: {printList(task.getCollaborators())}</p>"
        if task.getLengthMins() > 0 and task.getLengthHrs() > 0:
            extra_data += f"<p>Length: {task.getLengthHrs()} hours and {task.getLengthMins()} minutes.</p>"
        elif task.getLengthMins() > 0:
            extra_data += f"<p>Length: {task.getLengthMins()} minutes.</p>"
        elif task.getLengthHrs() > 0:
            extra_data += f"<p>Length: {task.getLengthHrs()} hours.</p>"
        st.markdown(taskString(task, extra_data), unsafe_allow_html=True)

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