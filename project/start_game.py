def start_game():
    print("★Welcome to a text based adventure!",
          "What would you like to do?",
          "\n > Start"
          "\n > Quit")
    
    start = input("Enter option here: ").lower()
    if start == "start":
        play_game()
    elif start == "quit":
        sys.exit()
    while start != "start" or "quit":
        print("Not vaild")
        start = input("Enter option here: ").lower()
        if start == "start":
            play_game()
        elif start == "quit":
            sys.exit()
start_game()
