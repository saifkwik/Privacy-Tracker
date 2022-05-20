from pymongo import MongoClient

cluster = ""

client = MongoClient(cluster)

db = client.Torrent_Info

collection = db.thirteen_thirtysevenX
# query = {'Search-term':"1337x search", 'Results': []}
# r = collection.insert_one(query)