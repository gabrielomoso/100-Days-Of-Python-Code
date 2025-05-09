import requests


class Post:
    def __init__(self):
        # Getting the full Json from the site
        self.response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
        self.response.raise_for_status()
        self.post = self.response.json()

    def all_post(self):
        return self.post

    def get_post(self, post_number):
        return self.post[post_number]


