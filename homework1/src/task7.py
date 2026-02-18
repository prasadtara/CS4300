import requests

def get_status_code(url: str, timeout: float = 5.0) -> int:
    """Fetch a URL and return the HTTP status code."""
    resp = requests.get(url, timeout=timeout)
    return resp.status_code


def main() -> None:
    print(get_status_code("https://example.com"))


if __name__ == "__main__":
    main()
