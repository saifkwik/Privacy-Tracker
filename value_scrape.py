from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re


def take_input():
    search_term = input("Enter search term: ").lower()
    if " " in search_term:
        search_term = search_term.replace(" ", "+")
    return search_term


class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


search = take_input()


def value_scrape(page_number):
    dict_obj = my_dictionary()
    for pages in range(1, page_number):
        browser = webdriver.Chrome(executable_path="driver\\chromedriver.exe")
        url = f"https://www.1337x.to/search/{search}/{pages}/"
        browser.get(url)
        html_source = browser.page_source
        browser.close()

        soup = BeautifulSoup(html_source, 'html.parser')

        a = soup(text=" No results were returned. Please refine your search. ")
        if not a:
            pass
        else:
            break

        div = soup.find_all("div", class_="box-info")
        for links in div:
            v = str(links.find_all("a", href=True)).split(', ')

            for elem in v:
                if "/torrent/" in elem:
                    # print(elem)
                    url_pattern = '"(.*?)"'
                    u = re.search(url_pattern, elem)
                    url = u.group().replace('"', '')
                    # print(url)
                    try:
                        name_pattern = '>(.*?)<'
                        n = re.search(name_pattern, elem)
                        name = n.group().replace('<', '').replace('>', '')
                        # print(name)
                    except AttributeError:
                        name_pattern = '>(.*?)'
                        n = re.search(name_pattern, elem)
                        name = n.group().replace('<', '')
                        # print(name)

                    dict_obj.add(name, url)
                    # print(dict_obj)

    return dict_obj

# e = value_scrape(5)
# print(e)
# print(len(e))
