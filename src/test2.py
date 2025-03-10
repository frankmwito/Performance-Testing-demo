from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1,5)
    
    @task
    def view_homepage(self):
        self.client.get("/")
        print("Hello, frank! am a web user")
        
    @task
    def view_about(self):
        self.client.get("/about")
        print("Hello, frank! am a web user")
        
    @task
    def view_contact(self):
        self.client.get("/contact")
        
    @task
    def view_blog(self):
        self.client.get("/blog")
    
    @task
    def view_shows(self):
        self.client.get("/shows")
        
   
        
    