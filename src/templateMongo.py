import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image
import os

cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
db = cluster["Impostergram"] #specifies the impostergram cluster
fs = gridfs.GridFS(db) 
path = "/home/team2/Documents/CS179g/project/python/src/Downloads"
img_id=fs.put(f,p_id=pid)
    
out_data=fs.get_version(p_id=pid)
output=open(path,'wb')
output.write(out_data.read())