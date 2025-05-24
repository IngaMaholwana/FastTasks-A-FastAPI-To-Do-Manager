from app.db import engine, Base
from app.models.todo import Todo

# Create all tables
Base.metadata.create_all(bind=engine)