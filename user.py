import random

class User:
    def __init__(self, name, coins = None):
        self.name = name 
        self.coins = coins if coins is not None else random.randint(10,30)*100
    
    def __str__(self):
        return f"User: {self.name}, Coins: {self.coins}"
        
    def update_coins(self, amount):
        self.coins += amount
        return self.coins <= 0
    # When less than 0 coins, returns true which then deletes the User in main program

