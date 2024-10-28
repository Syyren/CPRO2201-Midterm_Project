import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..Models.PersonalTask import PersonalTask
#For handling interraction with mongo and the view

#getting the connection path from the .env file and connecting to the client
load_dotenv()
uri = os.getenv("MONGO_CONNECTION")
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Tasks"]
collection = db[f"Personal_Tasks"]

#retreiving all tasks in collection as cursor instance
def getAllPersonalTasks():
    cursor = collection.find({})
    all_tasks = []
    for doc in cursor:
        task = PersonalTask(doc["title"],doc["description"],doc["friends"])
        task.setId(doc["_id"])
        task.setDueDate(doc['due_date'])
        task.setCreationDate(doc['creation_date'])
        all_tasks.append(task)
    return list(all_tasks)

#creating personal task and inserting to db
def createPersonalTask(task : PersonalTask):
    db_task = {
        "title" : task.getTitle(),
        "description" : task.getDescription(),
        "due_date" : task.getDueDate(),
        "creation_date" : task.getCreationDate(),
        "friends" : task.getFriends()
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

#Takes a personal task object, and the key:value to be updated and updates db
def updatePersonalTask(new_task : PersonalTask):
    task_id = collection.update_one({"_id": new_task.getId()}, 
                                    {"$set": 
                                        {'title' : new_task.getTitle(),
                                         'description' : new_task.getDescription(),
                                         'due_date':new_task.getDueDate(),
                                         "friends" : new_task.getFriends()
                                        }
                                    })
    print(f"Update For ID: {task_id}")

#Takes personal task object, deletes by id
def deletePersonalTask(task : PersonalTask):
    collection.delete_one({"_id":task.getId()})

#sending a ping to confirm successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!"+"\n")

except Exception as e:
    print(e)