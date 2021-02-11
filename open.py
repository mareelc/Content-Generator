# Laura Maree

import wikipedia as wiki

def verify_keywords(keyword1, keyword2):
    if not keyword1 or not keyword2:
        return False
    try:
        article = wiki.page(keyword1, auto_suggest=False, redirect=True).content
        return [True, search_article(article, keyword1, keyword2)]
    except wiki.exceptions.DisambiguationError as e:
        results = list(e.options)
        return [False, results]

def search_article(article, keyword1, keyword2):
    result = list(filter(lambda x: x != '', article.split('\n')))
    not_found = False
    for x in result:
        if keyword1 in x and keyword2 in x:
            return x
    return not_found



