from views.menu import MenuViews
from sys import exit
from controlers.player import PlayerController
from tinydb import TinyDB

class ApplicationController:

    def __init__(self):
        self.menu = MenuViews()

    def start(self):

        while True:
           self.menu.display_main_menu()
           user_input=input()

           if user_input=="1":
                #self.tournament
                pass
            
           elif user_input=="2":
                self.player.menu_player()

           elif user_input=="3":
                self.menu.display_message("Good bye")
                exit()
            
           else:
            self.menu.display_message("Invalid choice")
        