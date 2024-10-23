import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from ..Models import PersonalTask

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

def createTask(task : PersonalTask):
    db_task = {
        #attributes to be determined
    }
    task_id = collection.insert_one(db_task).inserted_id
    print(f"Insert Successful! Given ID: {task_id}")

def updateTask(task: PersonalTask):
    db_task = {
        #attributes to be determined
    }
    collection.update_one(db_task)
    print(f"Update Successful For ID:")

def deleteTask(task_id):
    collection.delete_one(task_id)