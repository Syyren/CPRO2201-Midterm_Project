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
def editView(task,
             task_type : str,
             date_check_text = "Set a date?",
             title_txt = "Title*",
             desc_txt = "Description",
             due_txt = "Date",
             time_txt = "Time",
             submit_txt = "Submit",
             REG = "Regular",
             PER = "Personal",
             WOR = "Work"):
    field_date_and_time : datetime = None
    field_date = None
    field_time = None

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
            if task.getDueDate():
                field_date_and_time = task.getDueDate()
                field_date = field_date_and_time.date()
                field_time = field_date_and_time.time()
            due_date = st.date_input(due_txt, field_date)
            due_time = st.time_input(time_txt, field_time)
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
            len_hour = st.slider("Hours", 0, 12, task.getLengthHrs())
            len_mins = st.slider("Minutes", 0, 60, task.getLengthMins())
        submitted = st.form_submit_button(submit_txt)
        if submitted:
            print(f"\"{title}\" update submitted.")
            if title == "":
                st.error("Title can't be blank!")
                return
            elif task_type == REG:
                task.setTitle(title)
                task.setDescription(description)
                new_task = task
                if date_check:
                    if due_date and due_time:
                        new_task.setDueDate(datetime.combine(due_date, due_time))
                updateTask(new_task)
            elif task_type == PER:
                new_task = PersonalTask(title, description)
                if due_date:
                    new_task.setDueDate(due_date)
                print(f"friends {friends}")
                if len(friends) > 0:
                    new_task.setFriends(friends)
                else:
                    new_task.setFriends([])
                updatePersonalTask(new_task)
            elif task_type == WOR:
                new_task = WorkTask(title, description)
                if due_date:
                    new_task.setDueDate(due_date)
                if len(collaborators) > 0:
                    new_task.setCollaborators(collaborators)
                else:
                    new_task.setCollaborators([])
                new_task.setLengthWithValues(len_hour, len_mins)
                updateWorkTask(new_task)
            st.rerun()