import os
from flask import Flask, render_template_string, request
from dotenv import load_dotenv
from aggregator import get_all_trends, get_trend_sources
from domain_generator import generate_domain_candidates
from godaddy_lookup import is_domain_available_godaddy

load_dotenv()

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <title>Cross-Trend Domain Finder 🌐</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2em; }
      h2 { margin-top: 2em; }
      .src { font-size: .9em; color: #888; }
      .domain { font-weight: bold; font-size: 1.2em; }
      .good { color: green; }
    </style>
  </head>
<body>
  <h1>Cross-Trend Domain Finder 🌐</h1>
  <form method="POST">
      <label for="count"># Domains to Generate and Check:</label>
      <input name="count" type="number" min="5" max="25" value="{{count}}">
      <button>Generate Domains</button>
  </form>
  {% if result %}
    <h2>Available, Cross-Referenced Domains</h2>
    {% for d in result %}
      <div class="domain good">{{d['domain']}}</div>
      <ul>
          {% for src, hits in d['hits'].items() if hits %}
              <li class="src">{{src}}: {{hits}}</li>
          {% endfor %}
      </ul>
    {% endfor %}
  {% endif %}

  <h2>About</h2>
  <p>This AI system cross-references trends and keywords from:</p>
  <ul>
    <li>Top 5 Social Media Platforms: X/Twitter (API), Reddit (API), TikTok/Instagram/Facebook (seeded top hashtags)</li>
    <li>Top News Outlets: CNN, BBC, New York Times (NewsAPI)</li>
    <li>Key Government Officials' Socials (Twitter)</li>
    <li>"The Simpsons": all episode titles and famous catchphrases</li>
  </ul>
  <p>Only <b>available</b> .com domains, 4-10 chars (not counting '.com'), are shown, with cross-source matches.</p>
</body>
</html>
"""

def cross_reference_sources(domain, source_map):
    """Returns {source: [hit, ...]} for this domain string."""
    base = domain.lower().split('.')[0]
    src_hits = {}
    for src, src_words in source_map.items():
        src_hits[src] = [w for w in src_words if w and w in base]
    return src_hits

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    count = int(request.form.get('count', 12))
    all_trends = get_all_trends()
    source_map = get_trend_sources()
    domains = generate_domain_candidates(all_trends, n=count * 2)
    checked = 0
    for d in domains:
        if is_domain_available_godaddy(d):
            hits = cross_reference_sources(d, source_map)
            if sum([bool(H) for H in hits.values()]) >= 2:
                result.append({"domain": d, "hits": hits})
                checked += 1
        if checked >= count:
            break
    return render_template_string(TEMPLATE, result=result, count=count)

if __name__ == "__main__":
    app.run(port=8080, debug=True)