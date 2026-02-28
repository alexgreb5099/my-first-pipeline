# test_app.py
from app import app

def test_homepage():
    response = app.test_client().get('/')
    assert response.data == b"Hello, DevOps World! Это мой второй пуск CI"
    assert response.status_code == 200
