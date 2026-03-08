import os
import requests

def is_domain_available_godaddy(domain, api_key=None):
    """
    Uses the GoDaddy Domains API to check domain availability.
    Docs: https://developer.godaddy.com/doc/endpoint/domains#/v1/available
    """
    if api_key is None:
        api_key = os.getenv("GODADDY_API_KEY")
    url = f"https://api.godaddy.com/v1/domains/available?domain={domain}"
    headers = {
        'Authorization': f'sso-key {api_key}',
        'Accept': 'application/json'
    }
    resp = requests.get(url, headers=headers, timeout=8)
    if resp.status_code == 200:
        return resp.json().get('available')
    else:
        print(f"GoDaddy API Error {resp.status_code}: {resp.text}")
        return False