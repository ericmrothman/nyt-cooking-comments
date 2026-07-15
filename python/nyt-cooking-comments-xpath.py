from lxml import etree
from curl_cffi import requests
import time
import random
import json
from pprint import pprint
import os

limit = 50

def getPageOfComments(offset, recipe_url):

    api_url = "https://www.nytimes.com/svc/community/V3/requestHandler"
    params = {
        "cmd": "GetCommentsAll", 
        "offset": offset,
        "limit": limit,
        "sort": "reader",
        "url": recipe_url
    }

    comments_page = None

    with requests.Session() as session:
        response = session.get(api_url, params=params, impersonate="chrome110")

        if response.status_code == 200:
            comments_page = response.json()

    return comments_page


def getRawCommentsFromPage(offset, recipe_url):
    comments_page = getPageOfComments(offset, recipe_url)
    
    if comments_page is not None:
        results = comments_page.get('results', {})
        raw_comments = results.get('comments', [])
    else:
        raw_comments = []
        
    return raw_comments


def collectAllComments(recipe_url):
    loop_counter = 0
    offset = 0
    last_page = False
    cleaned_comments = []
    raw_comments = getRawCommentsFromPage(offset, recipe_url)

    while len(raw_comments) != 0:

        print("-"*20)
        print(f"Currently working on page {loop_counter} of the comments. There are {len(raw_comments)} comments on this page.")
        for comment in raw_comments:
            comment_entry = {
                'commentBody' : comment.get('commentBody'),
                'commentType' : comment.get('commentType'),
                'userID' : comment.get('userID'),
                'recommendations' : comment.get('recommendations'),
            }

            cleaned_comments.append(comment_entry)

            replies = comment.get('replies', {})
            for reply in replies:
                reply_entry = {
                    'commentBody' : reply.get('commentBody'),
                    'commentType' : reply.get('commentType'),
                    'userID' : reply.get('userID'),
                    'recommendations' : reply.get('recommendations'),
                }
                cleaned_comments.append(reply_entry)

        if not last_page:
            delay = random.uniform(5.0, 20.0)
            print("-"*20)
            print(f"Waiting for {delay:.2f} seconds...")

            time.sleep(delay)
            loop_counter = loop_counter + 1

            if loop_counter % 15 == 0:
                long_pause = random.uniform(45.0, 120.0)
                print(f"Taking a long break for {long_pause/60:.1f} minutes...")
                time.sleep(long_pause)

        offset += limit

        raw_comments = getRawCommentsFromPage(offset, recipe_url)
        if len(raw_comments) < 25:
            last_page = True

    return cleaned_comments


def scrapeRecipes(recipe_links, file_name):
    dictionary = []
    loop_counter = 0

    for recipe_link in recipe_links:
        with requests.Session() as session:
            session.headers.update({
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,text/css,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            })
            response = session.get(recipe_link, impersonate="chrome110")
            tree = etree.HTML(response.text)

        title_element = tree.find(".//title")
        if title_element is not None:
            title = title_element.text
        else:
            title = "No title found"

        print("-"*20)
        print(f"Found a recipe: {title}")

        author = "No author found"
        h2s = tree.findall('.//h2')
        h2s
        for h2 in h2s:
            if h2 is not None:
                author_links = h2.xpath('./a')
                for author_link in author_links:
                    author = author_link.text
            else:
                author = h2.text

        print("-"*20)
        print(f"Found a recipe author: {author}")

        stats_table = tree.xpath('.//dl[contains(@class, "stats_statsTable")]')
        stats = {}

        if stats_table:
            all_dts = stats_table[0].xpath('.//dt')
            all_dds = stats_table[0].xpath('.//dd')

            for dt, dd in zip(all_dts, all_dds):
                key = dt.xpath('normalize-space(.)')
                value = dd.xpath('normalize-space(.)')

                if key != "Comments":
                    stats[key] = value

        print("-"*20)
        print(f"Found stats: {stats}")

        comments = collectAllComments(recipe_link)

        dictionary.append({
            "url" : recipe_link,
            "title" : title,
            "author" : author,
            "stats" : stats,
            "comments" : comments,
        })

        with open(f"recipe_data_{file_name}.json", "w", encoding="utf-8") as file:
            json.dump(dictionary, file, indent=4)

        delay = random.uniform(5.0, 20.0)
        print("-"*20)
        print(f"Waiting for {delay:.2f} seconds...")

        time.sleep(delay)
        loop_counter += 1

        if loop_counter % 15 == 0:
            long_pause = random.uniform(120.0, 300.0)
            print(f"Taking a long break for {long_pause/60:.1f} minutes...")
            time.sleep(long_pause)

links_to_scrape = {}
if os.path.exists('recipe_links.json'):
    with open('recipe_links.json', 'r') as file:
        links_to_scrape = json.load(file)

for author in links_to_scrape:
    scrapeRecipes(links_to_scrape[author], author)
# scrapeRecipes(links_to_scrape['Melissa Clark'], "Melissa_Clark")
