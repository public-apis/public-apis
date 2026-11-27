import requests


def check_content_type(url: str, expected: str = "application/json") -> bool:
    """
    Validate whether an API endpoint returns the expected Content-Type.

    Args:
        url (str): API endpoint URL.
        expected (str): Expected MIME type (default: "application/json").

    Returns:
        bool: True if the Content-Type matches expectation, else False.

    Examples:
        >>> check_content_type("https://api.github.com", "application/json")
        True
    """
    try:
        response = requests.get(url, timeout=5)
        content_type = response.headers.get("Content-Type", "").lower()

        # Some APIs include charset e.g. "application/json; charset=utf-8"
        return expected.lower() in content_type
    except Exception:
        return False
