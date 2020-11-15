import psycopg2

class tagged:
    def __init__(self, photo_id):
        __photo_id = photo_id
        conn=None
        try:
            #connect to the postgresql db
            conn = psycopg2.connect(
                host="localhost",
                database="impostergram_db",
                user="postgres",
                password="postgres"
            )            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            pass
   
    def tag(self):
        validity=False
        try:
            username = input('Please enter a username: ')
            cur=self.conn.cursor()
            cur.execute("SELECT username FROM Users WHERE username = %s", (username))
            if cur.rowcount > 0:
                validity = True
            if validity: 
                cur.execute("INSERT INTO Tagged(username,photo_id) VALUES(%s, %s)", (username, self.__photo_id))

        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
        finally:
             if cur is not None:
                cur.close()
                print("Closing cursor")
                if self.conn is not None:
                    self.conn.close()
                    # print("Closing database connection")
        return validity