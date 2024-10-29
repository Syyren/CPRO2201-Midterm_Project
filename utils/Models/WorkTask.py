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
    
    #sets the length via two inputted numbers rather than the standard string
    def setLengthWithValues(self, length_hrs: int, length_mins: int):
        if length_mins in range(0, 61) and length_hrs in range(0, 13):
            self._length = f"{length_hrs}:{length_mins}"
        else:
            self._length = "0:0"

    #sets the length via a string with some in-built error handling
    def setLength(self, length: str):
        if len(length.split(":")) == 2 and length.split(":")[0].isdigit() and length.split(":")[1].isdigit() :
            self._length = length
        else:
            self._length = "0:0"
    
    #get the length's hours
    def getLengthHrs(self):
        hrs = int(self.getLength().split(":")[0])
        return hrs
    
    #gets the length's minutes
    def getLengthMins(self):
        mins = int(self.getLength().split(":")[1])
        return mins

    def getCollaborators(self):
        return self._collaborators
    
    def setCollaborators(self, collaborators : list):
        self._collaborators = collaborators

#just testing
if __name__ == "__main__":
    test_work_task = WorkTask("Meeting")
    #test_work_task.setLengthWithValues(2, 30)
    test_work_task.setLength("test")
    test_work_task.displayAttributes()
    print("Hrs: ",test_work_task.getLengthHrs())
    print("Mins: ",test_work_task.getLengthMins())