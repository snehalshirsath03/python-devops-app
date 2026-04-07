from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def test_app(self):
        self.client.get("/")
