from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1,5)
    
    @task
    @task('home')
    def view_homepage(self):
        self.client.get("/")
        print("Hello, frank! am a web user")
        
    @task
    @task('about')
    def view_about(self):
        self.client.get("/about")
        print("Hello, frank! am a web user")
        
    @task
    @task('contact')
    def view_contact(self):
        self.client.get("/contact")
        
    @task
    @task('blog')
    def view_blog(self):
        self.client.get("/blog")
    
    @task
    @task('shows')
    def view_shows(self):
        self.client.get("/shows")
        
   
        
    