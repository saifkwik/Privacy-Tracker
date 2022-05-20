import pprint

from value_scrape import search
from data_scrape import main
from database import collection


def get_values():
    main()
    print(search)
    t = collection.find({'Search-term': search})
    downloads = []
    seeders = []
    leechers = []
    search_data = []
    for b in t:
        search_data.append(list(b.values())[2])
    search_data = search_data[0]
    # print(len(search_data))
    for x in range(0, len(search_data)):
        downloads.append(int(search_data[x]['Downloads']))
        seeders.append(int(search_data[x]['Seeders']))
        leechers.append(int(search_data[x]['Leechers']))
    # print(downloads)
    # print(seeders)
    # print(leechers)

    print(f'{search}\nVerified Downloads = {sum(downloads)}\nTotal Seeders = {sum(seeders)}\n'
          f'Total Leechers = {sum(leechers)}')


get_values()
