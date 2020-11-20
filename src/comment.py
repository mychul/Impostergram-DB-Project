import psycopg2
from postdb import post_db
from datetime import datetime

class comment:
    def __init__(self, username, photo_id):
        self.__photo_id = photo_id
        self.__username = username
        self.post = post_db()
        self.cur = None
        self.conn_closed = False # First flag that userMenu will check before
        
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
   
    def commented(self):
        try:
            check = True
            while(check):
                comment = input("Please enter your comment: ")
                choice = input("Comfirm comment: <" + comment + "> (Y/N): ")
                if(choice == "Y" or choice == "y"):
                    check = False
                    self.cur.execute("SELECT MAX(comment_id) FROM Comments")
                    row = self.cur.fetchone()
                    comment_id = int(row[0]) + 1
                    now = datetime.now()
                    # dd/mm/YY H:M:S
                    #dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
                    self.cur.execute("INSERT INTO Comments (comment_id, comments, username, photo_id, dates) VALUES (%s, %s, %s, %s, %s)", [str(comment_id), comment, self.__username, self.__photo_id, now])
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