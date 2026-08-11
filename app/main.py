from fastapi import FastAPI
from app.database.database import Base, engine
from app.routers.todo import router as todo_router

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="TODO REST API",
    description="A simple TODO REST API built with FastAPI and SQLite",
    version="1.0.0"
)
app.include_router(todo_router)

@app.get("/")
def root():
    return {
        "message": "TODO API is running"
    }