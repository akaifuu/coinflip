import json 
from user import User 

def save_users(users, filename="users.json"):
    with open(filename, 'w') as file:
        json.dump({name: user.coins for name, user in users.items()}, file)

def load_users(filename="users.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return{name: User(name,coins) for name, coins in data.items()}
    except FileNotFoundError:
        return{}