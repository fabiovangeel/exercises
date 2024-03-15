import re
import requests


def extract_urls(url):
    response = requests.get(url)
    html = response.text

    url_patterns = "https?:\/\/[^\s,]+\.(?:jpg|jpeg|png|gif|webp|svg|bmp)"
    urls = re.findall(url_patterns, html)
    return urls


def main():
    url = "https://www.bol.com"
    urls = extract_urls(url)

    for url in urls:
        print(url)


main()
