#imports ...
import psycopg2
from postdb import post_db
from userMenu import user_menu
from updateCsv import update_csv

def validation_login(u_name,u_pass):
        post= post_db() # create a postdb object of the class post_db
        cur = None
        validity=False
        try:
            print ("Attempting create a cursor")
            cur = post.conn.cursor()
            print ("Successfully made cursor")
            print("Querying for login validation.")
            cur.execute("SELECT username, pass FROM Users WHERE username = %s AND pass =%s",(u_name,u_pass)) #query for the username and password for validation
            if cur.rowcount == 1: # if that combination was found than rowcount would be 1
                validity =True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        finally:
            if cur is not None:
                print("Closing cursor")
                cur.close()
                
            if post.conn is not None:
                print("Closing database connection")
                post.conn.close()
            del post #cleanup of the post object
        return validity

#starting point
print("Welcome to Impostergram\nPlease log in.")
loop=True
while loop:
    choice = input("Would you like to log in(1) or exit(2): ") 
    if choice == "2":
        break
    username=input("Username: ")
    password=input("Password: ")
    valid_login=False
    valid_login=validation_login(username,password) #validate given login information
    if valid_login:
        print("Successful Login. Proceeding to main menu.")
        menu=user_menu(username)
        menu.start()
        del menu
    else:
        print("Invalid information entered. Would you like to try again?")
        con=input("(Y/N):")
        if con =="n" or con=="N" or con=="no" or con=="No":
            loop=False
backup_choice=input("Save changes to dynamic backup?: (Y/N)")
if backup_choice == "Y" or backup_choice== "y":
    dump= update_csv()
    dump.csv_export()
print("GoodBye")


