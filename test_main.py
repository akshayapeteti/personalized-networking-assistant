from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_history():
    response = client.get("/history")
    assert response.status_code == 200

def test_fact_check():
    response = client.get("/fact-check/Python")
    assert response.status_code == 200