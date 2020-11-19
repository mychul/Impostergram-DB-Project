import psycopg2
from postdb import post_db
from photoLikes import photo_likes
from tagged import tagged
from viewComments import view_comments
from comment import comment

class search_photo:
    def __init__(self, username):
        self.__username = username
        self.post = post_db()
        self.cur = None
        self.flag = True
        try:
            print ("Attempting to make cursor")
            self.cur = self.post.conn.cursor()
            print ("Successfully created cursor")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            print("Returning to Main Menu.")
            self.flag = False
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
   
    
    def menu(self):
        try:
            loop = True
            while(loop):
                pid = "p1" #TODO: write a photo search function and then call it here after display menu and giving the user a choice 
                print("1 - Like the photo\n2 - Unlike the photo\n3 - Tag a user\n4 - Untag a user\n5 - View comments\n6 - Make a comment\n7 - Download the photo onto your local device\n")
                choice = input("What would you like to do with this photo? (-1 to cancel): ")
                if(choice == "-1"):
                    loop = False
                    continue
                elif(choice == "1"):
                    photoL = photo_likes(self.__username, pid)
                    photoL.likes()
                    photoL.connection_close()
                    del photoL
                elif(choice == "2"):
                    photoU = photo_likes(self.__username, pid)
                    photoU.unlikes()
                    photoU.connection_close()
                    del photoU
                elif(choice == "3"):
                    tag = tagged(pid)
                    tag.tag()
                    tag.connection_close()
                    del tag
                elif(choice == "4"):
                    untag = tagged(pid)
                    untag.untag()
                    untag.connection_close()
                    del untag
                elif(choice == "5"):
                    viewC = view_comments(pid, self.__username)
                    viewC.view()
                    viewC.close_connection()
                    del viewC
                elif(choice == "6"):
                    newC = comment(self.__username, pid)
                    newC.commented()
                    newC.close_connection()
                    del newC
                elif(choice == "7"):
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
            if self.post is not None:
                del self.post
            return
        finally: 
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            if self.post is not None:
                del self.post
            # print("Closing database connection")
        return
