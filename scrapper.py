import requests
from bs4 import BeautifulSoup

url="https://www.ceneo.pl/63490289#tab=reviews"
response=requests.get(url)

page=BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recommendation = opinion.select("span.user-post__author-recomendation").pop(0)
stars = opinion.select_one("span.user-post__score_count")
content = opinion.select_one("div.user-post__text").get_text().strip()
positives = opinion.select("div.review-feature__title--positives ~ div.review-feature__item")
negatives = opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")
likes = opinion.select_one("buttton.vote-yes > span")
dislikes = opinion.select_one("buttton.vote-no > span")
date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
bought = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]


print(positives)