import requests
from bs4 import BeautifulSoup
import os

DEV_DOMAIN = "http://127.0.0.1:8000"
PROD_DOMAIN = "https://app.liammiller.net"
DEVELOPMENT = os.getenv("ENV", default=False) == "dev"
domain = DEV_DOMAIN if DEVELOPMENT else PROD_DOMAIN


def fetch_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch sitemap: {sitemap_url}")

    xml = BeautifulSoup(response.content, "lxml-xml", from_encoding="utf-8")

    urls = xml.find_all("url")
    locs = []

    for url in urls:

        if xml.find("loc"):
            loc = url.findNext("loc").text
            if DEVELOPMENT:
                loc = DEV_DOMAIN + loc.split("net")[1]
            locs.append(loc)
    return locs


def check_urls(urls):

    errors = []

    for url in urls:
        response = requests.get(url)
        if 400 <= response.status_code <= 500:
            errors.append(url)

    return errors


def main():
    sitemap_url = f"{domain}/sitemap.xml"
    urls = fetch_sitemap_urls(sitemap_url)
    if errors := check_urls(urls):
        print("Found errors at the following URLs:")
        for error in errors:
            print(error)
        exit(1)
    else:
        print(f"No errors found for {domain}. All pages are OK.")


if __name__ == "__main__":
    main()
