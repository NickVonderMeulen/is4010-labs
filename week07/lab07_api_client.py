def get_api_data(url):
    """Return parsed JSON from url, or None when the request or decoding fails."""
    import requests
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Parse and return JSON data
    except (requests.RequestException, ValueError):
        return None 