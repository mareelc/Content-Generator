# Laura Maree

import wikipedia as wiki

def verify_keywords(keyword1, keyword2):
    print("yay!")
    verify = wiki.search(keyword1)
    try:
        print(wiki.page(keyword1, auto_suggest=False, redirect=True).html)
    except wiki.exceptions.DisambiguationError as e:
        results = list(e.options)
        return results
def search_wiki(keyword1, keyword2):
    page = wiki.page(keyword1).hmtl
