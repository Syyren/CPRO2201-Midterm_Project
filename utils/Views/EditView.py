import streamlit as st
from ..Models.Task import Task
from ..Models.PersonalTask import PersonalTask
from ..Models.WorkTask import WorkTask

def editView(task,
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