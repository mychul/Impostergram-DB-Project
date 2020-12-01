import psycopg2
from postdb import post_db
import os 

#username, photo ID, photo description
class user_search:
    def __init__ (self,username):
        self.__u_name1 = username
        self.post = post_db()
        self.conn = None
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
               # print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
           # print("Returning to Main Menu.")
            self.conn_closed = True
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
          #  print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True
        
    def userSearch(self):
        try:
            loop = True
            while(loop):
                print("1. Search by username\n2. Search by Photo ID\n3. Search by Description\n4. Search by greater than or equal to number of followers\n5. Search by greater than or equal to number of likes\n6. Search by the number of photos published")
                select = input("Which option do you want to search? (-1. To Exit): ")

                # For clearing the screen after user choice
                clear = lambda: os.system('clear')
                clear()
                del clear

                if select == "-1":
                    break
                elif select == "1":
                    u_name2 = input("Please enter a username to search: ")
                    if u_name2 == self.__u_name1:
                        print("That is your username.")
                        continue
                    self.cur.execute("SELECT username FROM Users WHERE username = %s", [u_name2.lower()])
                    if self.cur.rowcount > 0:
                        print(u_name2 + " is an existing user.")
                        repeat = input("Do you want to search for another user? [Y/N]: ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                            #print("You put wrong answer")
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                    else:
                        print("That username does not exist.")
                        continue     
                elif select == "2":
                    photoId = input("Please enter a Photo ID to search: ")
                    self.cur.execute("SELECT publisher FROM Photos WHERE photo_id = %s", [photoId])
                    if self.cur.rowcount > 0:
                        tempString = self.cur.fetchone()
                        print("Publisher of Photo ID " + photoId + " is " + tempString[0])
                        repeat = input("Do you want to search for another user? [Y/N]: ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                            #print("You put wrong answer")
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                    else:
                        print("Photo/User not found.")
                        continue
                elif select == "3":
                    description = input("Please enter a description to search: ")
                    sql = "%" + description + "%"
                    self.cur.execute("SELECT photo_id, publisher FROM Photos WHERE description LIKE %s", [sql])
                    if self.cur.rowcount > 0:
                        result_users = self.cur.fetchall()
                        for row in result_users:
                            print("username: " + row[1] + " found in photo with id: " + row[0])
#                        choice = input("Please check the user from this list")     #start from here
                        repeat = input("Do you want to search for another user? [Y/N]: ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                           # print("You put wrong answer")
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                    else:
                        print("That description does not exist in Photos.")
                        continue
                elif select == "4":
                    
                    fence = input("Enter the number of followers to search by: ")
                    if fence != "0": 
                        self.cur.execute("SELECT username FROM Users WHERE numFollows >= %s", ([fence]))
                        if self.cur.rowcount > 0:
                            result_users = self.cur.fetchall()
                            for row in result_users:
                                print("username: " + row[0])
    #                        choice = input("Please check the user from this list")     #start from here
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                            while(not repeat == "Y" and not repeat == "y"):
                                if(repeat == "N" or repeat == "n"):
                                    loop = False
                                    break
                            # print("You put wrong answer")
                                repeat = input("Do you want to search for another user? [Y/N]: ")
                        else:
                            print("No users found.")
                            continue
                    else:
                        print("Please do not enter zero.")
                        continue
                elif select == "5":
                    
                    fence = input("Enter the number of photo likes to search by: ")
                    if fence != "0": 
                        self.cur.execute("SELECT publisher FROM Photos WHERE numLikes >= %s GROUP BY publisher", ([fence]))
                        if self.cur.rowcount > 0:
                            result_users = self.cur.fetchall()
                            for row in result_users:
                                print("username: " + row[0])
    #                        choice = input("Please check the user from this list")     #start from here
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                            while(not repeat == "Y" and not repeat == "y"):
                                if(repeat == "N" or repeat == "n"):
                                    loop = False
                                    break
                            # print("You put wrong answer")
                                repeat = input("Do you want to search for another user? [Y/N]: ")
                        else:
                            print("No users found.")
                            continue
                    else:
                        print("Please do not enter zero.")
                        continue
                elif select == "6":
                    
                    fence = input("Enter the number of photos published: ")
                    if fence != "0": 
                        self.cur.execute("SELECT COUNT(photo_id), publisher FROM Photos GROUP BY publisher")
                        if self.cur.rowcount > 0:
                            result_users = self.cur.fetchall()
                            for row in result_users:
                                if int(row[0]) >= int(fence):
                                    print("username: " + row[1])
    #                       choice = input("Please check the user from this list")     #start from here
                            repeat = input("Do you want to search for another user? [Y/N]: ")
                            while(not repeat == "Y" and not repeat == "y"):
                                if(repeat == "N" or repeat == "n"):
                                    loop = False
                                    break
                            # print("You put wrong answer")
                                repeat = input("Do you want to search for another user? [Y/N]: ")
                        else:
                            print("No users found.")
                            continue
                    else:
                        print("Please do not enter zero.")
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
        return
