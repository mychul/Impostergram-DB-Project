#imports ...
from postdb import postdb


print("Welcome to Impostergram\nPlease log in.")
loop=True
while loop:
    username=input("Username:")
    password=input("Password:")
    valid_login=False
    #query to see if valid combination of password and username
    #valid_login bool will change depending on query
    if valid_login:
        print("Successful Login Proceeding. Proceeding to menu.")
        #go to user menu class
        #pass along user token i.e. Username/Password
        #as they should only be allowed to do tasks related to their account
        #valid_login = post.login(username,password)
    else:
        print("Invalid information entered. Would you like to try again?")
        con=input("(Y/N):")
        if con =="n" or con=="N" or con=="no" or con=="No":
            loop=False
print("GoodBye")


