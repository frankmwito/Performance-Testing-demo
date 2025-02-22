from locusttest import HttpUser, task, between, tag

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    @tag('home')
    def load_homepage(self):
        self.client.get("/")

    @task(2)
    @tag('shows')
    def load_shows(self):
        self.client.get("/shows/")

    @task(1)
    @tag('about')
    def load_blog(self):
        self.client.get("/about/")