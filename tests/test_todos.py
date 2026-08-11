from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_create_todo():
    response = client.post(
        "/todos", json={
            "title": "Test TODO",
            "description": "Testing create endpoint"
        })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test TODO"
    assert data["completed"] is False
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_get_todo_not_found():
    response = client.get("/todos/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "TODO not found"
def test_complete_todo():
    create_response = client.post(
        "/todos",
        json={
            "title": "Complete the task",
            "description": "Testing completion"
        })
    todo_id = create_response.json()["id"]
    response = client.patch(f"/todos/{todo_id}/complete")

    assert response.status_code == 200
    assert response.json()["completed"] is True

def test_update_todo():
    create_response = client.post(
        "/todos",
        json={
            "title": "Old title",
            "description": "Old description"
        })
    todo_id = create_response.json()["id"]
    response = client.put(
        f"/todos/{todo_id}",
        json={
            "title": "New title",
            "description": "New description",
            "completed": True
        })
    assert response.status_code == 200
    assert response.json()["title"] == "New title"
    assert response.json()["completed"] is True

def test_delete_todo():
    create_response = client.post(
        "/todos",
        json={
            "title": "Delete me",
            "description": "Testing delete"
        })
    todo_id = create_response.json()["id"]
    response = client.delete(
        f"/todos/{todo_id}")

    assert response.status_code == 204
    get_response = client.get(
        f"/todos/{todo_id}")
    assert get_response.status_code == 404
    