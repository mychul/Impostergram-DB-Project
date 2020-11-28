import pymongo
from pymongo import MongoClient
import gridfs
import psycopg2
from postdb import post_db
from pathlib import Path

class upload:
    def __init__(self, username):
        self.post = post_db()
        self.cur = None
        self.conn_closed = False

    def uploads(self):
        filename = input("What file would you like to upload from within your Uploads folder?: ")
        pathFile = "/home/team2/Documents/CS179g/project/python/src/Uploads/" + filename + ".jpg"
        myFile = Path(pathFile)
        if(myFile.is_file()):
            numLikes = 0
            description = input("Please enter a description: ")
            cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
            db = cluster["Impostergram"] #specifies the impostergram cluster
            collection = db["fs.files"]
            count = collection.count_documents()
            count = count + 1
            pid = "p" + str(count)
            fs = gridfs.GridFS(db) 
            f = open(pathFile, 'rb')
            img_id=fs.put(f,p_id=pid)
            print("Upload Successful.")
            f.close()
        else:
            print("This filename does not exist inside your folder.  Please try again.")
        return