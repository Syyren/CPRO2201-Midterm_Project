from .Task import Task

#Declaring the work tasks child class
class WorkTask(Task):
    def __init__(self, title, description = None, collaborators = []):
        super().__init__(title, description)
        #custom properties for the work task child class
        self._length : str = None
        self._collaborators : list = collaborators
    #displayAttributes override, displays additional attributes exclusive to this child class
    def displayAttributes(self):
        super().displayAttributes()
        print(f'''length: {self.getLength()}
collaborators: {self.getCollaborators()}''')

    def getLength(self):
        return self._length

    def setLength(self, length_hours: int, length_mins: int):
        if length_mins < 60:
            self._length = f"{length_hours}:{length_mins}"
        else:
            self._length = None

    def setLength(self, length: str):
        self._length = length

    def getCollaborators(self):
        return self._collaborators
    
    def setCollaborators(self, collaborators):
        if len(collaborators) > 0:
            for collaborator in collaborators:
                self._collaborators.append(collaborator)

#just testing
if __name__ == "__main__":
    test_work_task = WorkTask("Meeting")
    test_work_task.setDueDate(2024, 10, 30, 3, 0)
    test_work_task.setLength(2, 30)
    test_work_task.displayAttributes()