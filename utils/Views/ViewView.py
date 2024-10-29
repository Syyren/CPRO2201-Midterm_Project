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
            tasks : list = []
            list_of_task_lists : list = []
            for task_type in task_types:
                if task_type == REG:
                    list_of_task_lists.append(regular_tasks)
                elif task_type == PER:
                    list_of_task_lists.append(personal_tasks)
                elif task_type == WOR:
                    list_of_task_lists.append(work_tasks)
            st.write(f"Viewing details for your \"{printList(task_types)}\" tasks.")
            #displaying an ordered by due date list of tasks
            for task_list in list_of_task_lists:
                tasks += task_list
            #sorting by due date and displaying tasks with no due date first
            tasks = sorted(tasks, key=lambda t: (t.getDueDate() is not None, t.getDueDate()))
            taskLayout(tasks)
        else:
            st.write("Please select the type of tasks you'd like to view.")

#function that generates the layout before gathering the edit view
def taskLayout(task_list : list, REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):
    for task in task_list:
        if type(task) is Task:
            task_type = REG
        elif type(task) is PersonalTask:
            task_type = PER 
        elif type(task) is WorkTask:
            task_type = WOR
        #printing in the console for logging
        task.displayAttributes()
        taskFormat(task, task_type)
        col1, col2 = st.columns([1,1])
        #these buttons are dynamically generated with a hash of the correlated task id
        with col1:
            edit = st.button(f"Edit \"{task.getTitle()}\"", key=f"edit_{hash(task.getId())}\"")
            if edit:
                editView(task, task_type)
        with col2:
            delete = st.button(f"Delete \"{task.getTitle()}\"", key=f"delete_{hash(task.getId())}\"")
            if delete:
                deleteView(task, task_type)

#function that writes details for a task
def taskFormat(task : Task, task_type : str, REG : str = "Regular", PER : str = "Personal", WOR : str = "Work"):            
    if task_type == REG:
        st.markdown(taskString(task), unsafe_allow_html=True)
    #gathering extra data for the non-regular tasks to put into the html
    elif task_type == PER:
        extra_data = ""
        if len(task.getFriends()) > 0:
            extra_data += f"<p>With: {printList(task.getFriends())}</p>"
        st.markdown(taskString(task, extra_data), unsafe_allow_html=True)
    elif task_type == WOR:
        extra_data = ""
        if len(task.getCollaborators()) > 0:
                extra_data += f"<p>Collaborators: {printList(task.getCollaborators())}</p>"
        #unique dialogue for varying conditions of task session length
        if task.getLengthMins() > 0 and task.getLengthHrs() > 0:
            extra_data += f"<p>Length: {task.getLengthHrs()} hours and {task.getLengthMins()} minutes.</p>"
        elif task.getLengthMins() > 0:
            extra_data += f"<p>Length: {task.getLengthMins()} minutes.</p>"
        elif task.getLengthHrs() > 0:
            extra_data += f"<p>Length: {task.getLengthHrs()} hours.</p>"
        st.markdown(taskString(task, extra_data), unsafe_allow_html=True)

#returns a string that's formatted depending on the type of task
def taskString(task : Task, extra_data : str = "<p></p>"):
    #formatting the description field
    desc = "No Description."
    desc_check = task.getDescription()
    if desc_check:
        desc = desc_check
    #formatting the due date field
    due_date = "<p class=\"due\">Due: No date assigned.</p>"
    due_check = task.getDueDate()
    if due_check:
        due_date = f"<p class=\"due\">Due: {due_check.strftime("%a, %b %d, %Y at %I:%M%p")}</p>"
    string = f'''
    <div class="card">
        <p class="title">{task.getTitle()}</p>
        <p>\"{desc}\"</p>
        {extra_data}
        {due_date}
        <p class="created">Created on: {task.getCreationDate().strftime("%a, %b %d, %Y at %I:%M%p")}</p>
    </div>
    '''
    return string