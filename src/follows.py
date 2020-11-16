import psycopg2
from postdb import post_db

class follows:
    def __init__(self,username):
        __u_name1 = username
        post = post_db()
        cur = post.conn.cursor()
        conn = None
            
    def addFollow(self):
        validity = False
        try:
            while(not validity):
                u_name2 = input("Please enter a username to follow : ")
#                cur = self.conn.cursor()
                self.cur.execute("SELECT username FROM Users WHERE username = %s",(u_name2))
                if self.cur.rowcount > 0:
                    validity = True
                else:
                    print("That username does not exist!")
                    repeat = input("Do you want to enter a username again?[Y/N] : ")
                    while(not repeat == "Y" and not repeat == "y"):
                        if(repeat == "N" or repeat == "n"):
                            break
                            break
                        print("You put wrong answer")
                        repeat = input("Do you want to enter a username again?[Y/N] : ")                    

            if validity:
                self.cur.execute("INSERT INTO Follows(username1,username2) VALUES(%s, %s)", (self.__u_name1, u_name2))
                validity = False
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")