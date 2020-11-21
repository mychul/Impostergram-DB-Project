import psycopg2
from postdb import post_db

class follows:
    def __init__(self,username):
        self.__u_name1 = username
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
        t_path_n_file = "/home/team2/Documents/CS179g/DynamicBackup/" + tableName + ".csv"
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
            
    def addFollow(self):
        validity = False
        validity_user = False
        try:
            while(not validity):
                u_name2 = input("Please enter a username to Follow : ")
                if u_name2 == self.__u_name1:
                        print("You put yourself! Try it again")
                        continue

                self.cur.execute("SELECT username FROM Users WHERE username = %s",[u_name2])
                if self.cur.rowcount > 0:
                    validity_user = True
                else:
                    print("That username does not exist!")
                    repeat = input("Do you want to enter a username again?[Y/N] : ")
                    while(not repeat == "Y" and not repeat == "y"):
                        if(repeat == "N" or repeat == "n"):
                            validity = True
                            break   #for break line 36
                        print("You put wrong answer")
                        repeat = input("Do you want to enter a username again?[Y/N] : ")                    
                if validity_user:
                    self.cur.execute("SELECT * FROM Follows WHERE username1 = %s, username2 = %s", (self.__u_name1, u_name2))
                    if self.cur.rowcount > 0:
                        print("You already followed %s", u_name2)
                    else:
                        self.cur.execute("INSERT INTO Follows(username1,username2) VALUES(%s, %s)", (self.__u_name1, u_name2))
                        self.cur.commit()
                        print("Success!")
                        self.csv_export("Follows")
                    valitidy = True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")
            self.conn_closed = True

    def delFollow(self):
        validity = False
        validity_user = False
        try:
            while(not validity):
                u_name2 = input("Please enter a username to Unfollow : ")
                if u_name2 == self.__u_name1:
                        print("You put yourself! Try it again")
                        continue
                self.cur.execute("SELECT * FROM Follows WHERE username1 = %s, username2 = %s",(self.__u_name1, u_name2))
                if self.cur.rowcount > 0:
                    validity_user = True
                else:
                    print("That follow does not exist!")
                    repeat = input("Do you want to enter a username again?[Y/N] : ")
                    while(not repeat == "Y" and not repeat == "y"):
                        if(repeat == "N" or repeat == "n"):
                            validity = True
                            break
                        print("You put wrong answer")
                        repeat = input("Do you want to enter a username again?[Y/N] : ")                    
                if validity_user:
                    self.cur.execute("DELETE * FROM Follows WHERE username1 = %s, username2 = %s", (self.__u_name1, u_name2))
                    if self.cur.rowcount <= 0:
                        print("You already unfollowed %s", u_name2)
                    else:
                        self.cur.commit()
                        print("Success!")
                        self.csv_export("Follows")
                    valitidy = True
                    
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.cur is not None:
                self.cur.close()
                print("Closing cursor")
                if self.post.conn is not None:
                    self.post.conn.close()
                    print("Closing database connection")
            self.conn_closed = True