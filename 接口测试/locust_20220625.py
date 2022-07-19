from locust import HttpUser, task, between
import os


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hello_world(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            "token": ''}

        url = ''
        response = self.client.get(url, headers=headers)

        key = response.json()['data']

        data = {}

        url_2 = ''
        self.client.post(url_2, headers=headers, json=data)


if __name__ == '__main__':
    os.system(r'locust -f test_20220625.py')
