from fastapi.testclient import TestClient
from fastapi_app import app

client = TestClient(app)

def test_create_itinerary():
    response = client.post("/itineraries", json={
        "name": "Phuket Adventure",
        "nights": 5,
        "region": "Thailand"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Itinerary created successfully"

def test_invalid_itinerary():
    response = client.post("/itineraries", json={
        "name": "Invalid Itinerary",
        "nights": 10, 
        "region": "Invalid Region"
    })
    assert response.status_code == 400
    assert "Nights must be between 2 and 8" in response.json()["detail"]

def test_get_recommendations():
    response = client.get("/recommendations?nights=5")
    assert response.status_code == 200
    assert len(response.json()["recommendations"]) >= 0
