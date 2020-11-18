import psycopg2
from postdb import post_db

class comment_likes:
    def __init__(self, username, comment_id):
        __comment_id = comment_id
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
   
    # Let user menu worry about the 'would you like to enter another comment'
    def likes(self):
        try:
            self.cur.execute("SELECT username FROM Likes WHERE username = %s AND comment_id = %s", (self.__username, self.__comment_id))
            if self.cur.rowcount > 0:
                print("Error: You've already liked this comment.  (-_-) ")
            elif self.cur.rowcount <= 0:
                self.cur.execute("INSERT INTO Likes (username, comment_id) VALUES (%s, %s)", (self.__username, self.__comment_id))            
                print("Successfully liked the comment.")
                self.post.conn.commit()
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

    def unlikes(self):
        try:
            self.cur.execute("SELECT username FROM Likes WHERE username = %s AND comment_id = %s", (self.__username, self.__comment_id))
            if self.cur.rowcount <= 0:
                print("Error: You have not liked this comment. >.> ")
            elif self.cur.rowcount > 0:
                self.cur.execute("DELETE FROM Likes WHERE username = %s AND comment_id = %s", (self.__username, self.__comment_id))            
                print("Successfully unliked the comment.")
                self.post.conn.commit()
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