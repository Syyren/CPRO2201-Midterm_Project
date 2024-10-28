import os
import datetime
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
        if doc["due_date"] != "None":
            task.setDueDate(datetime.datetime.strptime(doc['due_date'], '%Y-%m-%d %H:%M:%S.%f'))
        task.setCreationDate(datetime.datetime.strptime(doc['creation_date'], '%Y-%m-%d %H:%M:%S.%f'))
        all_tasks.append(task)
    return list(all_tasks)

#creating personal task and inserting to db
def createPersonalTask(task : PersonalTask):
    due_date = None
    if task.getDueDate():
        due_date = datetime.datetime.strftime(task.getDueDate(),'%Y-%m-%d %H:%M:%S.%f')
    db_task = {
        "title" : f"{task.getTitle()}",
        "description" : f"{task.getDescription()}",
        "due_date" : f"{due_date}",
        "creation_date" : f"{datetime.datetime.strftime(task.getCreationDate(),'%Y-%m-%d %H:%M:%S.%f')}",
        "friends" : f"{task.getFriends()}"
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

#Takes a personal task object, and the key:value to be updated and updates db
def updatePersonalTask(new_task : PersonalTask):
    due_date = new_task.getDueDate()
    if due_date:
        due_date = datetime.datetime.strftime(new_task.getDueDate(),'%Y-%m-%d %H:%M:%S.%f')
    task_id = collection.update_one({"_id": new_task.getId()}, 
                                    {"$set": 
                                        {'title' : new_task.getTitle(),
                                         'description' : new_task.getDescription(),
                                         'due_date':f"{due_date}",
                                         "friends" : f"{new_task.getFriends()}"
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