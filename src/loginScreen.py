#imports ...
import psycopg2
from postdb import post_db
from userMenu import user_menu

def validation_login(u_name,u_pass):
        post= post_db() # create a postdb object of the class post_db
        ourCursor = [post]
        validity=False
        try:
            
            print("Querying for login validation.")
            ourCursor[1].execute("SELECT username, pass FROM Users WHERE username = %s, pass =%s",(u_name,u_pass)) #query for the username and password for validation
            if ourCursor[1].rowcount == 1: # if that combination was found than rowcount would be 1
                validity =True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
        finally:
            if ourCursor[1] is not None:
                print("Closing cursor")
                ourCursor[1].close()
                
            if ourCursor[0] is not None:
                print("Closing database connection")
                ourCursor[0].close()
            del ourCursor
            del post #cleanup of the post object
        return validity

#starting point
print("Welcome to Impostergram\nPlease log in.")
loop=True
while loop:
    choice = input("Would you like to log in(1) or exit(2): ") 
    if choice == "2":
        break
    username=input("Username:")
    password=input("Password:")
    valid_login=False
    valid_login=validation_login(username,password) #validate given login information
    if valid_login:
        print("Successful Login. Proceeding to main menu.")
        menu=user_menu(username)
        menu.start()
    else:
        print("Invalid information entered. Would you like to try again?")
        con=input("(Y/N):")
        if con =="n" or con=="N" or con=="no" or con=="No":
            loop=False
print("GoodBye")


