from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.services import todo_service

router = APIRouter(
    prefix="/todos",
    tags=["Todos"])

@router.post(
    "",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)):
    return todo_service.create_todo(db, todo)

@router.get(
    "",
    response_model=list[TodoResponse],
    status_code=status.HTTP_200_OK)
def get_todos(
    completed: bool | None = None,
    db: Session = Depends(get_db)):
    return todo_service.get_todos(db, completed)

@router.get(
    "/{todo_id}",
    response_model=TodoResponse,
    status_code=status.HTTP_200_OK)
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)):
    todo = todo_service.get_todo(db, todo_id)

    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TODO not found")
    return todo

@router.put(
    "/{todo_id}",
    response_model=TodoResponse,
    status_code=status.HTTP_200_OK)
def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db)):
    updated_todo = todo_service.update_todo(
        db,
        todo_id,
        todo
    )

    if updated_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TODO not found"
        )
    return updated_todo

@router.patch(
    "/{todo_id}/complete",
    response_model=TodoResponse,
    status_code=status.HTTP_200_OK)
def complete_todo(
    todo_id: int,
    db: Session = Depends(get_db)):
    todo = todo_service.complete_todo(
        db,
        todo_id
    )
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TODO not found"
        )
    return todo

@router.delete(
    "/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db)):
    deleted = todo_service.delete_todo(
        db,
        todo_id
    )
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="TODO not found"
        )
    return None