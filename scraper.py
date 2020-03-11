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

opinion_id = opinion["data-entry-id"]
author = opinion.find("div", "reviewer-name-line").string
recommendation = opinion.find("div", "product-review-summary").find("em").string
stars = opinion.find("span", "review-score-count").string
purchased = opinion.find("div", "product-review-pz").string
# - data wystawienia: span.review-time > time["datetime"] - pierwszy element listy
# - data zakupu: span.review-time > time["datetime"] - drugi element listy
useful = opinion.find("button", "vote-yes").find("span").string
useless = opinion.find("button", "vote-no").find("span").string
content = opinion.find("p", "product-review-body").get_text()
# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul