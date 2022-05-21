from pymongo import MongoClient

cluster = ""

client = MongoClient(cluster)

db = client.Torrent_Info

collection = db.rarbg
