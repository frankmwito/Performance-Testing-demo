
from locust import HttpUser, task, between, TaskSet


class MyTaskSet(TaskSet):
    def web(self):
        print("am a web user")
    def mobile(self):
        print("am a mobile")


class MywebUser(HttpUser):
    wait_time = between(1, 2)
    
    tasks = [MyTaskSet]