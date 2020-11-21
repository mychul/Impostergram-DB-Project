import psycopg2

class post_db:
    def __init__(self):
        self.conn = None
        try:
            #connect to the postgresql db
            #print ("Attempting to create connection.")
            self.conn = psycopg2.connect(
                host="localhost",
                database="impostergram_db",
                user="team2",
                password="179g"
            )
            #print ("Successfully made connection")
            

            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


