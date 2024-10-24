import os
import datetime
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
collection = db[f"Work_Tasks"]



#retreiving all tasks in collection as cursor, then convert to list of WorkTasks
def getAllWorkTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = WorkTask(doc["title"],doc["description"], doc["collaborators"])
        task.setId(doc["_id"])
        task.setDueDate(doc['due_date'])
        task.setCreationDate(doc["creation_date"])
        task.setLength(doc['length'])
        all_tasks.append(task)
    return list(all_tasks)



#retrieving task by id and returning as WorkTask object.
def getTaskById(id):
    cursor = collection.find_one({"_id":id})
    db_task = WorkTask(
        cursor["title"],
        cursor["description"],
        cursor['collaborators']
    )
    db_task.setId(cursor["_id"])
    if cursor["due_date"] != "None":
        db_task.setDueDate(datetime.datetime.strptime(cursor['due_date'], '%Y-%m-%d %H:%M:%S.%f'))
    db_task.setCreationDate(datetime.datetime.strptime(cursor['creation_date'], '%Y-%m-%d %H:%M:%S.%f'))
    db_task.setLength(cursor['length'])
    return db_task
     
#creating WorkTask and inserting to db
def createTask(task : WorkTask):
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{task.getDueDate()}",
        "creation_date" : f"{datetime.datetime.task.getCreationDate().strftime('%Y-%m-%d %H:%M:%S.%f')}",
        "length" : f"{task.getLength()}",
        "collaborators" : f"{task.getCollaborators()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

#Takes a WorkTask object, and the key:value to be updated and updates db
def updateTask(task : WorkTask, update_key, new_value):  
    task_id = collection.update_one({"_id": task.getId()}, {"$set": {update_key : new_value}})
    print(f"Update For ID: {task_id}")

#Takes WorkTask object, deletes by id
def deleteTask(task_id):
    collection.delete_one(task_id)


#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)