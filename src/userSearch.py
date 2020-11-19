import psycopg2
from postdb import post_db

#username, photo ID, photo description
class user_search:
    def __init__ (self,username):
        __u_name1 = username
        post = post_db()
        cur = post.conn.cursor()
        conn = None

    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        del self.post
        
    def userSearch(self):
        validity_user = False
        validity_photo = False
        validity_description = False
        try:
            loop = True
            while(loop):
                print("1. Search by username\n2. Search by Photo ID\n3. Search by Description")
                select = input("Which option do ou want to search? : ")
                if select == 1:
                    u_name2 = input("Please enter a username to search : ")
                    if u_name2 == self.__u_name1:
                        print("It is your username!\nStart the search again!")
                        continue
                    self.cur.execute("SELECT username FROM Users WHERE username = %s",(u_name2))
                    if self.cur.rowcount > 0:
                        validity_user = True
                        print("%s exists in username list!", u_name2)
                        repeat = input("Do you want to search the user again?[Y/N] : ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                            print("You put wrong answer")
                            repeat = input("Do you want to search the user again?[Y/N] : ")
                    else:
                        print("that username does not exist!\nStart the search again!")
                        continue     
                elif select == 2:
                    photoId = input("Please enter a Photo ID to search : ")
                    self.cur.execute("SELECT publisher FROM Photos WHERE photo_id = %s",(photoId))
                    if self.cur.rowcount > 0:
                        validity_photo = True
                        print("Publisher of Photo ID %s is %s", photoId, self.cur.fetch_one())
                        repeat = input("Do you want to search the user again?[Y/N] : ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                            print("You put wrong answer")
                            repeat = input("Do you want to search the user again?[Y/N] : ")
                    else:
                        print("that username does not exist!\nStart the search again!")
                        continue
                elif select == 3:
                    description = input("Please enter a description to search : ")
                    self.cur.execute("SELECT publisher FROM Photos WHERE description LIKE %s", (description))
                    if self.cur.rowcount > 0:
                        validity_description = True
                        result_users = self.cur.fetchall()
                        result = []
                        for row in result_users:
                            print("username : " + str(row[0] + "\n"))
                            result.append(row[0])
#                        choice = input("Please check the user from this list")     #start from here
                        repeat = input("Do you want to search the user again?[Y/N] : ")
                        while(not repeat == "Y" and not repeat == "y"):
                            if(repeat == "N" or repeat == "n"):
                                loop = False
                                break
                            print("You put wrong answer")
                            repeat = input("Do you want to search the user again?[Y/N] : ")
                    else:
                        print("That description does not exist in Photos!\nStart the new search again!")
                        continue
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            return
        finally: 
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            # print("Closing database connection")
