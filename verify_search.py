# Laura Maree
# verify_search.py
# 2.24.2021

import wikipedia as wiki
from bs4 import BeautifulSoup
import re

def verify_keywords(keyword1, keyword2):
    """Check for valid keywords and article."""
    if not keyword1 or not keyword2 or " " in keyword1 or " " in keyword2:
        return ["err", "Keywords invalid. \n Try again!"]
    elif wiki.search(keyword1, suggestion=False) == []:
        return ["err", "Article not found. \n Try again!"]
    return find_article(keyword1, keyword1, keyword2)

def find_article(article, keyword1, keyword2):
    """Save article HTML and continue to parse.
    If Disambiguation Error, return list of
    article options to GUI."""
    try:
        found_article = wiki.page(article, auto_suggest=False, redirect=True).html()
        return [True, get_paragraphs(found_article, keyword1.lower(), keyword2.lower())]
    except wiki.exceptions.DisambiguationError as e:
        return [False, list(e.options)]

def get_paragraphs(article, keyword1, keyword2):
    """Using BeautifulSoup, get all paragraphs from html."""
    soup = BeautifulSoup(article, "html.parser")
    text = [p.text for p in soup.find_all("p")]
    return search_paragraphs(text, keyword1, keyword2)

def search_paragraphs(text, keyword1, keyword2):
    """Search each paragraph for both keywords."""
    for string in text:
        if re.search(r"\b" + keyword1 + r"\b", string.lower()) and \
                re.search(r"\b" + keyword2 + r"\b", string.lower()):
            return string
    return False