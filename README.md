# 📝 TODO Application

A simple and beginner-friendly **TODO REST API** built using **Python and FastAPI**.

The application allows users to create, view, update, complete, filter, and delete TODOs. Data is persisted using **SQLite with SQLAlchemy**.

---

## 🚀 Features

- ➕ Create a TODO
- 📋 View all TODOs
- 🔍 Get a TODO by ID
- ✏️ Update a TODO
- ✅ Mark a TODO as completed
- 🔎 Filter TODOs by completion status
- 🗑️ Delete a TODO
- ⚠️ Request validation and error handling
- 💾 SQLite database persistence
- 🧪 Automated API tests
- 📚 Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

- 🐍 **Python**
- ⚡ **FastAPI**
- 📦 **Pydantic**
- 🗄️ **SQLite**
- 🔗 **SQLAlchemy**
- 🧪 **Pytest**
- 🌿 **Git & GitHub**

---

## 📂 Project Structure

```text
TODO_Project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── todo.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── todo.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── todo.py
│   │
│   └── services/
│       ├── __init__.py
│       └── todo_service.py
│
├── tests/
│   ├── __init__.py
│   └── test_todos.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

