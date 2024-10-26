#file for scripts that do convenient things

import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

#function that applies CSS to page
def applyCSS():
    with open("utils/Views/ViewViewStyle.css") as stylesheet:
        css = stylesheet.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def editTask(task,
             task_type : str,
             date_check_text = "Is there a due date?",
             title_txt = "Title*",
             desc_txt = "Description",
             due_txt = "Due Date",
             submit_txt = "Submit",
             PER = "Personal",
             WOR = "Work"):
    date_check = st.checkbox(date_check_text)
    if task_type == PER:
        friend_slider = st.slider("Friends", 0, 5, len(task.getFriends()))
    elif task_type == WOR:
        collaborator_slider = st.slider("Collaborators", 0, 8, len(task.getCollaborators()))
    with st.form(f"edit_form_{hash(task.getId())}"):
        title = st.text_input(title_txt, value=task.getTitle())
        description = st.text_input(desc_txt, value=task.getDescription())
        due_date = task.getDueDate()
        if date_check:
            due_date = st.date_input(due_txt, value=task.getDueDate())
        if task_type == PER:
            friends = []
            for i in range(friend_slider):
                friend_name = st.text_input(f"Friend {i + 1}'s Name", task.getFriends()[i])
                if friend_name:
                    friends.append(friend_name)
        elif task_type == WOR:
            collaborators = []
            for i in range(collaborator_slider):
                collaborator_name = st.text_input(f"Collaborator {i + 1}'s Name", task.getCollaborators()[i])
                if collaborator_name:
                    collaborators.append(collaborator_name)
        submitted = st.form_submit_button(submit_txt)
        if submitted:
            st.write(f"\"{title}\" update submitted.")

def cancelButton(task : Task):
    cancel = st.button(f"Cancel", key=f"cancel_{hash(task.getId())}")
    if cancel:
        return False

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
            editTask(task, task_type)
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