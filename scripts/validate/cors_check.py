import requests


def supports_cors(url: str) -> bool:
    """
    Check if an API endpoint supports CORS by examining the response headers.

    Args:
        url (str): API base URL to check.

    Returns:
        bool: True if CORS headers are present, False otherwise.

    Examples:
        >>> supports_cors("https://api.github.com")
        True
        >>> supports_cors("https://example.com")
        False
    """
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Check common CORS headers
        return (
            "Access-Control-Allow-Origin" in headers
            or "Access-Control-Allow-Credentials" in headers
            or "Access-Control-Allow-Headers" in headers
        )
    except Exception:
        return False
