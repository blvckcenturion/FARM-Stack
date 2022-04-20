from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

# App object
app = FastAPI()

# List of allowed origins
origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET Methods
@app.get("/api/todo", response_model=list)
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo(title: str):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"Todo not found with title: {title}")


# POST Methods
@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(status_code=400, detail="Something went wrong")


# PUT Methods
@app.put("/api/todo/{id}", response_model=Todo)
async def put_todo(title: str, description: str, completed: bool):
    response = await update_todo(title, description, completed)
    if response:
        return response
    raise HTTPException(status_code=404, detail=f"Todo not found with title: {title}")


# DELETE Methods
@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted"
    raise HTTPException(status_code=404, detail=f"Todo not found with title: {title}")
