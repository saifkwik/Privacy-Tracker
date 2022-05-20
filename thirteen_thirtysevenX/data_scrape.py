import pprint

from value_scrape import value_scrape, search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from database import collection
from concurrent.futures import ThreadPoolExecutor

base_1337x = "https://www.1337x.to"

my_dict = value_scrape(5)
# print(my_dict)

# query = {'Search-term': search, 'Results': []}
# r = collection.insert_one(query)

url_list = list(my_dict.values())


def scraped_data(url):

    final_url = base_1337x + url
    print(final_url)

    for key, value in my_dict.items():
        if value == url:
            name = key

    browser = webdriver.Chrome(executable_path="../driver/chromedriver.exe")

    browser.get(final_url)
    html_source = browser.page_source
    browser.close()

    soup = BeautifulSoup(html_source, 'html.parser')

    div = soup.find_all("div", class_="col-9 page-content")
    for links in div:
        v = links.find_all("ul", class_="list")
        for x in v:
            y = x.get_text().split('\n')
            # print(y)
            for elements in y:
                if "Category" in elements:
                    Category = elements.replace('Category', '').strip()
                elif "Type" in elements:
                    Type = elements.replace('Type', '').strip()
                elif "Language" in elements:
                    Language = elements.replace('Language', '').strip()
                elif "Total size" in elements:
                    Total_size = elements.replace('Total size', '').strip()
                elif "Uploaded By" in elements:
                    Uploaded_by = elements.replace('Uploaded By', '').strip()
                elif "Downloads" in elements:
                    Downloads = elements.replace('Downloads', '').strip()
                elif "Last checked" in elements:
                    Last_checked = elements.replace('Last checked', '').strip()
                elif "Date uploaded" in elements:
                    Date_uploaded = elements.replace('Date uploaded', '').strip()
                elif "Seeders" in elements:
                    Seeders = elements.replace('Seeders', '').strip()
                elif "Leechers" in elements:
                    Leechers = elements.replace('Leechers', '').strip()
        data = {"Name": name, "Url": final_url, "Category": Category, "Type": Type, "Language": Language,
                "Total_size": Total_size,
                "Uploaded_by": Uploaded_by, "Downloads": Downloads, "Last_checked": Last_checked,
                "Date_uploaded": Date_uploaded, "Seeders": Seeders, "Leechers": Leechers}
        pprint.pprint(data)
    v = collection.update_one({'Search-term': search}, {"$push": {"Results": data}})


# for urls in url_list:
#     scraped_data(urls)


def main():
    with ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(scraped_data, url_list)

    document = collection.find({'Search-term': "1337x search"})
    for info in document:
        pprint.pprint(info)

# main()
