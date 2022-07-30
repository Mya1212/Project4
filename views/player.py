from controlers.player import Player

class PlayerViews:

    def create_player(self):

        first_name = input('Entrez votre nom :\n>')
        last_name = input('Entrez votre prénom :\n>')
        birthday = input ('Entrez votre date de naissance XX/XX/XXXX:\n>')
        sex = input ('Entrez votre genre F ou M:\n>')
        rank = input ('Entrez votre classement:\n>')

        data = {
            "first_name":first_name,

        }
        return data

    def display_player_list(self):
        #afficher liste joueur
        pass

    def update_player(self):
        #afficher liste des joueurs
        pass