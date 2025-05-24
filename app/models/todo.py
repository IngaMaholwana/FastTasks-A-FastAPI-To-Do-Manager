from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db import Base

class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="The title of the to-do item")
    description: Optional[str] = Field(None, max_length=1000, description="Optional description of the to-do item")
    due_date: Optional[datetime] = Field(None, description="The due date for the to-do item")
    status: str = Field("pending", description="The status of the to-do item (e.g., pending, completed)")

class TodoCreate(TodoBase):
    """Model for creating a new to-do item"""
    pass

class TodoResponse(TodoBase):
    """Model for to-do item responses that includes an ID"""
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Buy groceries",
                "description": "Milk, Bread, Eggs",
                "due_date": "2023-10-30T12:00:00",
                "status": "pending"
            }
        }

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    status = Column(String, default="pending")
    completed = Column(Boolean, default=False)