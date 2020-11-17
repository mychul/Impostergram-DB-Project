import psycopg2
from postdb import post_db

class photo_likes:
    def __init__(self, username, photo_id):
        __photo_id = photo_id
        __username = username
        post = post_db()
        cur = post.conn.cursor()
   
    # Let user menu worry about the 'would you like to enter another comment'
    def likes(self):
        try:
            self.cur.execute("SELECT username FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))
            if self.cur.rowcount > 0:
                print("Error: You've already liked this photo.  (-_-) ")
            elif self.cur.rowcount <= 0:
                self.cur.execute("INSERT INTO PhotoLikes (username, photo_id) VALUES (%s, %s)", (self.__username, self.__photo_id))            
                print("Successfully liked the photo.")
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
            self.cur.execute("SELECT username FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))
            if self.cur.rowcount <= 0:
                print("Error: You have not liked this photo.  (-_-) ")
            elif self.cur.rowcount > 0:
                self.cur.execute("DELETE FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))            
                print("Successfully unliked the photo.")
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