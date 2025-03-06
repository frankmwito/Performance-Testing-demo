from locust import HttpUser, task, between, events, stats
from datetime import datetime

host = "https://www.google.com"
# Test start Hook
@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Test is Starting! Perform setup.....")
    # perform setup here
    print("Environment host:", environment.host)
    
# Test stop Hook
@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Test is Stopping! Perform cleanup.....")
    # perform cleanup here
    print("Total requests:", environment.stats.total.num_requests)
class MywebUser(HttpUser):
    wait_time = between(1, 2)
    # host = "https://www.google.com"
   
    @task
    def web(self):
        self.client.get("/search?q=locust")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Hello, frank! am a web user")
