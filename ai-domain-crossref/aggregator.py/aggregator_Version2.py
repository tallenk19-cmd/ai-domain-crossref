import os
from social_trends import get_all_social_trends
from news_headlines import get_top_news_trends
from govt_officials_trends import get_all_govt_official_trends
from simpsons_data import get_all_simpsons_keywords

def get_all_trends():
    tw_bearer = os.getenv("TWITTER_BEARER_TOKEN")
    news_api_key = os.getenv("NEWS_API_KEY")
    trends = []

    if tw_bearer:
        trends += get_all_social_trends(tw_bearer)
        trends += get_all_govt_official_trends(tw_bearer)
    if news_api_key:
        trends += get_top_news_trends(news_api_key)
    trends += get_all_simpsons_keywords()
    # Deduplicate, filter length 3-32 chars, lower
    return sorted({t.lower().strip() for t in trends if 3 <= len(t.strip()) <= 32})

def get_trend_sources():
    """Returns dict of {source: keywords}."""
    import os
    tw_bearer = os.getenv("TWITTER_BEARER_TOKEN")
    news_api_key = os.getenv("NEWS_API_KEY")

    from social_trends import get_all_social_trends
    from news_headlines import get_top_news_trends
    from govt_officials_trends import get_all_govt_official_trends
    from simpsons_data import get_all_simpsons_keywords

    return {
        "Social": get_all_social_trends(tw_bearer),
        "News": get_top_news_trends(news_api_key) if news_api_key else [],
        "Govt": get_all_govt_official_trends(tw_bearer),
        "Simpsons": get_all_simpsons_keywords()
    }