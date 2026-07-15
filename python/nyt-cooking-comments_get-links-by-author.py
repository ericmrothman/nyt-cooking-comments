from lxml import etree
from curl_cffi import requests
import time
import random
import json
from pprint import pprint
import os

with requests.Session() as session:
    session.headers.update({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,text/css,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    })
    response = session.get('https://cooking.nytimes.com/about-us', impersonate="chrome110")
    tree = etree.HTML(response.text)

sections = tree.xpath('.//article[contains(@class, "authorcard")]')
author_pages = {}

for section in sections:
    link_element = section.xpath('./a')[0]
    current_link = link_element.get('href')
    author_name = link_element.xpath('./p')[0].text

    if current_link:
        current_link = "https://cooking.nytimes.com" + current_link
        author_pages[author_name] = current_link


def collectLinks(pages):
    loop_counter = 0

    master_links_dictionary = {}
    if os.path.exists('recipe_links.json'):
        with open('recipe_links.json', 'r') as file:
            master_links_dictionary = json.load(file)

    for page in pages:
        print(pages[page])

        if page not in master_links_dictionary:
            master_links_dictionary[page] = []

        with requests.Session() as session:
            session.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,text/css,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            })
            response = session.get(pages[page], impersonate="chrome110")
            tree = etree.HTML(response.text)

        sections = tree.findall('.//a')

        for section in sections:
            current_link = section.get('href')
            if current_link and current_link.startswith("/recipe"):
                current_link = "https://cooking.nytimes.com" + current_link

                if current_link not in master_links_dictionary[page]:
                    master_links_dictionary[page].append(current_link)

        print("-"*20)
        print(f"Grabbed {len(master_links_dictionary[page])} recipes from {pages[page]}.")

        with open('recipe_links.json', 'w') as file:
            json.dump(master_links_dictionary, file, indent=4)

        delay = random.uniform(5.0, 20.0)
        print("-"*20)
        print(f"Waiting for {delay:.2f} seconds...")

        time.sleep(delay)
        loop_counter += 1

collectLinks(author_pages)