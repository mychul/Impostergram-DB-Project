import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image
import psycopg2
import os
from postdb import post_db

class feed:
    def __init__(self,username):
        self.username=username
        self.post = post_db()
        self.cur = None
        self.conn_closed = False
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
            #print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True

    def display(self):# displays top 5 users and photos
        #Ask the user to display top user by follows, top photo by views, top photo by likes.
        try:
            self.cur.execute("SELECT username2 from Follows WHERE username1 =%s",([self.username]))   
            followedusers=self.cur.fetchall()    
            while(True):  
                choice = input("Sort your feed by: \n1. Views\n2. Likes\n-1. Return to main menu\n")
                
                if choice == "-1":
                    clear = lambda: os.system('clear')
                    clear()
                    del clear
                    return
                        
                elif choice=="1": #sort by views
                    
                    for x in followedusers:
                        self.cur.execute("SELECT photo_id from Photos WHERE publisher = %s order by numViews desc limit 1",([x[0]]))
                        resultpid=self.cur.fetchone()
                        print("User " + x[0] + "'s most popular photo is "+ str(resultpid[0]))  

                elif choice=="2": #sort by likes  
                    
                    for x in followedusers:
                        self.cur.execute("SELECT photo_id from Photos WHERE publisher = %s order by numLikes desc limit 1",([x[0]]))
                        resultpid=self.cur.fetchone()
                        print("User " + x[0] + "'s best photo is "+ str(resultpid[0]))
                    
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
                # print("Closing database connection")