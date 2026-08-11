from sqlalchemy.orm import Session

from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def create_todo(db: Session, todo_data: TodoCreate):
    todo = Todo(
        title=todo_data.title,
        description=todo_data.description,
        completed=False
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_todos(db: Session, completed: bool | None = None):
    query = db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)

    return query.all()


def get_todo(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(
    db: Session,
    todo_id: int,
    todo_data: TodoUpdate
):
    todo = get_todo(db, todo_id)

    if todo is None:
        return None

    todo.title = todo_data.title
    todo.description = todo_data.description
    todo.completed = todo_data.completed

    db.commit()
    db.refresh(todo)

    return todo


def complete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)

    if todo is None:
        return None

    todo.completed = True

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(db: Session, todo_id: int):
    todo = get_todo(db, todo_id)

    if todo is None:
        return None

    db.delete(todo)
    db.commit()

    return True