import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/impostergram?retryWrites=true&w=majority")
db = cluster["impostergram"]
collection = db["Photos"]

post= {"_id":p1}

collection.insert_one(post)

#result = collection.find({"_id":"p1"})

#for x in result:
    #print(x)