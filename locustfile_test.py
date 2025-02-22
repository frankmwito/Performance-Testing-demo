from locust_test2 import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Simulates user waiting between requests (1-5 seconds)

    @task
    def load_homepage(self):
        self.client.get("/")  # Sends a GET request to the homepage
