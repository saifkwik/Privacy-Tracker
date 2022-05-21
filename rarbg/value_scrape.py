import pprint

from thirteen_thirtysevenX.value_scrape import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

search = search
if "+" in search:
    search = search.replace("+", "%20")


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


def value_scrape(page_number):
    dict_obj = my_dictionary()
    for pages in range(1, page_number):
        browser = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
        url = f"https://www.rarbggo.to/search/{pages}/?search={search}"
        browser.get(url)
        html_source = browser.page_source
        browser.close()

        soup = BeautifulSoup(html_source, 'html.parser')
        # print(soup)

        div = soup.find_all("table", class_="tablelist2")

        for x in div:
            t = x.find_all("td", class_="tlista")
            l = []
            for text in t:
                a = text.get_text()
                # print(a)
                l.append(len(a))
        if not l:
            break

        for links in div:
            v = str(links.find_all("td", class_="tlista")).split(('>'))
            # print(v)
            for elem in v:
                if "/torrent/" in elem:
                    url_pattern = 'href="(.*?)"'
                    u = re.search(url_pattern, elem)
                    url = u.group().replace('href=', '').replace('"', '')
                    name_pattern = 'title="(.*?)"'
                    n = re.search(name_pattern, elem)
                    name = n.group().replace('title=', '').replace('"', '').replace(" torrent", '')
                    dict_obj.add(name, url)
        if dict_obj == {}:
            break
    pprint.pprint(dict_obj)
    print(len(dict_obj))
    return dict_obj


# value_scrape(5)
