import psycopg2
from postdb import post_db

class tagged:
    def __init__(self, photo_id):
        self.__photo_id = photo_id
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
   
    def tag(self):
        validity=False
        loop = True
        while(loop):#loop for invalid input
            try:
                username = input("Please enter a username: ")
                self.cur.execute("SELECT username FROM Users WHERE username = %s", [username])
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
                        self.conn_closed = True           
                if validity: 
                    self.cur.execute("SELECT username FROM Tagged WHERE username = %s AND photo_id = %s", (username, self.__photo_id))
                    if(self.cur.rowcount > 0):
                        print("This user is already tagged.")
                        loop = False
                        continue
                    else:
                        self.cur.execute("INSERT INTO Tagged (username,photo_id) VALUES (%s, %s)", (username, self.__photo_id))
                        self.post.conn.commit()
                        self.csv_export("Tagged")
                        print("Successfully tagged " + username)
                        if self.cur is not None:
                            self.cur.close()
                            print("Closing cursor")
                        if self.post.conn is not None:
                            self.post.conn.close()
                            # print("Closing database connection")
                        del self.post
                        self.conn_closed = True
                        return
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
                    # print("Closing database connection")
        return

    def untag(self):
        validity=False
        loop = True
        while(loop):#loop for invalid input
            try:
                username = input("Please enter a username: ")
                self.cur.execute("SELECT username FROM Users WHERE username = %s", [username])
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
                        self.conn_closed = True          
                if validity: 
                    if validity: 
                        self.cur.execute("SELECT username FROM Tagged WHERE username = %s AND photo_id = %s", (username, self.__photo_id))
                        if(self.cur.rowcount <= 0):
                            print("This user is already not tagged.")
                            loop = False
                            continue
                        else:
                            self.cur.execute("DELETE FROM Tagged (username,photo_id) VALUES (%s, %s)", (username, self.__photo_id))
                            self.post.conn.commit()
                            self.csv_export("Tagged")
                            print("Successfully untagged " + username)
                            if self.cur is not None:
                                self.cur.close()
                                print("Closing cursor")
                            if self.post.conn is not None:
                                self.post.conn.close()
                                # print("Closing database connection")
                            del self.post
                            self.conn_closed = True
                            return
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
                    # print("Closing database connection")
        return