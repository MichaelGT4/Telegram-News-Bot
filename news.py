import requests
from sys import argv

url = ('https://newsapi.org/v2/top-headlines?')

api_key = '3e22a7d0062c4c44b771d7897a9d8aa3'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "ve",
        "apiKey": api_key
    }
    return _get_articles(query_parameters)


def get_artciles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "do",
        "apiKey": api_key
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(url, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    return results

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "es",
        "apiKey": api_key
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        print(source['name'])
        print(source['url'])


if __name__ == "__main__":
    # print(f"Getting news for {argv[1]}...\n")
    # get_articles_by_category('business')
    print(f"Successfully retrieved top  headlines")
    # get_artciles_by_query("a")
    print(get_articles_by_category('business'))
    #print_sources_by_category("technology")
