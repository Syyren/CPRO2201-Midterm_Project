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
collection = db[f"Work_Tasks"]



#retreiving all tasks in collection as cursor, then convert to list of WorkTasks
def getAllWorkTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = WorkTask(doc["title"],doc["description"], doc["collaborators"])
        task.setId(doc["_id"])
        task.setDueDate(doc['due_date'])
        task.setCreationDate(doc['creation_date'])
        task.setLength(doc['length'])
        all_tasks.append(task)
    return list(all_tasks)
     
#creating WorkTask and inserting to db
def createWorkTask(task : WorkTask):
    db_task = {
        "title" : task.getTitle(),
        "description" : task.getDescription(),
        "due_date" : task.getDueDate(),
        "creation_date" : task.getCreationDate(),
        "length" : task.getLength(),
        "collaborators" : task.getCollaborators()
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

#Takes a WorkTask object, and the key:value to be updated and updates db
def updateWorkTask(new_task : WorkTask):
    task_id = collection.update_one({"_id": new_task.getId()}, 
                                    {"$set": 
                                        {'title' : new_task.getTitle(),
                                         'description' : new_task.getDescription(),
                                         'due_date':new_task.getDueDate(),
                                         "length" : new_task.getLength(),
                                         "collaborators" : new_task.getCollaborators()
                                        }
                                    })
    print(f"Update For ID: {task_id}")

#Takes WorkTask object, deletes by id
def deleteWorkTask(task : WorkTask):
    collection.delete_one({"_id":task.getId()})

#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Work Task Controler: pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)