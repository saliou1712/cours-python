import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
response = requests.get(url)
page = response.content

soup = BeautifulSoup(page, "html.parser")
title = soup.find("title")

print(title.string)
