from .Task import Task

#Declaring the personal tasks child class
class PersonalTask(Task):
    def __init__(self, title, description = None, friends = []):
        super().__init__(title, description)
        #custom properties for the personal task child class
        self._friends : list = friends
    #displayAttributes override, displays additional attributes exclusive to this child class
    def displayAttributes(self):
        super().displayAttributes()
        print(f'''friends: {self.getFriends()}''')

    def getFriends(self):
        return self._friends
    
    def setFriends(self, friends : list):
        self._friends = friends

#just testing
if __name__ == "__main__":
    test_personal_task = PersonalTask("Work Out")
    test_personal_task.displayAttributes()