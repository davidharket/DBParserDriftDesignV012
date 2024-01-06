import requests
from bs4 import BeautifulSoup

def fetch_html(domain):
    try:
        response = requests.get(f'http://{domain}/', timeout=8)
        print("Response collected")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Soup created")
        html = soup.prettify()
        print("HTML prettified")
        return html
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML for {domain}: {e}")
        return None
    