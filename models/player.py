from controlers.player import Player
from tinydb import TinyDB, Query, where

db = TinyDB('db.json')
db_player = db.table("table_players")

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

    def save_new_player(self, data:dict)->int:
        db_player.insert(self.__dict__)

    def update_player(self, data:dict)->int:
        #db_player.update
        pass


    