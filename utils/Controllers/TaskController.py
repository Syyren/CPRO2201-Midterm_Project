import os
from dotenv import load_dotenv
from datetime import datetime
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

#retreiving all tasks in collection as cursor, then convert to list of Tasks
def getAllTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = Task(doc["title"],doc["description"])
        task.setId(doc["_id"])
        task.setDueDate(doc['due_date'])
        task.setCreationDate(doc['creation_date'])
        all_tasks.append(task)
    return list(all_tasks)
    
#creating task and inserting to db
def createTask(task : Task):
    db_task = {
        "title" : task.getTitle(),
        "description" : task.getDescription(),
        "due_date" : task.getDueDate(),
        "creation_date" : task.getCreationDate()
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

#Takes a task object and updates db info
def updateTask(new_task : Task): 
    task_id = collection.update_one({"_id": new_task.getId()}, 
                                    {"$set": 
                                        {'title' : new_task.getTitle(),
                                         'description' : new_task.getDescription(),
                                         'due_date': new_task.getDueDate()
                                        }
                                    })
    print(f"Update For ID: {task_id}")

#Takes task object, deletes by id
def deleteTask(task : Task):
    collection.delete_one({"_id":task.getId()})

#Sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Task Controler: pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)