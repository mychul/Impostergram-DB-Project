#imports ...
import psycopg2
from postdb import post_db
from userMenu import user_menu
from updateCsv import update_csv
import os

def validation_login(u_name,u_pass):
        post= post_db() # create a postdb object of the class post_db
        cur = None
        validity=False
        try:
            #print ("Attempting create a cursor")
            cur = post.conn.cursor()
            #print ("Successfully made cursor")
            #print("Querying for login validation.")
            cur.execute("SELECT username, pass FROM Users WHERE username = %s AND pass =%s",(u_name,u_pass)) #query for the username and password for validation
            if cur.rowcount == 1: # if that combination was found than rowcount would be 1
                validity =True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        finally:
            if cur is not None:
                #print("Closing cursor")
                cur.close()
                
            if post.conn is not None:
                #print("Closing database connection")
                post.conn.close()
            del post #cleanup of the post object
        return validity

def signup():
    try:
        post= post_db() # create a postdb object of the class post_db
        cur = None
        cur = post.conn.cursor()
        while (True):
            username = input("Enter your desired username(-1 to cancel): ")
            cur.execute("SELECT username FROM Users WHERE username = %s",([username]))
            if cur.rowcount == 1:
                print("Sorry this username already exists. Please try again.")
                continue
            elif username == "-1":
                return
            else:
                password = input("Enter your desired password(-1 to cancel): ")
                if password == "-1":
                    return
                confirm_pass=input("Enter your desired password again to confirm: ")
                if password != confirm_pass:
                    print("Password do not match. Please try again")
                    continue
                email = input("Enter your desired email(-1 to cancel): ")
                confirm_email=input("Enter your desired email again to confirm: ")
                if email != confirm_email:
                    print("Emails do not match. Please try again")
                    continue
                cur.execute("INSERT INTO Users (username,email,pass,numFollows) VALUES (%s, %s, %s, %s)",(username,email,password,"0"))
                post.conn.commit()
                return
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
    finally:
        if cur is not None:
            #print("Closing cursor")
            cur.close()
            
        if post.conn is not None:
            #print("Closing database connection")
            post.conn.close()
        del post #cleanup of the post object

    

#starting point
print("Welcome to Impostergram")
loop=True
while loop:
    choice = input("Would you like to: \n1.Log in\n2.Sign up\n3.Exit\n") 
    if choice == "3":
        break
    elif choice == "1":
        username=input("Username: ")
        password=input("Password: ")
        valid_login=False
        valid_login=validation_login(username,password) #validate given login information
        if valid_login:
            clear = lambda: os.system('clear')
            clear()
            del clear
            print("Successful Login. Proceeding to main menu.")
            menu=user_menu(username)
            menu.start()
            del menu
        else:
            con=input("Invalid information entered. Would you like to try again?(Y/N): ")
            if con =="n" or con=="N" or con=="no" or con=="No":
                loop=False
    elif choice == "2":
        signup()
backup_choice=input("Save changes to dynamic backup? (Y/N): ")
if backup_choice == "Y" or backup_choice== "y":
    dump= update_csv()
    if not dump.conn_closed:
        dump.csv_export()
        if not dump.conn_closed:
            dump.close_connection()
print("GoodBye")


