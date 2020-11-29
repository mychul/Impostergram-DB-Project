from follows import follows
from searchPhotoMenu import search_photo
from userSearch import user_search
from follows import follows
import os 
from upload import upload
from top import top
from feed import feed

class user_menu:
    def __init__ (self,username):
        self.__username=username

    def start(self):
        print("Hello",(self.__username))
        while(True):
            choice = input("Main Menu: \n1. Search for a Photo \n2. Search for a user \n3. Follow a User \n4. Unfollow a User \n5. View your feed\n6. View Top Posts \n7. Upload a photo \n8. Logout\n")
            # For clearing the screen after user choice
            clear = lambda: os.system('clear')
            clear()
            del clear

            if choice == "1": # goes to photo submenu
                photo_menu = search_photo(self.__username)
                if not photo_menu.conn_closed:
                    photo_menu.menu()
                    if not photo_menu.conn_closed: # If the user exits 
                        photo_menu.close_connection()
                   # print("Back Here in Main Menu in choice #1") #debug 
                del photo_menu
            elif choice == "2": # fufills functions requirment 2
                user_search_menu = user_search(self.__username)
                if not user_search_menu.conn_closed:
                    user_search_menu.userSearch()
                    if not user_search_menu.conn_closed:
                        user_search_menu.close_connection()
                del user_search_menu
            elif choice == "3":# fufill function requirement 3
                follow=follows(self.__username)
                if not follow.conn_closed:
                    follow.addFollow()
                    if not follow.conn_closed:
                        follow.close_connection()
                del follow
            elif choice == "4":# fufill function requirement 3
                unfollow =follows(self.__username)
                if not unfollow.conn_closed:
                    unfollow.delFollow()
                    if not unfollow.conn_closed:
                        unfollow.close_connection()
                del unfollow
            elif choice == "5":# fufill function requirement 4
                fd = feed(self.__username)
                if not fd.conn_closed:
                    fd.display()
                    if not fd.conn_closed:
                        fd.close_connection()
                del fd

            elif choice == "6":# fufills function requirement 10
                tp = top(self.__username)
                if not tp.conn_closed:
                    tp.display()
                    if not tp.conn_closed:
                        tp.close_connection()
                del tp
            elif choice == "7":
                # fufills function requirement 1a
                up = upload(self.__username)
                if not up.conn_closed:
                    up.uploads()
                    if not up.conn_closed:
                        up.close_connection()
                del up
            elif choice == "8":
                return
        return



