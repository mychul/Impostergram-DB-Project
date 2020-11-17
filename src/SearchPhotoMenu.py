import psycopg2
from postdb import post_db
from photo_likes import photo_likes
from tagged import tagged
from view_comments import view_comments
from comment import comment

class searchPhoto:
    def __init__(self, username):
        __username = username
        post = post_db()
        cur = post.conn.cursor()
   
    
    def menu(self):
        try:
            loop = True
            while(loop):
                pid = "p1" #TODO: write a photo search function and then call it here after display menu and giving the user a choice 
                print("1 - Like the photo\n2 - Tag a user\n3 - View comments\n4 - Make a comment\n5 - Download the photo onto your local device\n")
                choice = input("What would you like to do this photo? (-1 to cancel): ")
                if(choice == -1):
                    loop = False
                    continue
                elif(choice == 1):
                    temp = photo_likes(self.__username, pid)
                    del temp
                elif(choice == 2):
                    temp = tagged(pid)
                    del temp
                elif(choice == 3):
                    temp = view_comments(pid, self.__username)
                    del temp
                elif(choice == 4):
                    temp = comment(self.__username, pid)
                    del temp
                elif(choice == 5):
                    pass
                else:
                    print("Incorrect input.  Please choose -1 or 1 - 5.\n")
                    loop = True
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
        return