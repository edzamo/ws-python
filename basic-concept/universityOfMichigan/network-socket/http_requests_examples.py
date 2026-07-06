"""
Examples for HTTP requests and web data access in Python.
"""

import gzip
import ssl
from urllib.request import Request, urlopen


def fetch_page(url):
    print(f"Fetching: {url}")
    context = ssl._create_unverified_context()
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, context=context) as response:
        data = response.read()
        content_encoding = response.headers.get("Content-Encoding", "")
        if content_encoding == "gzip":
            data = gzip.decompress(data)
        body = data.decode("utf-8", errors="ignore")

    print("Status:", response.status)
    print("Content-Type:", response.headers.get_content_type())
    print("First 200 characters:")
    print(body[:200])
    return body


if __name__ == "__main__":
    fetch_page("https://www.python.org")
