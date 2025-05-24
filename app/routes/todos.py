# app/routes/items.py
from fastapi import APIRouter, Path, Query, HTTPException, status
from typing import List, Optional

from ..models.todo import TodoCreate, TodoResponse
from ..utils.exceptions import ItemNotFoundError

router = APIRouter(prefix="/items", tags=["items"])

# Mock database (in a real app, this would be a database)
fake_items_db = {}
item_counter = 0

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: TodoCreate):
    """Create a new item"""
    global item_counter
    item_counter += 1

    # Create new item with ID
    item_dict = item.dict()
    new_item = {**item_dict, "id": item_counter}

    # Store in our fake database
    fake_items_db[item_counter] = new_item

    return new_item

@router.get("/{item_id}", response_model=TodoResponse)
async def read_item(item_id: int = Path(..., gt=0)):
    """Get a specific item by ID"""
    if item_id not in fake_items_db:
        raise ItemNotFoundError(item_id)

    return fake_items_db[item_id]

@router.get("/", response_model=List[TodoResponse])
async def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    """List items with optional filtering and pagination"""
    items = list(fake_items_db.values())

    # Apply pagination
    return items[skip:skip+limit]

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int = Path(..., gt=0)):
    """Delete a specific item by ID"""
    if item_id not in fake_items_db:
        raise ItemNotFoundError(item_id)

    del fake_items_db[item_id]
    return
