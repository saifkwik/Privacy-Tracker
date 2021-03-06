import pprint

from data_scrape import main, a_dict
from database import collection
from value_scrape import search


def delete_existing_document():
    myquery = {"Search-term": search}
    x = collection.delete_one(myquery)
    print(x.deleted_count, " documents deleted.")
    return True


def insert_value_inDB():
    for a in a_dict:
        v = collection.update_one({'Search-term': search}, {"$push": {"Results": a}})


def main_func():
    main()
    if delete_existing_document():
        query = {'Search-term': search, 'Results': []}
        r = collection.insert_one(query)
        insert_value_inDB()
    pprint.pprint(a_dict)
    t = collection.find({'Search-term': search})
    downloads = []
    seeders = []
    leechers = []
    search_data = []
    for b in t:
        search_data.append(list(b.values())[2])
    search_data = search_data[0]
    for x in range(0, len(search_data)):
        downloads.append(int(search_data[x]['Downloads']))
        seeders.append(int(search_data[x]['Seeders']))
        leechers.append(int(search_data[x]['Leechers']))

    print(f'{search}\nVerified Downloads = {sum(downloads)}\nTotal Seeders = {sum(seeders)}\n'
          f'Total Leechers = {sum(leechers)}')


main_func()
