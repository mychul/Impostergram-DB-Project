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
        self.conn_closed = False
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
            print("Unexpected error. Returning to Main Menu.")
            self.conn_closed = True
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Closing cursor in close function in search photo")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True
   
    
    def menu(self):
        try:
            loop = True
            while(loop):
                pid = "p1" #TODO: write a photo search function and then call it here after display menu and giving the user a choice and update the view count
                print("1 - Like the photo\n2 - Unlike the photo\n3 - Tag a user\n4 - Untag a user\n5 - View comments\n6 - Make a comment\n7 - Download the photo onto your local device\n")
                choice = input("What would you like to do with this photo? (-1 to cancel): ")
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
                    pass
                else:
                    print("Incorrect input.  Please choose -1 or 1 - 5.\n")
                    loop = True
                    continue
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
                print("Error: Closing cursor")
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
                    print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                if self.post is not None:
                    del self.post
                self.conn_closed = True
                # print("Closing database connection")
        return
