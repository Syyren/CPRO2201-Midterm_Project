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



#retreiving all tasks in collection as cursor, then convert to list of Tasks
def getAllTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = Task(doc["title"],doc["description"])
        task.setId(doc["_id"])
        task.setDueDate(doc['due_date'])
        task.setCreationDate(doc["creation_date"])
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
    db_task.setDueDate(cursor['due_date'])
    db_task.setCreationDate(cursor["creation_date"])
    return db_task
     
#creating task and inserting to db
def createTask(task : Task):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{task.getCreationDate()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")


#Takes a task object, and the key:value to be updated and updates db
def updateTask(task : Task, update_key, new_value):  
    task_id = collection.update_one({"_id": task.getId()}, {"$set": {update_key : new_value}})
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