from follows import follows
from searchPhotoMenu import search_photo
from userSearch import user_search
from follows import follows

class user_menu:
    def __init__ (self,username):
        self.__username=username

    def start(self):
        print("Hello",(self.__username))
        while(True):
            choice = input("Main Menu: \n1. Search for a Photo \n2. Search for a user \n3. Follow a User \n4. Unfollow a User \n5. View your feed\n6. View Top Posts \n7. Upload a photo \n8. Logout\n")
           
            if choice == "1": # goes to photo submenu
                photo_menu = search_photo(self.__username)
                photo_menu.menu()
                photo_menu.connection_close()
                del photo_menu
            elif choice == "2": # fufills functions requirment 2
                user_search_menu = user_search(self.__username)
                user_search_menu.menu()
                user_search_menu.connection_close()
                del user_search_menu
            elif choice == "3":# fufill function requirement 3
                follow=follows(self.__username)
                follow.addFollow()
                follow.connection_close()
                del follow
            elif choice == "4":# fufill function requirement 3
                unfollow =follows(self.__username)
                follow.delFollow()
                follow.connection_close()
                del unfollow
            elif choice == "5":# fufill function requirement 4
                print ("implement feed")
            elif choice == "6":
                print ("implement top")# fufills function requirement 10
            elif choice == "7":
                print ("implement upload")# fufills function requirement 1a
            elif choice == "8":
                return
        return



