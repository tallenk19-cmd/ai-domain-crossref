import requests

def fetch_newsapi_headlines(api_key, sources=None, limit=10):
    """Fetch headlines from NewsAPI.org for given sources."""
    url = ("https://newsapi.org/v2/top-headlines?"
           "pageSize={}&apiKey={}").format(limit, api_key)
    if sources:
        url += "&sources=" + ",".join(sources)
    resp = requests.get(url)
    if resp.status_code != 200:
        return []
    headlines = [a['title'] for a in resp.json().get('articles', [])]
    # Split headlines into key words/phrases by common delimiters
    flat = []
    for h in headlines:
        flat += [w.strip().lower() for w in h.replace(":", " ").replace("-", " ").replace("'", "").split()]
    return [w for w in flat if len(w) > 3]

def get_top_news_trends(news_api_key):
    # Popular NewsAPI sources: 'cnn', 'bbc-news', 'the-new-york-times'
    return fetch_newsapi_headlines(
        news_api_key,
        sources=['cnn', 'bbc-news', 'the-new-york-times'],
        limit=12
    )