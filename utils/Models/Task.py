from dataclasses import dataclass
import datetime

#declaring the parent class for tasks
class Task():
    #constructor, takes a title and description string, sets a default due date and creation time
    def __init__(self, title : str, description : str = None):
        self._id = "temp_id"
        if title.strip() == "":
            title = "Untitled Task"
        self._title = title
        if description:
            if description.strip() == "":
                description = None
        self._description = description
        self._due_date : datetime = None
        self.__creation_date: datetime = datetime.datetime.now()

    #function that outputs the key attributes of the task object
    def displayAttributes(self):
        print(f'''
title: {self.getTitle()}
description: {self.getDescription()}
due date: {self.getDueDate()}''')
        
    #getters and setters for all relevant attributes, creation date has no setter as that's automatic and (inteded to be) immutable
    def getId(self):
        return self.id
    
    def setId(self, id : str):
        self.id = id

    def getTitle(self):
        return self._title
    
    def setTitle(self, title : str):
        self._title = title
    
    def getDescription(self):
        return self._description
    
    def setDescription(self, description : str):
        self._description = description
    
    def getDueDate(self):
        return self._due_date

    def setDueDate(self, due_date : datetime):
        self._due_date = due_date

    def getCreationDate(self):
        return self.__creation_date
    
    def setCreationDate(self, creation_date : datetime):
        self.__creation_date = creation_date

#just testing
if __name__ == "__main__":
    test_task = Task("Get Food", "Go to the store and grab some food.")
    test_task.setDueDate(2024, 10, 12, 4, 16)
    test_task.displayAttributes()