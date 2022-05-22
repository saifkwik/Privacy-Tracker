import pprint

from value_scrape import value_scrape
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from database import collection
from concurrent.futures import ThreadPoolExecutor

a_dict = value_scrape(5)


def get_urls():
    url_l = []
    for url in a_dict:
        b = url['Url']
        url_l.append(b)
    return url_l


url_list = get_urls()


# print(url_list)
# url = 'https://www.rarbggo.to/torrent/the-kashmir-files-2022-1080p-zee5-10bit-ddp-5-1-x265-hashminer-5252307.html'


def scraped_downloads(url):
    browser = webdriver.Chrome(executable_path="../driver/chromedriver.exe")

    browser.get(url)
    html_source = browser.page_source
    browser.close()

    soup = BeautifulSoup(html_source, 'html.parser')
    div = soup.find_all("td", class_="tlista", id="downloads")
    for e in div:
        e = e.get_text()
        e = e.replace("\n", '').strip()
    for sub in a_dict:
        if sub['Url'] == url:
            sub['Downloads'] = e


def main():
    with ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(scraped_downloads, url_list)

# main()
# scraped_downloads(url)
# pprint.pprint(a_dict)
