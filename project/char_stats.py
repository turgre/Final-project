## Characthers + Stats

class wildWolf():
    def __init__(self):
        self.name = "Wolf"
        self.health = 10
        self.attack = 2

class bartender():
    def __init(self):
        self.name = "Merle"
        self.health = 30
        self.attack = 5
        

class player():
    def __init__(self):
        self.health = 50
        self.gold = 10
        self.weapon = ""
        self.defence = 0
        self.name = ""

##Checking different stats of player
stats = player()
s = {
    'health' : stats.health,
    'gold' : stats.gold,
    'weapon' : stats.weapon,
    'defence' : stats.defence
    }

sAnswer = input("what stats would you like to check?: ").lower()

if sAnswer == "health" or "gold" or "weapon" or "defence":
    print(s[sAnswer])
