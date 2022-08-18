from views.player import PlayerViews
from models.player import PlayerModels


class PlayerController:

    def __init__(self) -> None:
        self.player_view = PlayerViews()
        self.player_models = PlayerModels()

    def menu_player(self):
        while True:
            self.player_view.display_player_menu()
            user_input = input("Entrez votre choix : ")

            if user_input == "1":
                self.create_player()

            elif user_input == "2":
                pass
                self.update_player()

            elif user_input == "3":
                self.display_player_name()

            elif user_input == "4":
                self.display_player_rank()

            elif user_input == "5":
                break

            else:
                self.display_message("Invalid choice")


    def display_player_name(self):
        self.views.diplay_player_list()
        #player_list_name = db_player.all
        #players_list_name.sort_list(player_list_name, sort_by = 'name')
        #return player_list_name

    def display_player_rank(self, sort_by: str):
        self.views.diplay_player_list()
        #player_list_rank = db_player.all
        #players_list_rank.sort_list(player_list_name, sort_by = 'rank')
        #return player_list_rank

    def create_player(self):
        data_player = self.player_view.create_player()
        player = Player(**data_player)
        #player = Player(first_name=data_player["first_name"])
        player.save()

    def update_player(self):
        """Update a player"""
        print("update player")
        input("Entrez")


if __name__ == "__main__":
    player = Player("pierre", "dupont", "12-12-1988", "M", "800")
    print(player)
    data = player.serialize()
    print(data)
