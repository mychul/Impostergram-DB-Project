import psycopg2
from postdb import post_db

class tagged:
    def __init__(self, photo_id):
        __photo_id = photo_id
        post = post_db()
        cur = post.conn.cursor()
   
    def tag(self):
        validity=False
        loop = True
        while(loop):
            try:
                username = input("Please enter a username: ")
                self.cur.execute("SELECT username FROM Users WHERE username = %s", (username))
                if self.cur.rowcount > 0:
                    validity = True
                else: 
                    choice = input('User not found.\nWould you like to try again? (Y/N): ')
                    if (choice == "N" or choice == "n"):
                        loop = False
                        if self.cur is not None:
                            self.cur.close()
                            print("Closing cursor")
                        if self.post.conn is not None:
                            self.post.conn.close()     
                        del self.post              
                if validity: 
                    self.cur.execute("INSERT INTO Tagged (username,photo_id) VALUES (%s, %s)", (username, self.__photo_id))
                    self.post.conn.commit()
                    print("Successfully tagged " + username)
                    if self.cur is not None:
                        self.cur.close()
                        print("Closing cursor")
                    if self.post.conn is not None:
                        self.post.conn.close()
                        # print("Closing database connection")
                    del self.post
                    return
            except (Exception,psycopg2.DatabaseError) as error:
                print(error)
                if self.cur is not None:
                    self.cur.close()
                    print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                del self.post
                return
                    # print("Closing database connection")
        return