import os
import datetime
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

#STRPTIME makes a datetime Obj from string in specified format
#STRFTIME makes a string from datetime obj into the specified format

#retreiving all tasks in collection as cursor, then convert to list of Tasks
def getAllTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = Task(doc["title"],doc["description"])
        task.setId(doc["_id"])
        print(f"Creation Date from Mongo: {doc["creation_date"]}")
        print('doc["due_date"]: ',doc["due_date"])
        if doc["due_date"] is type(str) and doc["due_date"] != None:
            task.setDueDate(datetime.datetime.strptime(doc['due_date'], '%Y-%m-%d %H:%M:%S.%f'))
        task.setCreationDate(datetime.datetime.strptime(doc['creation_date'], '%Y-%m-%d %H:%M:%S.%f'))
        all_tasks.append(task)
    return list(all_tasks)


#retrieving task by id and returning as Task object.
def getTaskById(id):
    cursor = collection.find_one({"_id":id})
    db_task = Task(
        cursor["title"],
        cursor["description"]
    )
    db_task.setId(cursor["_id"])
    if cursor["due_date"] != 'None':
        db_task.setDueDate(cursor['due_date'])
    db_task.setCreationDate(cursor["creation_date"])
    return db_task
     
#creating task and inserting to db
def createTask(task : Task):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{datetime.datetime.strftime(task.getCreationDate(),'%Y-%m-%d %H:%M:%S.%f')}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")


#Takes a task object and updates db info
def updateTask(new_task : Task):  

    task_id = collection.update_one({"_id": new_task.getId()}, 
                                    {"$set": 
                                        {'title' : new_task.getTitle(),
                                         'description' : new_task.getDescription(),
                                         'due_date':new_task.getDueDate()}})
    print(f"Update For ID: {task_id}")

#Takes task object, deletes by id
def deleteTask(task : Task):
    collection.delete_one({"_id":task.getId()})

#Sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)