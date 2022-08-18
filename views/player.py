
class PlayerViews:

    def display_main_menu(self):
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Tournament menu")
        print("[2] Player menu")
        print("[3] Exit program")

    def display_player_menu(self):
        print("\n\n=== PLAYER MENU ===\n")
        print("[1] Create player")
        print("[2] Update player")
        print("[3] Display player list order by name")
        print("[4] Display player list order by rank")
        print("[5] Return main menu")

    def error_input(self):
        print("error")

    def display_message(self, message: str):
        """Print a message in the console, le créer dans un menu views"""
        print(f"\n{message}\n")

    def create_player(self):

        first_name = input('Entrez votre nom :\n>')
        last_name = input('Entrez votre prénom :\n>')
        birth = input('Entrez votre date de naissance XX/XX/XXXX:\n>')
        sex = input('Entrez votre genre F ou M:\n>')
        rank = input('Entrez votre classement:\n>')

        data_player = {
            "first_name": first_name, "last_name": last_name, "birth_date": birth, "sex": sex, "rank": rank
        }
        return data_player

    def display_player_list(self):
        print("\n\n=== Player list ===\n")
            #for player in Player_list :
                #print

        # database display list player

    def update_player(self):
        # database import player list
        # select dans liste player
        # affichage info player
        # select info à modifier
        # input user
        # update database
        pass

    def user_player_menu_choice(self):

        while True:
            self.menu.display_player_menu()
            user_input = input()

            if user_input == "1":
                print("Create player")

            elif user_input == "2":
                print("update player")

            elif user_input == "3":
                print("player list sort by name")

            elif user_input == "4":
                print("player list sort by rank")

            elif user_input == "5":
                print("return main menu")

            else:
                self.menu.display_message("Invalid choice")
