import time
import sys
import random
import play_game


"""This function bring the player to a start screen and begins the game"""
def start_game():
    #Code for loop https://stackoverflow.com/questions/32928143/how-to-continue-asking-user-for-input-until-it-is-considered-valid
    start = None
    print("★★★★★★★★★★★★★★★★★★★★★★★★"
        "\n Welcome to a text based adventure!",
          "\n What would you like to do?",
          "\n > Start"
          "\n > Quit"
          "\n★★★★★★★★★★★★★★★★★★★★★★★★")
    
    start = input("Enter option here: ").lower()

    while start not in ("start", "quit"):
        if start is not None:
            print("\nInvaild reponse")
        start = input("Enter option here: ").lower()
            
    if start == "start":
        play_game.play()   
    elif start == "quit":
        sys.exit()
        
start_game()
