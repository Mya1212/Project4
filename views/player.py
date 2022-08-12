from views.menu import MenuViews
import inquirer

class PlayerViews:

    def create_player(self):

        first_name = input('Entrez votre nom :\n>')
        last_name = input('Entrez votre prénom :\n>')
        birthday = input ('Entrez votre date de naissance XX/XX/XXXX:\n>')
        sex = input ('Entrez votre genre F ou M:\n>')
        rank = input ('Entrez votre classement:\n>')

        data_player = {
            "first_name":first_name, "last_name":last_name, "birthday":birthday, "sex":sex, "rank":rank
        }
        return data_player

    def display_player_list(self):
        #select sort by name or sort by rank
        print("\n\n=== Player list ===\n")
        #database display list player
        

    def update_player(self):
        #database import player list
        #select dans liste player
        """questions = [
        inquirer.List('player',
                message="Select a",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            ),
        ]
        answers = inquirer.prompt(questions)"""
        #affichage info player
        #select info à modifier
        #input user
        #update database
    pass
    
    def user_player_menu_choice(self):
        
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