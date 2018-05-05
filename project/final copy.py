##Text-based adventure

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

while sAnswer != s[0] or s[2]:
    print(s[sAnswer])

            
                                 
  












    



##
##
##
##adven = [("A stiff chill sweeps through your tent, you awaken shivering and upset.", 
##         "Rubbing the sleep from your eyes, you grab a journal adding a tally mark to a page already littered with those same faded marks.",
##         "Today marks your 50th day since your separation from the group.")
##
##         ("Gathering your strength, you shift slowly from the makeshift bed on the floor.",
##          "A yawn spills out of your mouth as you pull on a thick winter fur coat and walk towards the opening to your tent.",
##          "You move to let yourself out but find the entrance slightly open, that explains the wind in the tent.")]
##
##
##
##
##for x in adven[0]:
##    print(x)
##
##
##
##    
####adven_answers = [">Get out of your tent? Y/N"]
####
####        
####print("★Welcome to a text based adventure! What would you like to do?"
####      "1. Start"
####      "2. "
####      "3. Quit"
####      options = input(int(">>>"))
####
####if options == int(1):
####      ...##Start game
##
##      
##
##
##
##
##
##
##
