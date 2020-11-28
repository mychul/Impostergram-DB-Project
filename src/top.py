import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image
import psycopg2
import os
from postdb import post_db

class top:
    def __init__(self,username):
        self.__username=username
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
            while(True):            
                choice = input("What would you like to view?\n1. Top 5 Users\n2. Top 5 Photos by Views\n3. Top 5 Photos by likes\n-1. Return to main menu\n")
                if choice == "-1":
                    clear = lambda: os.system('clear')
                    clear()
                    del clear
                    return
                elif choice=="1": #top 5 users
                    #SELECT * from Users order by numFollows desc limit 5
                    self.cur.execute("SELECT * from Users order by numFollows desc limit 5")
                    topusers=self.cur.fetchall()
                    for row in topusers:
                        print("username: " + str(row[0]))
                        print("Number of followers: " +str(row[3]))
                elif choice=="2": #top 5 photos by views
                    #SELECT * from Photos order by numViews desc limit 5
                    self.cur.execute("SELECT * from Photos order by numViews desc limit 5")
                    topphotoviews=self.cur.fetchall()
                    for row in topphotoviews:
                        print("photo id: " + str(row[0]))
                        print("Number of views: " + str(row[6]))
                elif choice=="3": #top 5 photos  
                    #SELECT * from Photos order by numLikes desc limit 5
                    self.cur.execute("SELECT * from Photos order by numViews desc limit 5")
                    topphotolikes=self.cur.fetchall()
                    for row in topphotolikes:
                        print("photo id: " + str(row[0]))
                        print("Number of likes: " + str(row[5]))
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

        