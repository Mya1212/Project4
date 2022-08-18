from sys import exit
from controlers.player import PlayerController
from views.player import PlayerViews
from tinydb import TinyDB


class ApplicationController:

    def __init__(self):
        self.player_controller = PlayerController()
        self.player_views = PlayerViews()

    def start(self):

        while True:
            self.player_views.display_player_menu()
            user_input = input("Entrez votre choix ")

            if user_input == "1":
                # self.tournament
                pass

            elif user_input == "2":
                self.player_controller.menu_player()

            elif user_input == "3":
                self.menu.display_message("Good bye")
                exit()

            else:
                self.menu.display_message("Invalid choice")
