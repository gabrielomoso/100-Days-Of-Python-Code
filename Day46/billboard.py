from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"


class Billboard:

    def get_songs(self, date):
        """This function gets a list of songs from billboard"""
        response = requests.get(f"{URL}{date}")
        response.raise_for_status()
        content = response.text
        website = BeautifulSoup(content, "html.parser")

        data = [tag.getText().strip() for tag in website.select("li ul li h3")]
        return data
