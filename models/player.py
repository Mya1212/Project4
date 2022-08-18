from tinydb import TinyDB, Query, where

db = TinyDB('db.json')
db_player = db.table("players")


class PlayerModels:
    def __init__(self, first_name, last_name, birth_date, sex, rank, id=None) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.sex = sex
        self.rank = rank
        self.id = None

""""
    def full_name(self):
        # return self.id + " " + self.first_name + " " + self.last_name
        return f"{self.id} - {self.first_name} - {self.last_name}"
        """

    def __str__(self):
        return self.full_name

    def serialize(self):

        data_player = {}
        data_player['first_name'] = self.first_name
        data_player['last_name'] = self.last_name
        data_player['birth_date'] = self.birth_date
        data_player['sex'] = self.sex
        data_player['rank'] = self.rank

        return data_player

    def save(self) -> int:
        data = self.serialize()
        self.id = db_player.insert(data)
        print(self.full_name())

    def update_player(self, data: dict) -> int:
        # db_player.update({})
        pass
