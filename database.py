from pymongo import MongoClient

cluster = "mongodb+srv://rango:ylEEDSikq33TLyKx@cluster0.jbwqp.mongodb.net/Torrent_Info?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.Torrent_Info

collection = db.thirteen_thirtysevenX
# query = {'Search-term':"1337x search", 'Results': []}
# r = collection.insert_one(query)