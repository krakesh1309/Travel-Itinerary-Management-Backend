from locust import HttpUser, task, between

class FastAPIPerformanceTest(HttpUser):
    host = "http://localhost:8000"  

    wait_time = between(1, 3)  

    @task
    def view_itineraries(self):
        response = self.client.get("/itineraries")
        if response.status_code != 200:
            print(f"Failed to GET /itineraries: {response.status_code}, {response.text}")

    @task
    def create_itinerary(self):
        payload = {
            "name": "Performance Test",
            "nights": 4,
            "region": "Thailand"
        }
        response = self.client.post("/itineraries", json=payload)
        if response.status_code not in [200, 201]:
            print(f"Failed to POST /itineraries: {response.status_code}, {response.text}")
