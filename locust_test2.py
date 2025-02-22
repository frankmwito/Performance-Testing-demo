# simulating user login and session based testing

from locust_test2 import HttpUser, task, between
import json

class AuthenticateUser(HttpUser):
    wait_time = between(2, 5)
    
    def on_start(self):
        response = self.client.post("/login", json={"username":"mfranklyne039@gmail.com", "password": "Xf6Lbez33G"})
        
    @task(3)
    def view_dashboard(self):
        """Accessing a protected resource using authentication"""
        headers = {"Authorization": "Bearer" + self.client.auth_token}
        self.client.get("/request-artists", headers=headers)