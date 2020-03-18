#import bibliotek
import requests
from bs4 import BeautifulSoup

#adres URL przykłdowej strony z opiniami
url = "https://www.ceneo.pl/7468416#tab=reviews"

#pobranie kodu HTML strony z podanego URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text, 'html.parser')

#wydobycie z kodu HTML strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych dla pojedynczej opinii
opinion = opinions.pop()

for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.find("div", "reviewer-name-line").string
    recommendation = opinion.find("div", "product-review-summary").find("em").string
    stars = opinion.find("span", "review-score-count").string
    try:
        purchased = opinion.find("div", "product-review-pz").string
    except AttributeError:
        purchased = None
    try:
        dates = opinion.find("span", "reviev-time").find_all("time")
    except AttributeError:
        dates = None
    try:
        review_date = dates.pop(0)["datetime"]
    except AttributeError:
        review_date = None
    try:
        purchase_date = dates.pop(0)["datetime"]
    except AttributeError:
        purchase_date = None
    useful = opinion.find("button", "vote-yes").find("span").string
    useless = opinion.find("button", "vote-no").find("span").string
    content = opinion.find("p", "product-review-body").get_text()
    try:
        pros = opinion.find("div", "pros-cell").find("ul").get_text()
    except AttributeError:
        pros = None
    try:
        cons = opinion.find("div", "cons-cell").find("ul").get_text()
    except AttributeError:
        cons = None
    print(opinion_id, stars, content, author, pros, cons, useful, useless, purchased, purchase_date, review_date)