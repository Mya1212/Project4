from views.menu import MenuViews
from sys import exit
from tinydb import TinyDB

class ApplicationController:

    def __init__(self):
        self.menu = MenuViews()

    def start(self):

        while True:
           self.menu.display_main_menu()
           user_input=input()

           if user_input=="1":
                self.menu.display_tournament_menu()
            
           elif user_input=="2":
                self.menu.display_player_menu()

           elif user_input=="3":
                self.menu.display_message("Good by.")
                exit()
            
           else:
            self.menu.display_message("Invalid choice")
        