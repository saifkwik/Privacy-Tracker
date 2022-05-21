
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

browser = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
url = f"https://www.rarbggo.to/search/2/?search=kashmir%20files"
browser.get(url)
html_source = browser.page_source
browser.close()

soup = BeautifulSoup(html_source, 'html.parser')



div = soup.find_all("table", class_="tablelist2")
for links in div:
    t = links.find_all("td", class_="tlista")
    l = []
    for text in t:
        a = text.get_text()
        # print(a)
        l.append(len(a))
    print(l)

