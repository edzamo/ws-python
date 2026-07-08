import urllib.request

url = "http://data.pr4e.org/intro-short.txt"
with urllib.request.urlopen(url) as response:
    headers = response.info()
    for header in ['Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type']:
        print(f"{header}: {headers.get(header)}")