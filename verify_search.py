# Laura Maree
# Verify keys/Find Article/Parse
# 2.12.2021

import wikipedia as wiki
from bs4 import BeautifulSoup

def verify_keywords(keyword1, keyword2):
    """Check for valid keywords."""
    # Empty input.
    if not keyword1 or not keyword2:
        return "keywords invalid"

    # Multiple keywords or spaces.
    if " " in keyword1 or " " in keyword2:
        return "keywords invalid"

    # No article found.
    if wiki.search(keyword1, suggestion=False) == []:
        return "not found"

    # Call to find_article to process.
    return find_article(keyword1, keyword2)

def find_article(keyword1, keyword2):
    """
    Save article HTML and continue to parse.
    If Disambiguation Error, return list of
    article options to GUI.
    :param keyword1: input key 1
    :param keyword2: input key 2
    :return: Parsed article or disambiguation error list.
    """
    try:
        article = wiki.page(keyword1, auto_suggest=False, redirect=True).html()
        return [True, parse(article, keyword1, keyword2)]
    except wiki.exceptions.DisambiguationError as e:
        results = list(e.options)
        return [False, results]

def parse(article, keyword1, keyword2):
    """Parse article HTML and search for paragraph with keywords."""
    soup = BeautifulSoup(article, 'html.parser')

    # Save all <p> tag text.
    text = [p.text for p in soup.find_all("p")]
    not_found = False

    # Search each paragraph for both keywords and return first, else False.
    for x in text:
        if (keyword1.lower() in x.lower()) and (keyword2.lower() in x.lower()):
            return x
    return not_found

