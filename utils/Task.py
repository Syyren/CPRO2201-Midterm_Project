from dataclasses import dataclass
import datetime

#declaring the parent class for tasks
class Task():
    #constructor, takes a title and description string, sets a default due date and creation time
    def __init__(self, title : str, description : str = None):
        self._title = title
        self._description = description
        self._due_date : datetime = None
        self.__creation_date: datetime = datetime.datetime.now

    #function that outputs the key attributes of the task object
    def displayAttributes(self):
        print(f'''
title: {self.getTitle()}
description: {self.getDescription()}
due date: {self.getDueDate()}''')
        
    #getters and setters for all relevant attributes, creation date has no setter as that's automatic and (inteded to be) immutable
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

#Declaring the personal tasks child class
class PersonalTask(Task):
    def __init__(self, title, description = None):
        super().__init__(title, description)

#Declaring the work tasks child class
class WorkTask(Task):
    def __init__(self, title, description = None):
        super().__init__(title, description)
        _length : str = None

    def displayAttributes(self):
        super().displayAttributes()
        print(f"length: {self.getLength()}")

    def getLength(self):
        return self._length

    def setLength(self, length_hours: int, length_mins: int):
        if length_mins < 60:
            self._length = f"{length_hours}:{length_mins}"
        else:
            self._length = None


if __name__ == "__main__":
    test_task = Task("Get Food", "Go to the store and grab some food.")
    test_task.setDueDate(2024, 10, 12, 4, 16)
    test_task.displayAttributes()

    test_personal_task = PersonalTask("Work Out")
    test_personal_task.displayAttributes()

    test_work_task = WorkTask("Meeting")
    test_work_task.setDueDate(2024, 10, 30, 3, 0)
    test_work_task.setLength(2, 30)
    test_work_task.displayAttributes()