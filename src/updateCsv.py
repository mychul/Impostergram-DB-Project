import psycopg2
from postdb import post_db
class update_csv:
    def __init__(self):
        self.tablename = ["Comments", "Follows", "Likes", "PhotoLikes", "Photos", "Tagged", "Views", "Users"]
        self.post= post_db()
        self.cur=None
        self.conn_closed=False
        try:
           # print ("Attempting to make cursor")
            self.cur = self.post.conn.cursor()
            #print ("Successfully created cursor")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
            if self.cur is not None:
                self.cur.close()
             #   print("Closing cursor")
            if self.post.conn is not None:
                self.post.conn.close()
            del self.post
            #print("Unexpected error. Returning to Main Menu.")
            self.conn_closed = True
    
    def close_connection(self):
        if self.cur is not None:
            self.cur.close()
            #print("Closing cursor in close function in dump")
        if self.post.conn is not None:
            self.post.conn.close()     
        if self.post is not None:
            del self.post
        self.conn_closed = True

    def csv_export(self,):
        #print("Function csv_export has been called.  Executing update...")
        for x in self.tablename:    
            s = ""
            s += "SELECT *"
            s += " FROM "
            #print(x)
            s += x
            s += ""

            #print(s)

            # Use the COPY function on the SQL we created above.
            SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(s)
            # Set up a variable to store our file path and name.
            t_path_n_file = "/home/team2/Documents/CS179g/DynamicBackup/" + x + ".csv"
            try:
                with open(t_path_n_file, 'w') as f_output:
                    self.cur.copy_expert(SQL_for_file_output, f_output)
            except (Exception,psycopg2.DatabaseError) as error:
                print(error)
        #print("Updated data files in DynamicBackup folder successfully")
        return   