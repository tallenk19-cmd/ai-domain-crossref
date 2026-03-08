import openai
import os
import random
import string

def generate_domain_candidates(trends, n=20):
    """
    Use OpenAI GPT-3.5 to generate trendy .com domain names, or fallback to a simple generator if key missing.
    """
    key = os.getenv('OPENAI_API_KEY')
    if not key:
        return simple_domain_candidates(trends, n)
    openai.api_key = key

    trend_string = ", ".join(trends[:20])
    prompt = (
        f"Create {n} short, pronounceable, creative dot-com (.com) domain names, inspired by these keywords: {trend_string}. "
        "Each name should be 4 to 10 letters (not including the .com), use only English letters, and avoid generic words like 'domain' or 'website'. Output the names separated by commas."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
        temperature=0.95
    )
    raw = response.choices[0].message.content
    # Split by commas and clean up
    domains = [d.strip().lower() for d in raw.replace('.com', '').replace('\n', '').split(',')]
    domains = [d + ".com" for d in domains if 4 <= len(d) <= 10 and d.isalpha()]
    if not domains:
        return simple_domain_candidates(trends, n)
    return list(dict.fromkeys(domains))[:n]

def simple_domain_candidates(trends, n=20):
    """
    Combine random trend parts as fallback.
    """
    result = set()
    chars = string.ascii_lowercase
    while len(result) < n:
        base = random.choice(trends)
        tail = ''.join(random.choices(chars, k=random.randint(1, 5)))
        name = (base[:8] + tail)[:10]
        if 4 <= len(name) <= 10:
            result.add(name + ".com")
    return list(result)