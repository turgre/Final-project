import time

"""This functions goes through all the text for the game."""
def play():
    player_hp = 50
    #Code for loop https://stackoverflow.com/questions/32928143/how-to-continue-asking-user-for-input-until-it-is-considered-valid
    tent = None
    
    print("\n A stiff chill sweeps through your tent, you awaken shivering and upset."
        "\n Rubbing the sleep from your eyes, you grab a journal adding a tally mark to a page already littered with those same faded marks.",
        "\n Today marks your 50th day since your separation from the group.")
    
    time.sleep(0)
    print()

    
    tent = input("Get out of your tent? Y/N: ").lower()

    while tent not in ("y", "n"):
        if tent is not None:
            print("Try again")
        tent = input("Get out of your tent? Y/N: ").lower()
        
    if tent == "y":
        print("You feel demotivated and tired, wishing you slept a few more minutes. -5 hp")
        player_hp = player_hp - 5
        print(player_hp)
        
    if tent == "n":
        print("You linger in the tent for 30 more minutes. Gaining more sleep +10")
        player_hp = player_hp + 10
        print(player_hp)

    
        
        


##
##    while tent != "y" or tent != "n":
##         print("Try again")
##         tent = input("Get out of your tent? Y/N: ").lower()
##    
##    if tent == "y":
##        print("You feel demotivated and tired, wishing you slept a few more minutes. -5 hp")
##        player_hp = player_hp - 5
##        print(player_hp)
##        
##    if tent == "n":
##        print("You linger in the tent for 30 more minutes. Gaining more sleep +10")
##        player_hp = player_hp + 10
##        print(player_hp)




            
##    else:
##        print("Try again")
##        tent = input("Get out of your tent? Y/N: ").lower()
    
##    print("\n Gathering your strength, you shift slowly from the makeshift bed on the floor.",
##        "\n A yawn spills out of your mouth as you pull on a thick winter fur coat and walk towards the opening to your tent.",
##        "\n You move to let yourself out but find the entrance slightly open, that explains the wind in the tent.")
