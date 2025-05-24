# FastTasks-A-FastAPI-To-Do-Manager
# README.md
# To-Do List Application

This is a simple To-Do List application built with FastAPI. It allows users to create, list, update, and delete to-do items. The application is structured to provide a clear separation of concerns, with models, routes, services, and utilities organized into distinct modules.

## Features

- Create new to-do items
- List all to-do items with pagination
- Update existing to-do items
- Delete to-do items
- Input validation and error handling
- API documentation generated automatically by FastAPI

## Project Structure

```
todo-list-app
├── app
│   ├── main.py          # Entry point of the application
│   ├── models           # Pydantic models for to-do items
│   │   └── todo.py
│   ├── routes           # CRUD endpoints for managing to-do items
│   │   └── todos.py
│   ├── utils            # Custom exceptions and error handlers
│   │   └── exceptions.py
│   └── services         # Business logic for managing to-do items
│       └── todo_service.py
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd todo-list-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `POST /todos/` - Create a new to-do item
- `GET /todos/` - List all to-do items
- `GET /todos/{todo_id}` - Retrieve a specific to-do item
- `PUT /todos/{todo_id}` - Update a specific to-do item
- `DELETE /todos/{todo_id}` - Delete a specific to-do item

