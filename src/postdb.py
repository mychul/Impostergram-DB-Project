import psycopg2

class post_db:
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
            


