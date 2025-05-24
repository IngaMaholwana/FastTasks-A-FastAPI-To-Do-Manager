# app/models/item.py
from pydantic import BaseModel, Field
from typing import Optional, List

class ItemBase(BaseModel):
    """Base model for item data"""
    name: str = Field(..., min_length=1, max_length=100, description="The name of the task")
    description: Optional[str] = Field(None, max_length=1000, description="Description for the task")
    status: str = Field(..., gt=0, description="List all to-do items with optional filtering by status (completed/pending)")
    tags: List[str] = Field(default=[], description="List of tags for the item")

class ItemCreate(ItemBase):
    """Model for creating a new to do task"""
    pass

class ItemResponse(ItemBase):
    """Model for item responses that includes the ID"""
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Finish website project",
                "description": "Complete the final touches on the website project",
                "status": 1299.99,
                "tags": ["electronics", "computers"]
            }
        }
