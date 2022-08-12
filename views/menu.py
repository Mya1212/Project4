print(f"name dans le fichier menu {__name__}")

class MenuViews:

    def __init__(self):
        pass

#rajouter input joueur, boucle verif input correct, return choix
    def display_main_menu(self):
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Tournament menu")
        print("[2] Player menu")
        print("[3] Exit program")

    def display_tournament_menu(self):
        print("\n\n=== TOURNAMENT MENU ===\n")
        print("[1] Tournament list")
        print("[2] Create tournanment")
        print("[3] Return main menu")

    def display_player_menu(self):
        print("\n\n=== PLAYER MENU ===\n")
        print("[1] Create player")
        print("[2] Update player")
        print("[3] Display player list order by name")
        print("[4] Display player list order by rank")
        print("[5] Return main menu")

    def update_player(self):
        print("\n\n=== UPDATE PLAYER ===\n")
        print("[1] Edit player")
        print("[2] delete player")
        print("[3] Return player menu")


    def error_input(self):
        print("error")

    def display_message(self, message: str):
        """Print a message in the console"""
        print(f"\n{message}\n")

if __name__ == "__main__":
    print(__name__)
    
    menu = MenuViews()
    menu.display_main_menu()
