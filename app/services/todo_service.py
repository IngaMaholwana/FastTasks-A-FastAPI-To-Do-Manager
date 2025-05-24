from typing import List, Optional

from ..models.todo import TodoCreate, TodoResponse
from fastapi import HTTPException, status

# Mock database (in a real app, this would be a database)
fake_todos_db = {}
todo_counter = 0

def create_todo(todo: TodoCreate) -> TodoResponse:
    global todo_counter
    todo_counter += 1
    todo_dict = todo.dict()
    new_todo = {**todo_dict, "id": todo_counter}
    fake_todos_db[todo_counter] = new_todo
    return new_todo

def get_todo(todo_id: int) -> TodoResponse:
    if todo_id not in fake_todos_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return fake_todos_db[todo_id]

def list_todos(skip: int = 0, limit: int = 10) -> List[TodoResponse]:
    return list(fake_todos_db.values())[skip: skip + limit]

def update_todo(todo_id: int, todo: TodoCreate) -> TodoResponse:
    if todo_id not in fake_todos_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    updated_todo = {**fake_todos_db[todo_id], **todo.dict()}
    fake_todos_db[todo_id] = updated_todo
    return updated_todo

def delete_todo(todo_id: int) -> None:
    if todo_id not in fake_todos_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    del fake_todos_db[todo_id]