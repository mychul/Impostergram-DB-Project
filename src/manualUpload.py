import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image
import os

cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
db = cluster["Impostergram"] #specifies the impostergram cluster
collection = db["Photos"] #specifies the photos collection
fs = gridfs.GridFS(db) 
count=1

for filename in os.listdir("/home/team2/Documents/CS179g/project/python/src/Img"):
   with open(os.path.join("/home/team2/Documents/CS179g/project/python/src/Img", filename), 'rb') as f:
       pid="p"+str(count)
       img_id=fs.put(f,p_id=pid)
       
       out_data=fs.get_version(p_id=pid)
       result="result"+ str(count) +".jpg"
       output=open(result,'wb')
       output.write(out_data)
       view = Image.open(result)
       view.show
       count=count+1
