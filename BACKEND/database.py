from motor.motor_asyncio import AsyncIOMotorClient
from models import Task

#MongoDB
client = AsyncIOMotorClient('mongodb://localhost')
database = client.taskdatabase
collection = database.tasks

#CRUD
#Get all tasks
async def get_all_task():
    tasks = []
    cursor = await collection.find({})

    async for document in cursor:
        tasks.append(**document)
    return tasks
#Get one task
async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task
#Create task
async def create_task(id):
    new_task = await collection.insert_one({'_id': id})
    created_task = await collection.find_one({'_id': new_task.inserted_id})
    return created_task
#Update task
async def update_task(id: str,  task):
    await collection.update_one({'_id': id}, {'$set': task})
    document = await collection.find_one({'_id': id})
    return document
#Delete task
async def delete_task(id: str):
    await collection.delete_one({'_id': id})
    return True