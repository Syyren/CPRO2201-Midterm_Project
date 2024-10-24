from dataclasses import dataclass
import datetime

#declaring the parent class for tasks
class Task():
    #constructor, takes a title and description string, sets a default due date and creation time
    def __init__(self, title : str, description : str = None):
        self.id = "temp_id"
        self._title = title
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
    
    def setId(self, id):
        self.id = id

    def getTitle(self):
        return self._title
    
    def setTitle(self, title):
        self._title = title
    
    def getDescription(self):
        return self._description
    
    def setDescription(self, description):
        self._description = description
    
    def getDueDate(self):
        return self._due_date

    def setDueDate(self, year: int, month: int, day: int, hour: int, minute: int):
        self._due_date = datetime.datetime(year, month, day, hour, minute)

    def getCreationDate(self):
        return self.__creation_date

#just testing
if __name__ == "__main__":
    test_task = Task("Get Food", "Go to the store and grab some food.")
    test_task.setDueDate(2024, 10, 12, 4, 16)
    test_task.displayAttributes()