"""At the begginning of this project I was going to try using classes to keep track of STATS
I found it to be extremely challanging and diffucult for myself but I ended up using varable.
I keep this in the project folder to just show my progress"""


class wildWolf():
    def __init__(self):
        self.name = "Wolf"
        self.health = 10
        self.attack = 2

class bartender():
    def __init__(self):
        self.name = "Merle"
        self.health = 30
        self.attack = 5
        

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
