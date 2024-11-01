from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_foo():
    res = 1
    assert res == 1


def test_foo2():
    res = {"message": "Hello World"}
    assert res == {"message": "Hello World"}


def test_root_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
