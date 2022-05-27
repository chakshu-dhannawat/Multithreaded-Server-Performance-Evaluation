from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def on_login(self):
        response = self.client.get('student/studentlogin')
        csrftoken = response.cookies['csrftoken']
        self.client.post('student/studentlogin',
                         {'username': 'jaimin', 'password': 'jaimin'},
                         headers={'X-CSRFToken': csrftoken})
        self.client.get("student/start-exam/1")
        self.client.get("student/view-result")  