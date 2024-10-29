#module that returns a pop up containing an edit

import streamlit as st
from datetime import datetime
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask
from ..Controllers.TaskController import updateTask
from ..Controllers.PersonalTaskController import updatePersonalTask
from ..Controllers.WorkTaskController import updateWorkTask

#pop up window that allows the user to edit an existing task via its form
@st.dialog(f"Edit Task")
def editView(task, task_type : str,
             date_check_text = "Set a due date?",
             title_txt = "Title*",
             desc_txt = "Description",
             due_txt = "Date",
             time_txt = "Time", 
             submit_txt = "Submit",
             REG = "Regular", PER = "Personal", WOR = "Work"):
    #declaring the checkbox to be on when the form is initialized
    date_check = st.checkbox(date_check_text, value=True)
    #checking the task type and dynamically generating elements based on the type
    if task_type == PER:
        friend_slider = st.slider("Friends", 0, 5, len(task.getFriends()))
    elif task_type == WOR:
        collaborator_slider = st.slider("Collaborators", 0, 8, len(task.getCollaborators()))
    with st.form(f"edit_form_{hash(task.getId())}"):
        title = st.text_input(title_txt, value=task.getTitle())
        description = st.text_input(desc_txt, value=task.getDescription())
        #determining more elements based on whether the user wants to include a date or not
        due = None
        if date_check:
            if task.getDueDate():
                field_date_and_time : datetime = task.getDueDate()
                field_date = field_date_and_time.date()
                field_time = field_date_and_time.time()
            else:
                field_date = datetime.now().date()
                field_time = datetime.now().time()
            due_date = st.date_input(due_txt, field_date)
            due_time = st.time_input(time_txt, field_time)
            due = datetime.combine(due_date, due_time)
        #generating fields based off a slider for friends/collaborators, dynamically adds names from the task to fields
        if task_type == PER:
            friends = []
            for i in range(friend_slider):
                if i + 1 <= len(task.getFriends()):
                    friend_name = st.text_input(f"Friend {i + 1}'s Name", task.getFriends()[i])
                else:
                    friend_name = st.text_input(f"Friend {i + 1}'s Name")
                if friend_name:
                    friends.append(friend_name)
        elif task_type == WOR:
            collaborators = []
            for i in range(collaborator_slider):
                if i + 1 <= len(task.getCollaborators()):
                    collaborator_name = st.text_input(f"Collaborator {i + 1}'s Name", task.getCollaborators()[i])
                else:
                    collaborator_name = st.text_input(f"Collaborator {i + 1}'s Name")
                if collaborator_name:
                    collaborators.append(collaborator_name)
            len_hour = st.slider("Hours", 0, 12, task.getLengthHrs())
            len_mins = st.slider("Minutes", 0, 60, task.getLengthMins())
        submitted = st.form_submit_button(submit_txt)
        #this triggers once the submit button is launched
        if submitted:
            print("Form Name:", task_type)
            #error handling
            print(f"\"{title}\" update submitted.")
            if title == "":
                st.error("Title can't be blank!")
                return
            #checking the task type and then creating a new object based on the entered variables
            #Regular Task
            elif task_type == REG:
                new_task = Task(title, description)
                new_task.setId(task.getId())
                if due:
                    new_task.setDueDate(due)
                updateTask(new_task)
            #Personal Task
            elif task_type == PER:
                new_task = PersonalTask(title, description)
                new_task.setId(task.getId())
                if due:
                    new_task.setDueDate(due)
                #setting the extra personal task values
                if len(friends) > 0:
                    new_task.setFriends(friends)
                else:
                    new_task.setFriends([])
                updatePersonalTask(new_task)
            #Work Task
            elif task_type == WOR:
                new_task = WorkTask(title, description)
                new_task.setId(task.getId())
                if due:
                    new_task.setDueDate(due)
                #setting the extra work task values
                if len(collaborators) > 0:
                    new_task.setCollaborators(collaborators)
                new_task.setLengthWithValues(len_hour, len_mins)
                updateWorkTask(new_task)
            #running a page refresh to close the dialogue
            st.rerun()