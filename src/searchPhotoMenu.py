import psycopg2
from postdb import post_db
from photo_likes import photo_likes
from tagged import tagged
from viewComments import view_comments
from comment import comment

class search_photo:
    def __init__(self, username):
        __username = username
        post = post_db()
        cur = post.conn.cursor()
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        del self.post
   
    
    def menu(self):
        try:
            loop = True
            while(loop):
                loop2 = True
                pid = "p1" #TODO: write a photo search function and then call it here after display menu and giving the user a choice 
                print("1 - Like the photo\n2 - Tag a user\n3 - View comments\n4 - Make a comment\n5 - Download the photo onto your local device\n")
                choice = input("What would you like to do this photo? (-1 to cancel): ")
                if(choice == -1):
                    loop = False
                    continue
                elif(choice == 1):
                    while(loop2):
                        choice2 = input("1 to Like\n2 to Unlike\n-1 to cancel\nChoose:")
                        if(choice2 == -1):
                            loop2 = False
                            continue
                        photoL = photo_likes(self.__username, pid)
                        if(choice2 == 1):
                            photoL.likes()
                        elif(choice2 == 2):
                            photoL.unlikes()
                        del photoL
                elif(choice == 2):
                    while(loop2):
                        choice2 = input("1 to Tag\n2 to Untag\n-1 to cancel\nChoose:")
                        if(choice2 == -1):
                            loop2 = False
                            continue
                        tag = tagged(self.__username, pid)
                        if(choice2 == 1):
                            tag.tag()
                        elif(choice2 == 2):
                            tag.untag()
                        del tag
                elif(choice == 3):
                    viewC = view_comments(pid, self.__username)
                    viewC.view()
                    del viewC
                elif(choice == 4):
                    newC = comment(self.__username, pid)
                    newC.commented()
                    del newC
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
