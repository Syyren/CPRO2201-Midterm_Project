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

#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def createTask(task : Task):
    collection = db["Regular_Tasks"]
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

def updateTask(task: Task):
    collection = db["Regular_Tasks"]
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}"
    }
    collection.update_one(db_task)
    print(f"Update Successful For ID:")

def deleteTask(task_id):
    collection = db["Regular_Tasks"]
    collection.delete_one(task_id)