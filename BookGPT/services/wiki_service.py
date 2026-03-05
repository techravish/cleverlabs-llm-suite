import requests

def fetch_wikipedia_summary(place):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{place}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("extract", "No summary available for this place.")
    except requests.RequestException:
        return "Error fetching data from Wikipedia."