import pymongo
from pymongo import MongoClient
import gridfs
import psycopg2
from pathlib import Path

class download:
    def __init__(self, pid):
        self.pid = pid

    def downloads(self):
        cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
        db = cluster["Impostergram"] #specifies the impostergram cluster
        fs = gridfs.GridFS(db) 
        filename = input("What would you like to name the file?: ")
        pathFile = "/home/team2/Documents/CS179g/project/python/src/Downloads/" + filename + ".jpg"
        myFile = Path(pathFile)
        if not myFile.is_file():
            out_data=fs.get_version(p_id=self.pid)
            output=open(pathFile,'wb')
            output.write(out_data.read())
            output.close()
            print("Download Successful.  Returning to photo menu.")
        else:
            print("This filename already exists inside your folder.  Please try again.")
        return