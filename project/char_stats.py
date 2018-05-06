"""At the begginning of this project I was going to try using classes to keep track of STATS
I found it to be extremely challanging and diffucult for myself but I ended up using varable.
I keep this in the project folder to just show my progress"""

"""Keeps the health, name, gold and attack of the player"""
class player():
    def __init__(self):
        self.name = ""
        self.health = 50
        self.gold = 10
        self.attack = 5

##Checking different stats of player
stats = player()
s = {
    'health' : stats.health,
    'gold' : stats.gold,
    'attack' : stats.attack,
    'name' : stats.name
    }

##sAnswer = input("what stats would you like to check?: ").lower()
##
##if sAnswer == "health" or "gold" or "attack" or "name":
##    print(s[sAnswer])
