# app/main.py
from fastapi import FastAPI
from .routes import todos
from .utils.exceptions import add_exception_handlers

app = FastAPI(
    title="To-Do List Application",
    description="A FastAPI application for managing a to-do list with CRUD operations.",
    version="1.0.0"
)

app.include_router(todos.router)

add_exception_handlers(app)

@app.get("/", tags=["root"])
async def root():
    return {
        "message": "Welcome to the To-Do List API",
        "docs": "/docs",
        "endpoints": {
            "todos": "/todos"
        }
    }

# To run: uvicorn app.main:app --reload