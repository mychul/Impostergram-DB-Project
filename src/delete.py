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

    def uploads(self):
        try: 
            print          
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