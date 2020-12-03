import pymongo
from pymongo import MongoClient
import gridfs
import psycopg2
from postdb import post_db
from pathlib import Path
from datetime import datetime

class upload:
    def __init__(self, username):
        self.post = post_db()
        self.cur = None
        self.conn_closed = False
        self.username = username

        try:
            #print ("Attempting to make cursor")
            self.cur = self.post.conn.cursor()
            #print ("Successfully created cursor")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
                #print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            #print("Returning to Main Menu.")
            self.conn_closed = True

    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
           # print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True

    def uploads(self):
        try: 
            filename = input("What file would you like to upload from within your Uploads folder?: ")
            pathFile = "/home/team2/Documents/CS179g/project/python/src/Uploads/" + filename + ".jpg"
            myFile = Path(pathFile)
            if(myFile.is_file()):
                description = input("Please enter a description: ")
                now = datetime.now()
                cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
                db = cluster["Impostergram"] #specifies the impostergram cluster
                collection = db["fs.files"]
                count = collection.count_documents({})
                count = count + 1
                pid = "p" + str(count)
                self.cur.execute("INSERT INTO Photos (photo_id, publisher, dates, privacy, description, numLikes, numViews) VALUES (%s, %s, %s, %s, %s, %s, %s)", (pid, self.username, now, str(0), description, str(0), str(0)))
                self.post.conn.commit()
                fs = gridfs.GridFS(db) 
                f = open(pathFile, 'rb')
                img_id=fs.put(f,p_id=pid)
                print("Upload Successful.")
                f.close()
            else:
                print("This filename does not exist inside your folder.  Please try again.")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if not self.conn_closed:
                if self.cur is not None:
                    self.cur.close()
                    #print("Error: Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                if self.post is not None:
                    del self.post
                self.conn_closed = True
            return
        finally: 
            if not self.conn_closed:
                if self.cur is not None:
                    self.cur.close()
                    #print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                if self.post is not None:
                    del self.post
                self.conn_closed = True
        return