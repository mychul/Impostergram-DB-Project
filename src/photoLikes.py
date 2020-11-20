import psycopg2
from postdb import post_db

class photo_likes:
    def __init__(self, username, photo_id):
        self.__photo_id = photo_id
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
    
    def csv_export(self,tableName):
        s = ""
        s += "SELECT *"
        s += " FROM "
        s += tableName
        s += ""

        # Use the COPY function on the SQL we created above.
        SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(s)
        # Set up a variable to store our file path and name.
        t_path_n_file = "/home/team2/Documents/CS179g/Backup/" + tableName + ".csv"
        try:
            with open(t_path_n_file, 'w') as f_output:
                self.cur.copy_expert(SQL_for_file_output, f_output)
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)    

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
            self.cur.execute("SELECT username FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))
            if self.cur.rowcount > 0:
                print("Error: You've already liked this photo.  (-_-) ")
            elif self.cur.rowcount <= 0:
                self.cur.execute("INSERT INTO PhotoLikes (username, photo_id) VALUES (%s, %s)", (self.__username, self.__photo_id))            
                print("Successfully liked the photo.")
                self.post.conn.commit()
                self.csv_export("PhotoLikes")
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

    def unlikes(self):
        try:
            self.cur.execute("SELECT username FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))
            if self.cur.rowcount <= 0:
                print("Error: You have not liked this photo.  (-_-) ")
            elif self.cur.rowcount > 0:
                self.cur.execute("DELETE FROM PhotoLikes WHERE username = %s AND photo_id = %s", (self.__username, self.__photo_id))            
                print("Successfully unliked the photo.")
                self.post.conn.commit()
                self.csv_export("PhotoLikes")
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