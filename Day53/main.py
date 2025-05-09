import pprint
from googleDocs import GoogleDocs

import requests
from bs4 import BeautifulSoup
DEFAULT_LINK = "https://www.zillow.com/albuquerque-nm/rentals/?searchQueryState=%7B%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22north%22%3A35.33944923530499%2C%22south%22%3A34.74805564413613%2C%22east%22%3A-106.27289488085938%2C%22west%22%3A-107.00073911914063%7D%2C%22usersSearchTerm%22%3A%224114%20Nigeria%20St%20Sebring%2C%20FL%2033875%22%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A23429%2C%22regionType%22%3A6%7D%5D%2C%22pagination%22%3A%7B%7D%7D"

HEADER = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
response = requests.get(url=DEFAULT_LINK, headers=HEADER)
response.raise_for_status()
content = response.text

website = BeautifulSoup(content, "html.parser")

# Finding all articles
articles = website.find_all('article', {'data-test': 'property-card'})
print("Found all Articles...")
all_data = []
for article in articles:
    address = article.find(name="address").getText().split("|")[-1].strip()
    price = article.find('span', {'class': 'PropertyCardWrapper__StyledPriceLine-srp-8-100-1__sc-16e8gqd-1', 'data-test': 'property-card-price'}).getText().split("+")[0].split("/")[0]
    link = f"https://www.zillow.com{article.find('a')['href']}"
    all_data.append([address, price, link])
print("Created a list of each article data...")
google_docs = GoogleDocs()
google_docs.fill_form(all_data)
print("Congratulations, All data have been submitted.")




