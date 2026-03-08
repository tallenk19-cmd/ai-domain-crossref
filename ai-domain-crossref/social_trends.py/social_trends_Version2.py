import os
import requests

def fetch_twitter_trends(bearer_token, woeid=1, limit=10):
    """Fetch trending topics from Twitter/X API."""
    url = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
    headers = {'Authorization': f'Bearer {bearer_token}'}
    resp = requests.get(url, headers=headers, timeout=7)
    trends = resp.json()[0]['trends']
    return [t['name'].strip('#').lower() for t in trends if t['name']][:limit]

def fetch_reddit_trends(limit=10):
    """Fetch hot Reddit topics (titles from r/all)."""
    try:
        resp = requests.get("https://www.reddit.com/r/all/hot.json?limit=25", headers={'User-Agent': 'Mozilla/5.0'})
        posts = resp.json()['data']['children']
        return [p['data']['title'].lower() for p in posts][:limit]
    except Exception:
        return []

def fetch_tiktok_trends_seeded():
    """Seeded TikTok trends; update list regularly or inject API here."""
    # Update this list occasionally or use a paid API
    # Example source: https://influencermarketinghub.com/tiktok-hashtags/
    return [
        "foryou", "fyp", "viral", "trending", "tiktokchallenge",
        "dance", "music", "funny", "comedy", "duet"
    ]

def fetch_instagram_trends_seeded():
    """Seeded Instagram hashtags; update regularly or inject API."""
    # Example source: https://influencermarketinghub.com/instagram-hashtags/
    return [
        "love", "instagood", "fashion", "photooftheday", "art",
        "beautiful", "happy", "cute", "travel", "style"
    ]

def fetch_facebook_trends_seeded():
    """Seeded Facebook trends; update or inject API."""
    # Example from public trend summary articles
    return [
        "covid19", "news", "sports", "memes", "election",
        "happybirthday", "throwback", "support", "sale", "friends"
    ]

def get_all_social_trends(bearer_token):
    trends = []
    try:
        trends += fetch_twitter_trends(bearer_token)
    except Exception:
        pass
    try:
        trends += fetch_reddit_trends()
    except Exception:
        pass
    trends += fetch_tiktok_trends_seeded()
    trends += fetch_instagram_trends_seeded()
    trends += fetch_facebook_trends_seeded()
    # De-duplicate, lowercase, filter short ones
    return sorted({t.strip().lower() for t in trends if len(t.strip()) >= 3})