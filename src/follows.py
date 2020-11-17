import psycopg2
from postdb import post_db

class follows:
    def __init__(self,username):
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
            
    def addFollow(self):
        validity = False
        validity_user = False
        try:
            while(not validity):
                u_name2 = input("Please enter a username to Follow : ")
#                cur = self.conn.cursor()
                if u_name2 == self.__u_name1:
                        print("You put yourself! Try it again")
                        continue

                self.cur.execute("SELECT username FROM Users WHERE username = %s",(u_name2))
                if self.cur.rowcount > 0:
                    validity_user = True
                else:
                    print("That username does not exist!")
                    repeat = input("Do you want to enter a username again?[Y/N] : ")
                    while(not repeat == "Y" and not repeat == "y"):
                        if(repeat == "N" or repeat == "n"):
                            break
                            break
                        print("You put wrong answer")
                        repeat = input("Do you want to enter a username again?[Y/N] : ")                    
                if validity_user:
                    self.cur.execute("SELECT * FROM Follows WHERE username1 = %s, username2 = %s", (self.__u_name1, u_name2))
                    if self.cur.rowcount > 0:
                        print("You already followed %s", u_name2)
                    else:
                        self.cur.execute("INSERT INTO Follows(username1,username2) VALUES(%s, %s)", (self.__u_name1, u_name2))
                    valitidy = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")
    def delFollow(self):
        validity = False
        validity_user = False
        try:
            while(not validity):
                u_name2 = input("Please enter a username to Unfollow : ")
                if u_name2 == self.__u_name1:
                        print("You put yourself! Try it again")
                        continue
#                cur = self.conn.cursor()
                self.cur.execute("SELECT * FROM Follows WHERE username1 = %s, username2 = %s",(self.__u_name1, u_name2))
                if self.cur.rowcount > 0:
                    validity = True
                else:
                    print("That follow does not exist!")
                    repeat = input("Do you want to enter a username again?[Y/N] : ")
                    while(not repeat == "Y" and not repeat == "y"):
                        if(repeat == "N" or repeat == "n"):
                            break
                            break
                        print("You put wrong answer")
                        repeat = input("Do you want to enter a username again?[Y/N] : ")                    
                if validity:
                    self.cur.execute("DELETE * FROM Follows WHERE username1 = %s, username2 = %s", (self.__u_name1, u_name2))
                    validity = False
                    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")