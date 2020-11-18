import psycopg2
from postdb import post_db

class comment:
    def __init__(self, username, photo_id):
        __photo_id = photo_id
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
   
    def commented(self):
        try:
            comment_id = 0
            check = True
            while(check):
                comment = input("Please enter your comment: ")
                choice = input("Comfirm comment: <" + comment + "> (Y/N): ")
                if(choice == "Y" or choice == "y"):
                    check = False
                    self.cur.execute("SELECT MAX(comment_id) FROM Comments")
                    comment_id = self.cur.fetchone()
                    comment_id = comment_id + 1
                    self.cur.execute("INSERT INTO Comments (comment_id, comments, username, photo_id) VALUES (%s, %s, %s, %s)", (comment_id, comment, self.__username, self.__photo_id))
                    self.post.conn.commit()
                    print("Successfully commented.")
                elif(choice == 'N' or choice == 'n'):
                    check = True
                    comment = ''
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