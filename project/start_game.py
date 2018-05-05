import time
import sys
import random
import play_game

def start_game():
    print("★★★★★★★★★★★★★★★★★★★★★★★★"
        "\n Welcome to a text based adventure!",
          "\n What would you like to do?",
          "\n > Start"
          "\n > Quit"
          "\n★★★★★★★★★★★★★★★★★★★★★★★★")
    
    start = input("Enter option here: ").lower()
    if start == "start":
        play_game.play()   
    elif start == "quit":
        sys.exit()
    while start != "start" or "quit":
        print("Not vaild")
        start = input("Enter option here: ").lower()
        if start == "start":
             play_game.play()  
        elif start == "quit":
            sys.exit()
start_game()
