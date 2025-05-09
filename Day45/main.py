import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
contents = response.text

website = BeautifulSoup(contents, "html.parser")

movieList = [tag.getText() for tag in website.find_all(name="h3")[::-1]]
 #starts looping through the list from the End


with open("movie_list.txt", mode="a") as data:
    data.write("Below are a list of the Top 100 Greatest movies of all time\n\n")
    for movie in movieList:
       data.write(f"{movie}\n")


