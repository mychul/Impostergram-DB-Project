from commentLikes import comment_likes
import psycopg2
from postdb import post_db

class view_comments:
    def __init__(self, photo_id, username):
        __photo_id = photo_id
        __username = username
        post = post_db()
        cur = post.conn.cursor()
   
    # Let user menu worry about the 'would you like to enter another comment'
    def view(self):
        try:
            self.cur.execute("SELECT comment_id, comments, username, dates FROM Comments WHERE photo_id = %s", (self.__photo_id))
            all_comments = self.cur.fetchall()
            comment_id = []
            for row in all_comments:
                print("comment_id = " + str(row[0]) + ", ")
                print("comment = " + str(row[1]) + ", ")
                print("username = " + str(row[2]) + ", ")
                print("date = " + str(row[3]) + "\n")
                comment_id.append(row[0])
            choice = input("Would you like to \"Like\/Unlike\" a comment? (Y/N): ")
            if(choice == "Y" or choice == "y"):
                loop = True
                while(loop):
                    comment_choice = input("Please enter the comment's id (-1 to Cancel): ")
                    if(comment_choice == -1):
                        loop = False
                        continue
                    valid = False 
                    for temp in comment_id:
                        if(comment_choice == comment_id):
                            valid = True
                            break
                    if(valid):
                        choice2 = input("Enter 1 to Like, 0 to UnLike (-1 to Cancel): ")
                        if(choice2 == -1):
                            loop = False
                            continue
                        if(choice2 == 1):
                            # create a Comment_Like object passing in comment_choice and username into the appropoate function
                            temp = comment_likes(self.__username, comment_choice)
                            temp.likes()
                            del temp # delete the object
                        elif(choice2 == 0):
                            # create a Comment_Like object passing in comment_choice and username into the appropoate function
                            temp = comment_likes(self.__username, comment_choice)
                            temp.unlikes()
                            del temp # delete the object
                    else:
                        print("Comment_id that you entered does not exist.")
                        valid = False
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