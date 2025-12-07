import pytest
import json
from src.calculator import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'

def test_calculate_add(client):
    response = client.post('/calculate', 
                          json={'operation': 'add', 'num1': 10, 'num2': 5})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 15

def test_calculate_invalid_operation(client):
    response = client.post('/calculate', 
                          json={'operation': 'invalid', 'num1': 10, 'num2': 5})
    assert response.status_code == 400