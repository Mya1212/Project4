from controlers.player import Player

class Player:
    def __init__(self, first_name, last_name, birth_date, sex, rank) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name

    def serialize(self):

        data_player = {}
        data_player['first_name'] = self.first_name
        data_player['last_name'] = self.last_name
        data_player['birth_date'] = self.birth_date
        data_player['sex'] = self.sex
        data_player['rank'] = self.rank
        data_player['name'] = self.first_name + " "+ self.last_name

        return data_player

    def save(self):
        """ save the player to the database """
        print ("sauvegarde du player")


    def update_player(self):
        #a refaire pas input
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