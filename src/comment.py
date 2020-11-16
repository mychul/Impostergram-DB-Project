import psycopg2
from postdb import post_db

class comment:
    def __init__(self, username, photo_id):
        __photo_id = photo_id
        post = post_db()
        cur = post.conn.cursor()
   
    # Let user menu worry about the 'would you like to enter another comment
    def commented(self):
        validity=False
        try:
            check = True
            while(check):
                comment = input("Please enter your comment: ")
                choice = input("Comfirm comment: <" + comment + "> (Y/N): ")
                if(choice == "Y" or choice == "y"):
                    check = False
                    self.cur.execute("")
                    self.cur.execute("INSERT INTO Comments (username,photo_id) VALUES (%s, %s)", (username, self.__photo_id))
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
            lopp = False
                # print("Closing database connection")
        return