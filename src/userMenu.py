from follows import follows
from searchPhotoMenu import search_photo
from userSearch import user_search
from follows import follows

class user_menu:
    def __init__ (self,username):
        __username=username

    def start(self):
        print("Hello %s," ,(self.__username))
        while(True):
            choice = input("Main Menu: \n1. Search for a Photo \n2. Search for a user \n3. Follow a User \n4. Unfollow a User \n5. View your feed\n6. View Top Posts \n7. Upload a photo \n8. Logout")
            if choice == 1:
                photo_menu = search_photo()
                photo_menu.menu(self.__username)
                photo_menu.connection_close()
                del photo_menu
            elif choice == 2:
                user_search_menu = userSearch()
                user_search_menu.menu(self.__username)
                user_search_menu.connection_close()
                del user_search_menu
            elif choice == 3:
                follow=follows()
                follow.addFollow(self.__username)
                follow.connection_close()
                del follow
            elif choice == 4:
                unfollow =follows()
                follow.delFollow(self.__username)
                follow.connection_close()
                del unfollow
            elif choice == 5:
                print ("implement feed")
            elif choice == 6:
                print ("implement top")
            elif choice == 7:
                print ("implement upload")
            elif choice == 8:
                return
        return



