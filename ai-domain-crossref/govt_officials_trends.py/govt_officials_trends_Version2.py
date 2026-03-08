import requests

TWITTER_HANDLES = [
    "POTUS",    # US President
    "VP",       # US Vice President
    "JustinTrudeau",   # Canada PM
    "RishiSunak",      # UK PM
    "EmmanuelMacron",  # France President
]

def fetch_latest_tweets(bearer_token, handle, limit=3):
    """Fetch up to 3 most recent tweets for a given user handle."""
    # Twitter API v1.1 used for compatibility with standard access
    url = f"https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={handle}&count={limit}"
    headers = {'Authorization': f'Bearer {bearer_token}'}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return []
    tweets = resp.json()
    return [t['text'].lower() for t in tweets if 'text' in t]

def get_all_govt_official_trends(bearer_token):
    trends = []
    for handle in TWITTER_HANDLES:
        try:
            trends += fetch_latest_tweets(bearer_token, handle)
        except Exception:
            continue
    # Split into words/short phrases
    flat = []
    for t in trends:
        flat += [w.strip().lower() for w in t.replace(":", " ").replace("-", " ").replace("'", "").split()]
    return [w for w in flat if len(w) > 3]