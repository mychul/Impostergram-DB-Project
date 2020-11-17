from follows import follows
from SearchPhotoMenu import searchPhoto
from userSearch import userSearch
from follows import follows

class userMenu:
    def __init__ (self,username):
        __username=username

    def start(self):
        print("Hello %s," ,(self.__username))
        while(True):
            choice = input("Main Menu: \n 1. Search for a Photo \n 2. Search for a user \n 3. Follow a User \n 4. Unfollow a User \n 5. View your feed\n 6. View Top Posts \n 7. Upload a photo \n 8. Logout")
            if choice == 1:
                photomenu = searchPhoto()
                photomenu.menu(self.__username)
                del photomenu
            elif choice == 2:
                user_search_menu = userSearch()
                user_search_menu.menu(self.__username)
                del user_search_menu
            elif choice == 3:
                follow=follows()
                follow.addFollow(self.__username)
                del follow
            elif choice == 4:
                unfollow =follows()
                follow.delFollow(self.__username)
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



