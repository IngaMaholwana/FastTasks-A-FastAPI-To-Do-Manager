# FastTasks - A FastAPI To-Do Manager

## Overview

FastTasks is a robust and scalable To-Do List application built with FastAPI. It provides a RESTful API for managing tasks with features such as creating, listing, updating, and deleting to-do items. The application uses SQLite for persistent storage and follows a modular architecture to ensure maintainability and extensibility.

## Features

- **Create To-Do Items**: Add new tasks with a title, description, due date, and status.
- **List To-Do Items**: Retrieve all tasks with optional pagination and filtering.
- **Retrieve Specific To-Do Items**: Fetch details of a specific task by its ID.
- **Update To-Do Items**: Modify the details of an existing task.
- **Delete To-Do Items**: Remove tasks by their ID.
- **Persistent Storage**: Uses SQLite to store tasks persistently.
- **Input Validation**: Ensures data integrity using Pydantic models.
- **Error Handling**: Custom exception handling for better user feedback.
- **Interactive API Documentation**: Automatically generated by FastAPI for easy testing and exploration.

## Project Structure

```
todo-list-app
├── app
│   ├── main.py          # Entry point of the application
│   ├── models           # SQLAlchemy models for database tables
│   │   └── todo.py
│   ├── schemas          # Pydantic models for request/response validation
│   │   └── todo.py
│   ├── routes           # API endpoints for managing to-do items
│   │   └── todos.py
│   ├── utils            # Custom exceptions and error handlers
│   │   └── exceptions.py
│   ├── db.py            # Database configuration and session management
│   └── init_db.py       # Script to initialize the database
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-list-app
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python3.10 -m app.init_db
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### To-Do Management

- **POST `/items/`**: Create a new to-do item.
  - **Request Body**:
    ```json
    {
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs",
      "due_date": "2025-05-30T12:00:00",
      "status": "pending"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs",
      "due_date": "2025-05-30T12:00:00",
      "status": "pending"
    }
    ```

- **GET `/items/`**: List all to-do items with optional pagination.
  - **Query Parameters**:
    - `skip` (default: 0): Number of items to skip.
    - `limit` (default: 10): Maximum number of items to return.
  - **Response**:
    ```json
    [
      {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, Bread, Eggs",
        "due_date": "2025-05-30T12:00:00",
        "status": "pending"
      }
    ]
    ```

- **GET `/items/{item_id}`**: Retrieve a specific to-do item by its ID.
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Buy groceries",
      "description": "Milk, Bread, Eggs",
      "due_date": "2025-05-30T12:00:00",
      "status": "pending"
    }
    ```

- **PUT `/items/{item_id}`**: Update a specific to-do item by its ID.
  - **Request Body**:
    ```json
    {
      "title": "Buy groceries and snacks",
      "description": "Milk, Bread, Eggs, Chips",
      "due_date": "2025-06-01T12:00:00",
      "status": "pending"
    }
    ```
  - **Response**:
    ```json
    {
      "id": 1,
      "title": "Buy groceries and snacks",
      "description": "Milk, Bread, Eggs, Chips",
      "due_date": "2025-06-01T12:00:00",
      "status": "pending"
    }
    ```

- **DELETE `/items/{item_id}`**: Delete a specific to-do item by its ID.
  - **Response**: `204 No Content`

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLite**: Lightweight database for persistent storage.
- **SQLAlchemy**: ORM for database interaction.
- **Pydantic**: Data validation and settings management.

## Future Enhancements

- Add user authentication and authorization.
- Implement advanced filtering and sorting for the list endpoint.
- Add support for task prioritization and categorization.
- Create a frontend interface for managing tasks.
- Add support for recurring tasks and reminders.

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding! 🇿🇦 Ndilinde ukusebenza nani nonke 
