import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority")
db = cluster["Impostergram"]
collection = db["Photos"]

post= {"_id":"p1"}

#collection.insert_one(post)

result = collection.find({"_id":"p1"})

for x in result:
    print(x)