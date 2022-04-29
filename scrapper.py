from re import T
import requests
from bs4 import BeautifulSoup
import json

all_opinions=[]
url="https://www.ceneo.pl/63490289#tab=reviews"
while(url):
    response=requests.get(url)

    page=BeautifulSoup(response.text, 'html.parser')


    opinions = page.select("div.js_product-review")
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            recommendation=None
        stars = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text().strip()
        pros = [item.get_text() for item in opinion.select("div.review-feature__title--positives ~ div.review-feature__item")]
        cons = [item.get_text() for item in opinion.select("div.review-feature__title--negatives ~ div.review-feature__item")]
        likes = opinion.select_one("button.vote-yes > span").get_text().strip()
        dislikes = opinion.select_one("button.vote-no > span").get_text().strip()
        date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            bought = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            bought=None

        single_opinion = {
            "opinion_id" : opinion_id,
            "author" : author,
            "recommendation":recommendation,
            "stars" : stars,
            "content" : content,
            "pros" : pros,
            "cons" : cons,
            "likes" : likes,
            "dislikes" : dislikes,
            "date" : date,
            "bought" : bought
        }
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl/" + page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None
with open("opinions/63490289.json", "w",encoding="UTF-8") as jf:
    json.dump(all_opinions, jf, indent=4, ensure_ascii=False)