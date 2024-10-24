import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
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

def getTask():
    return collection.find_one()
     

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
def updateTask(task : Task, update_key, new_value):    
    task_id = collection.find_one_and_update({"title": task.getTitle()}, {"$set": {update_key : new_value}})
    print(f"Update For ID: {task_id}")

def deleteTask(task_id):
    collection.delete_one(task_id)

#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    print("getting data... ")
    data = getAllTasks()
    i = 0
    for doc in data:
        i += 1
        print(f"doc {i}: {doc}")

    print("updating data... ")
    task = getTask()
    task_ob = Task(task['title'],task['description'])
    task_ob.setId(task["_id"])
    updateTask(task_ob, 'title', 'UpdateTask1')

    print("getting new data...")
    data = getAllTasks()
    i = 0
    for doc in data:
        i += 1
        print(f"doc {i}: {doc}")

except Exception as e:
    print(e)