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