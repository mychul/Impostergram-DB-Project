import psycopg2

conn=None
cur =None
try:
    #connect to the postgresql db
    print ("Attempting to create connection.")
    conn = psycopg2.connect(
        host="localhost",
        database="impostergram_db",
        user="team2",
        password="179g"
    )
    print ("Successfully made connection")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Users")
    rows =cur.fetchall()
    for x in rows:
        print (x)    
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally: 
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


