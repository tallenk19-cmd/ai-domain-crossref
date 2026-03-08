import requests

def fetch_simpsons_episode_titles():
    """Get Simpsons episode titles using Wikipedia API."""
    # Use the Wikipedia API to get all episode list pages and parse the episode names
    # WARNING: This is a partial, demo implementation for simplicity
    url = "https://en.wikipedia.org/w/api.php?action=parse&format=json&page=List_of_The_Simpsons_episodes"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        # Extract basic episode links from HTML (full parsing would use BeautifulSoup)
        html = data['parse']['text']['*']
        # Naive extraction: get anything between quotes (episode titles are often in quotes)
        import re
        matches = re.findall(r'&quot;([^&]*)&quot;', html)
        titles = [m.lower() for m in matches if 3 <= len(m) <= 64]
    except Exception:
        # As fallback, use static set
        titles = [
            "simpsons roasting on an open fire", "bart the genius", "homer's odyssey", "moaning lisa",
            "the telltale head", "life on the fast lane", "krusty gets busted", "some enchanted evening"
        ]
    return titles

def fetch_simpsons_catchphrases_seeded():
    """Static common Simpsons catchphrases. Extend as needed."""
    return [
        "d'oh", "eat my shorts", "ay caramba", "excellent", "meh", 
        "release the hounds", "woohoo", "don't have a cow", "cowabunga",
        "hail to the chimp", "worst episode ever", "hi-diddly-ho"
    ]

def get_all_simpsons_keywords():
    return fetch_simpsons_episode_titles() + fetch_simpsons_catchphrases_seeded()