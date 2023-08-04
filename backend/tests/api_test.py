from fastapi.testclient import TestClient
from src.main.config.app import app

client = TestClient(app)

def test_app_running():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}



