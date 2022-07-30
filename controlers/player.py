from views.player import PlayerViews
from views.menu import MenuViews
from models.player import Player

class PlayerController:

    def __init__(self) -> None:
        self.player_view = PlayerViews

    def update_player(self):
        while True:
            self.menu.display_player_menu()
            user_input=input()

            if user_input=="1":
                #player list
                #select player
                #edit
                pass
            
            elif user_input=="2":
                #player list
                #select player
                #delete
                pass

            elif user_input=="3":
                self.menu.display_player_menu()
            
            else:
                self.menu.display_message("Invalid choice")

    def display_player_name(self):
        #players = []
        #players.sort(key=)
        self.views.diplay_player_list()

    def display_player_rank(self, sort_by: str):
        self.views.diplay_player_list()

    def create_player(self):
        data_player = self.player_view.create_player()
        player = Player(**data_player)
        #player = Player(first_name=data_player["first_name"])
        player.save()
        
    def menu_player(self):
        while True:
            self.menu.display_player_menu()
            user_input=input()

            if user_input=="1":
                self.create_player()
            
            elif user_input=="2":
                self.update_player()

            elif user_input=="3":
                self.display_player_name()

            elif user_input=="4":
                self.display_player_rank()

            elif user_input=="5":
                self.menu.display_player_menu()
                exit()
            
            else:
                self.menu.display_message("Invalid choice")

if __name__ == "__main__":
    player = Player("pierre","dupont","12-12-1988","M","800")
    print(player)
    data = player.serialize()
    print(data)