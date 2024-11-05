from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sheep Compendium!"}
def test_get_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "age": 3,
        "sex": "Female"
    }
def test_add_sheep():
    new_sheep = {
        "id": 2,
        "name": "Daisy",
        "breed": "Suffolk",
        "age": 2,
        "sex": "Female"
    }
    response = client.post("/sheep", json=new_sheep)
    assert response.status_code == 201
    assert response.json() == new_sheep
