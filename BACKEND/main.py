from fastapi import FastAPI
from database import get_all_task, get_one_task_id, create_task, update_task, delete_task

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Wellcome to the API"}

#GET
@app.get("/api/tasks")
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@app.get("/api/tasks/{id}")
async def get_task():
    return {"data": "The task"}

#CREATE POST
@app.post("/api/tasks")
async def create_task():
    return {"data": "Create task"}

#UPDATE PUT
@app.put("/api/tasks/{id}")
async def update_tasks():
    return {"data": "Update task"}

#DELETE DELETE
@app.delete("/api/tasks/{id}")
async def delete_task():
    return {"data": "Delete task"}