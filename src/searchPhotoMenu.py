import psycopg2
import os
from postdb import post_db
from photoLikes import photo_likes
from tagged import tagged
from viewComments import view_comments
from comment import comment
import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image
from download import download
from upload import upload

class search_photo:
    def __init__(self, username):
        self.__username = username
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
            #print("Unexpected error. Returning to Main Menu.")
            self.conn_closed = True
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            #print("Closing cursor in close function in search photo")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True
   
    def photo_search(self):
        try:
            pid_choice = "-1"
            loop = True
            while(loop):
                print("1. Search by a tagged username\n2. Search by greater than # of likes\n3. Search by less than # of likes\n4. Search by a specific # of likes\n5. Search by exact date\n6. Search by range of dates\n7. Search by username")
                select = input("Which option do you want to search by? (-1. To Exit): ")

                # For clearing the screen after user choice
                clear = lambda: os.system('clear')
                clear()
                del clear

                if select == "-1":
                    break
                elif select == "1":
                    u_name2 = input("Please enter a tagged user to search: ")
                    self.cur.execute("SELECT photo_id FROM Tagged WHERE username = %s", [u_name2.lower()])
                    result = []
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("user " + u_name2 + " tagged in photo id " + row[0])
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!")                             
                    else:
                        print("That username does not exist.")
                        continue     
                elif select == "2":
                    likes = int( input("Please enter # of likes to search (-1 to Cancel): "))
                    #likes = int(likes)
                    if(likes == -1):
                        break
                    result = []
                    self.cur.execute("SELECT photo_id FROM Photos WHERE numLikes > %s", [likes])
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("photo id " + row[0] + " has numLikes > " + str(likes))
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!") 
                    else:
                        print("No photos found that are greater than that # of likes.")
                        continue
                elif select == "3":
                    likes = int( input("Please enter # of likes to search (-1 to Cancel): "))
                    #likes = int(likes)
                    if(likes == -1):
                        break
                    result = []
                    self.cur.execute("SELECT photo_id FROM Photos WHERE numLikes < %s", [likes])
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("photo id " + row[0] + " has numLikes < " + str(likes))
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!") 
                    else:
                        print("No photos found that are less than that # of likes.")
                        continue
                elif select == "4":
                    likes = int( input("Please enter # of likes to search (-1 to Cancel): "))
                    if(likes == -1):
                        break
                    #likes = int(likes)
                    result = []
                    self.cur.execute("SELECT photo_id FROM Photos WHERE numLikes = %s", [likes])
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("photo id " + row[0] + " has numLikes = " + str(likes))
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!") 
                    else:
                        print("No photos found that are equal to that # of likes.")
                        continue
                elif select == "5":
                    date = input("Please enter a exact date to search by (-1 to Cancel): ")
                    if(date == "-1"):
                        break
                    result = []
                    self.cur.execute("SELECT photo_id FROM Photos WHERE dates = %s", [date])
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("photo id " + row[0] + " uploaded on " + date)
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!") 
                    else:
                        print("No photos found that are greater or equal to that # of likes.")
                        continue
                    
                elif select == "6":
                    date1 = input("Please enter a beginning date of photo uploaded (-1 to Cancel): ")
                    if(date1 == "-1"):
                        break
                    date2 = input("Please enter a ending date of photo uploaded (-1 to Cancel): ")
                    if(date2 == "-1"):
                        break
                    self.cur.execute("SELECT photo_id FROM Photos WHERE dates BETWEEN %s AND %s ", [date1,date2])
                    result = []
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("photo id " + row[0] + " uploaded between " + date1 + " and " + date2)
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("There is no photo that uploaded between both date")
                    else:
                        print("That photo_id does not exist.")
                        continue
                elif select == "7":
                    u_name2 = input("Please enter a username to search: ")
                    self.cur.execute("SELECT photo_id FROM Photos WHERE publisher = %s", [u_name2.lower()])
                    result = []
                    result_pids = self.cur.fetchall()
                    if self.cur.rowcount > 0:
                        for row in result_pids:
                            print("user " + u_name2 + " published photo id " + row[0])
                            result.append(row[0])      
                        correct = False
                        while(not correct):
                            pid_choice = input("Which photo id would you like to see? (-1 to cancel): ")   
                            if(pid_choice == "-1"):
                                correct = True
                                continue
                            if pid_choice in result:
                                return pid_choice  
                            else:
                                print("That photo id does not exist!")                             
                    else:
                        print("That username does not exist.")
                        continue
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
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
                   # print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                if self.post is not None:
                    del self.post
                self.conn_closed = True
                # print("Closing database connection")
        return pid_choice


    def menu(self):
        try:
            loop = True
            pid = self.photo_search()
            view_checked = False
            clear = lambda: os.system('clear')
            clear()
            del clear
            while(loop):
                if(not pid == "-1"):
                    cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
                    db = cluster["Impostergram"] #specifies the impostergram cluster
                    fs = gridfs.GridFS(db) 
                    out_data=fs.get_version(p_id=pid)
                    path = "/home/team2/Documents/CS179g/project/python/src/tmp/tmp.jpg"
                    output = open(path,'wb')
                    output.write(out_data.read())
                    output.close()
                    view = Image.open(path)
                    view.show()

                    if not view_checked:
                        self.cur.execute("SELECT * FROM Views WHERE username = %s AND photo_id = %s", (self.__username, pid))
                        if(self.cur.rowcount < 1):
                            self.cur.execute("INSERT INTO Views (username, photo_id) VALUES (%s, %s)", (self.__username, pid))
                        view_checked = True
                    #the viewer will close 'view'

                if(pid == "-1"):
                   # print("Returning to Main menu")
                    loop = False
                    continue
                choice = input("1. Like the photo\n2. Unlike the photo\n3. Tag a user\n4. Untag a user\n5. View comments\n6. Make a comment\n7. Download the photo onto your local device\nWhat would you like to do with this photo? (-1 to cancel): ")
                clear = lambda: os.system('clear')
                clear()
                del clear
                if(choice == "-1"):
                    loop = False
                    continue
                elif(choice == "1"):
                    photoL = photo_likes(self.__username, pid)
                    if not photoL.conn_closed:
                        photoL.likes()
                        if not photoL.conn_closed:
                            photoL.close_connection()
                    del photoL
                elif(choice == "2"):
                    photoU = photo_likes(self.__username, pid)
                    if not photoU.conn_closed:
                        photoU.unlikes()
                        if not photoU.conn_closed:
                            photoU.close_connection()
                    del photoU
                elif(choice == "3"):
                    tag = tagged(pid)
                    if not tag.conn_closed:
                        tag.tag()
                        if not tag.conn_closed:
                            tag.close_connection()
                    del tag
                elif(choice == "4"):
                    untag = tagged(pid)
                    if not untag.conn_closed:
                        untag.untag()
                        if not untag.conn_closed:
                            untag.close_connection()
                    del untag
                elif(choice == "5"):
                    viewC = view_comments(pid, self.__username)
                    if not viewC.conn_closed:
                        viewC.view()
                        if not viewC.conn_closed:
                            viewC.close_connection()
                    del viewC
                elif(choice == "6"):
                    newC = comment(self.__username, pid)
                    if not newC.conn_closed:
                        newC.commented()
                        if not newC.conn_closed:
                            newC.close_connection()
                    del newC
                elif(choice == "7"):
                    dl = download(pid)
                    dl.downloads()
                    del dl
                else:
                    print("Incorrect input.  Please choose -1 or 1 - 5.\n")
                    loop = True
                    continue
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
        return
