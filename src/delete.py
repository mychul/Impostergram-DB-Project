import pymongo
from pymongo import MongoClient
import gridfs
import psycopg2
from postdb import post_db
from pathlib import Path
from datetime import datetime

class delete:
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

    def delete(self):
        try: 
            target = input("What is the id of the photo you wish to delete. (-1 to cancel): ")
            if input == "-1":
                return
            self.cur.execute("SELECT photo_id FROM Photos WHERE photo_id = %s AND publisher = %s",(target,self.username))
            if self.cur.rowcount>0:
                print("Found photo id:" +str(target))
                self.cur.execute("DELETE FROM Photos WHERE photo_id = %s",[target])
                self.conn.commit()
                cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
                db = cluster["Impostergram"]
                fs = gridfs.GridFS(db)
                result= fs.find_one({"p_id":target})
                id=result['_id']
                fs.delete(id)
            else:
                print("Photo id: "+str(target)+" was not found or is not owned by you.")
                return
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