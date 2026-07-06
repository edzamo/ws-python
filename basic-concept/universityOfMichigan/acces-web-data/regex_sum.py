"""
Regex sum: read a local file path or a URL, extract all integers, and print their sum and count.

Usage:
  python3 regex_sum.py                # prompts for file or URL
  python3 regex_sum.py <path_or_url>  # runs with provided argument

If the argument starts with 'http', it will be fetched via urllib.
"""

import sys
import re
from urllib.request import urlopen


def read_source(path_or_url):
    if path_or_url.startswith('http://') or path_or_url.startswith('https://'):
        with urlopen(path_or_url) as resp:
            data = resp.read().decode(errors='ignore')
        return data
    else:
        with open(path_or_url, 'r', encoding='utf-8', errors='ignore') as fh:
            return fh.read()


def sum_numbers(text):
    nums = re.findall(r"[0-9]+", text)
    ints = [int(x) for x in nums]
    return sum(ints), len(ints)


def main():
    if len(sys.argv) > 1:
        source = sys.argv[1]
    else:
        source = input('Enter file or URL: ').strip()
        if len(source) == 0:
            source = 'http://py4e-data.dr-chuck.net/regex_sum_2437954.txt'

    try:
        text = read_source(source)
    except Exception as e:
        print('Error reading source:', e)
        sys.exit(1)

    total, count = sum_numbers(text)
    print('Count', count)
    print('Sum', total)


if __name__ == '__main__':
    main()
