import psycopg2

class post_sever:
    def __init__(self):
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
            if self.conn is not None:
                self.conn.close()
                print("Closing database connection")
                
    def login(self,u_name,u_pass):
        validity=False
        try:
            cur=self.conn.cursor()
            cur.execute("SELECT %s,%s")
        except (Exception,psycopg2.DatabaseError) as error:
            print(error)
        finally:
             if cur is not None:
                cur.close()
                print("Closing cursor")
        return validity

