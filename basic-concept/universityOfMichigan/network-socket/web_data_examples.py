"""
Examples for reading and processing web data in Python.
"""

import re
import ssl
from urllib.request import Request, urlopen


def fetch_and_decode(url):
    print(f"Fetching: {url}")
    context = ssl._create_unverified_context()
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, context=context) as response:
        html_bytes = response.read()

    html_text = html_bytes.decode("utf-8")
    print("Decoded text length:", len(html_text))
    return html_text


def print_first_lines(text, lines=5):
    print("First lines of the page:")
    for line in text.splitlines()[:lines]:
        print(line)
    print()


def extract_links(text):
    links = re.findall(r'href="([^"]+)"', text)
    print("Links found:")
    for link in links[:10]:
        print("-", link)
    print()
    return links


if __name__ == "__main__":
    url = "https://www.python.org"
    page = fetch_and_decode(url)
    print_first_lines(page)
    extract_links(page)
