from locust import HttpUser, task, between
from datetime import datetime

class MywebUser(HttpUser):
    wait_time = between(1, 2)
   # host = "https://www.google.com"
    
    
    @task(3)
    def web(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Hello, frank! am a web user")
        
class MymobileUser(HttpUser):
    wait_time = between(1, 2)
   # host = "https://www.google.com"
    
    
    @task(2)
    def mobile(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Hello, frank! am a mobile user")
        
