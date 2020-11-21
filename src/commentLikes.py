import psycopg2
from postdb import post_db

class comment_likes:
    def __init__(self, username, comment_id):
        self.__comment_id = comment_id
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
            print("Returning to Main Menu.")
            self.conn_closed = True 

    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            print("Closing cursor")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True
   
    def likes(self):
        try:
            self.cur.execute("SELECT username FROM Likes WHERE username = %s AND comment_id = %s", (self.__username, self.__comment_id))
            if self.cur.rowcount > 0:
                print("Error: You've already liked this comment.  (-_-) ")
            elif self.cur.rowcount <= 0:
                self.cur.execute("INSERT INTO Likes (username, comment_id) VALUES (%s, %s)", (self.__username, self.__comment_id))            
                print("Successfully liked the comment.")
                self.post.conn.commit()
                #self.csv_export("Likes")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            self.conn_closed = True
            return
        finally: 
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            # print("Closing database connection")
            self.conn_closed = True
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
            """  self.csv_export("Likes") """
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