import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..Models.Task import Task
#For handling interraction with mongo and the view

#getting the connection path from the .env file and connecting to the client
load_dotenv()
uri = os.getenv("MONGO_CONNECTION")
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Tasks"]
collection = db[f"Regular_Tasks"]



#retreiving all tasks in collection as cursor instance
def getAllTasks():
    cursor = collection.find({})
    return cursor


#INCOMPLETE
def getTask(id):
    return collection.find_one({ "_id": id })

def createTask(task : Task):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")


#INCOMPLETE
def updateTask(task: Task, updated_key_value: dict):
    collection.update_one({"_id": task.getId()}, {"$set": updated_key_value})
    print(f"Update Successful For ID:")

def deleteTask(task_id):
    collection.delete_one(task_id)



#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # try:
    #     print("getting a task...")
    #     print(getTask("67187ff4475432be422d0dc3"))
    # except Exception as e:
    #     print('error getting task')
except Exception as e:
    print(e)