import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..Models.WorkTask import WorkTask

#For handling interraction with mongo and the view

#getting the connection path from the .env file and connecting to the client
load_dotenv()
uri = os.getenv("MONGO_CONNECTION")
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Tasks"]
collection = db[f"Personal_Tasks"]


#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#retreiving all tasks in collection as cursor instance
def getTask():
    cursor = collection.find({})
    return cursor

def createTask(task : WorkTask):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}",
        "length" : f"{task.getLength()}",
        "collaborators" : f"{task.getCollaborators()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

def updateTask(task: WorkTask):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}",
        "length" : f"{task.getLength()}",
        "collaborators" : f"{task.getCollaborators()}"
    }
    collection.update_one(db_task)
    print(f"Update Successful For ID:")

def deleteTask(task_id):
    collection.delete_one(task_id)