# Laura

import wikipedia as wiki
from bs4 import BeautifulSoup

def verify_keywords(keyword1, keyword2):
    if not keyword1 or not keyword2:
        return "keywords invalid"
    if " " in keyword1 or " " in keyword2:
        return "keywords invalid"
    if wiki.search(keyword1, suggestion=False) == []:
        return "not found"
    return find_article(keyword1, keyword2)

def find_article(keyword1, keyword2):
    try:
        article = wiki.page(keyword1, auto_suggest=False, redirect=True).html()
        return [True, parse(article, keyword1, keyword2)]
    except wiki.exceptions.DisambiguationError as e:
        results = list(e.options)
        return [False, results]

def parse(article, keyword1, keyword2):
    soup = BeautifulSoup(article, 'html.parser')
    text = [p.text for p in soup.find_all("p")]
    not_found = False
    for x in text:
        if (keyword1.lower() in x.lower()) and (keyword2.lower() in x.lower()):
            return x
    return not_found

