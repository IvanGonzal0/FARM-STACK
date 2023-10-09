from motor.motor_asyncio import AsyncIOMotorClient
from models import Task

#MongoDB
client = AsyncIOMotorClient('mongodb://localhost')
database = client.taskdatabase
collection = database.tasks

async def get_all_task():
    tasks = []
    cursor = await collection.find({})

    async for document in cursor:
        tasks.append(**document)
    return tasks

async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task


async def create_task(id):
    new_task = await collection.insert_one({'_id': id})
    created_task = await collection.find_one({'_id': new_task.inserted_id})
    return created_task