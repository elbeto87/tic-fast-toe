from tinydb import TinyDB

db = TinyDB('game_history.json')


def add_game_to_history(timestamp, winner):
    db.insert({'timestamp': timestamp, 'winner': winner})


def get_game_history():
    return db.all()
