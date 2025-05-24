# app/routes/items.py
from fastapi import APIRouter, Path, Query, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import SessionLocal
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoResponse

router = APIRouter(prefix="/items", tags=["items"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: TodoCreate, db: Session = Depends(get_db)):
    """Create a new item"""
    db_item = Todo(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=TodoResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    """Get a specific item by ID"""
    db_item = db.query(Todo).filter(Todo.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.get("/", response_model=List[TodoResponse])
async def list_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """List items with optional filtering and pagination"""
    return db.query(Todo).offset(skip).limit(limit).all()

@router.put("/{item_id}", response_model=TodoResponse)
async def update_item(item_id: int, updated_item: TodoCreate, db: Session = Depends(get_db)):
    """Update a specific item by ID"""
    db_item = db.query(Todo).filter(Todo.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in updated_item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Delete a specific item by ID"""
    db_item = db.query(Todo).filter(Todo.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return
