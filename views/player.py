from controlers.player import Player

class PlayerViews:

    def create_player(self):

        first_name = input('Entrez votre nom :\n>')
        last_name = input('Entrez votre prénom :\n>')
        birthday = input ('Entrez votre date de naissance XX/XX/XXXX:\n>')
        sex = input ('Entrez votre genre F ou M:\n>')
        rank = input ('Entrez votre classement:\n>')

        data = {
            "first_name":first_name, "last_name":last_name, "birthday":birthday, "sex":sex, "rank":rank
        }
        return data

    def display_player_list(self):
        #afficher liste joueur
        pass

    def update_player(self):

        while True:
            self.menu.display_update_player()
            user_input=input()
            
            if user_input=="1":
                print("Edit player")
            
            elif user_input=="2":
                print("Create player")

            elif user_input=="3":
                print("return main menu")
            
            else:
                self.menu.display_message("Invalid choice")
       
    
    def menu_player(self):
        
        while True:
            self.menu.display_player_menu()
            user_input=input()

            if user_input=="1":
                print("Create player")
            
            elif user_input=="2":
                print("update player")

            elif user_input=="3":
                print("player list sort by name")

            elif user_input=="4":
                print("player list sort by rank")

            elif user_input=="5":
                print("return main menu")
            
            else:
                self.menu.display_message("Invalid choice")