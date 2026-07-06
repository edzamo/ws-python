"""
Examples for web scraping with BeautifulSoup.
"""

import ssl
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def fetch_html(url):
    print(f"Fetching: {url}")
    context = ssl._create_unverified_context()
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, context=context) as response:
        html = response.read().decode("utf-8")
    return html


def parse_links(html):
    soup = BeautifulSoup(html, "html.parser")
    print("Title:", soup.title.get_text(strip=True) if soup.title else "No title")

    links = []
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href:
            links.append(href)

    print("Links found:")
    for link in links[:10]:
        print("-", link)

    return links


if __name__ == "__main__":
    url = "https://www.python.org"
    html = fetch_html(url)
    parse_links(html)
