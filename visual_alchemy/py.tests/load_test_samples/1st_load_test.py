from locust import HttpLocust, TaskSet, task
#locust -f 1st_load_test.py --host=http://beta.novartisaml.claimsmapping.com/accounts/login/


class UserBehavior(TaskSet):
    def on_start(self):
        # assume user is at the login page
        self.login()

    def login(self):
        self.client.post("/accounts/login", {"user":"developer", "password":"imagine2"})

    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "http://beta.novartisaml.claimsmapping.com"
    min_wait = 5000
    max_wait = 9000