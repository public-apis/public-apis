import requests


def supports_https(url: str) -> bool:
    """
    Check whether the given API endpoint supports HTTPS.

    Args:
        url (str): API base URL

    Returns:
        bool: True if HTTPS is supported, else False

    Examples:
        >>> supports_https("https://google.com")
        True
        >>> supports_https("http://example.com")
        False
    """
    if not url.startswith(("http://", "https://")):
        return False

    https_url = url.replace("http://", "https://")

    try:
        response = requests.get(https_url, timeout=5)
        return response.status_code < 500
    except Exception:
        return False
