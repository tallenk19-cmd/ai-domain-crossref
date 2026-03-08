# Cross-Trend AI Domain Finder

Finds AVAILABLE .com domains (4-10 chars) inspired by combined trends from top social media, news, government social posts, and every episode of The Simpsons!

## Features

- Aggregates keywords/trends from:
  - Top 5 Social Media Sites: X/Twitter, Reddit, TikTok, Instagram, Facebook
  - Top 3 News Outlets: CNN, BBC, NYTimes (via NewsAPI)
  - Key Government Officials (Twitter)
  - All Simpsons episode titles and catchphrases (Wikipedia)
- AI-powered trendy domain name generation (OpenAI GPT-3.5)
- Checks domain availability (GoDaddy API)
- Shows which sources each domain matches

## Quick Start

1. **Clone/download repository** and enter directory:
    ```
    git clone <repo-url>
    cd ai-domain-crossref
    ```

2. **Install requirements**:
    ```
    pip install -r requirements.txt
    ```

3. **Configure your secrets**:
    - Copy `.env.example` to `.env`
    - Fill in `OPENAI_API_KEY` (from https://platform.openai.com/)
    - Fill in `TWITTER_BEARER_TOKEN` (Twitter/X developer portal)
    - Fill in `GODADDY_API_KEY` (GoDaddy developer portal)
    - Fill in `NEWS_API_KEY` (https://newsapi.org/)

4. **Run locally**:
    ```
    python app.py
    ```

5. **Or build and run with Docker**:
    ```
    docker build -t domain-crossref .
    docker run --env-file .env -p 8080:8080 domain-crossref
    ```

6. **Visit [http://localhost:8080](http://localhost:8080) in your web browser!**

## Customization

- Edit `TWITTER_HANDLES` in `govt_officials_trends.py` to track different world leaders.
- For TikTok/Instagram/Facebook: Update the seeded trend lists as often as you like; API integrations can be added where possible later.

## Limitations

- Instagram, Facebook, and TikTok trend APIs are not open; seed lists only.
- Simpsons episode title extraction is a best effort from Wikipedia; it can be upgraded with better parsing or the Kaggle Simpsons dataset.
- All APIs subject to rate limits and terms of use.

**Enjoy your data-driven, meme-powered, Simpsons-flavored domain creation!**