import time
import end_game


"""This functions goes through all the text for the game. It hold the varables for the characthers and loops"""
def play():
    player_hp = 50
    player_weapon = 0
    player_defence = 0
    player_gold = 20
    #Code for loop https://stackoverflow.com/questions/32928143/how-to-continue-asking-user-for-input-until-it-is-considered-valid
    tent = None
    weapon = None
    shops = None
    items = None
    move_t = None
    drink = None
    
    print("\n A stiff chill sweeps through your tent, you awaken shivering and upset."
        "\n Rubbing the sleep from your eyes, you grab a journal adding a tally mark to a page already littered with those same faded marks.",
        "\n Today marks your 50th day since your separation from the group.")
    
    time.sleep(2)
    print()

    
    tent = input("Get out of your tent? Y/N: ").lower()

    """This makes sure that the user can enter in a right answer if typed in wrong"""
    while tent not in ("y","n"):
        if tent is not None:
            print("Try again")
        tent = input("Get out of your tent? Y/N: ").lower()
        
    if tent == "y":
        print("You feel demotivated and tired, wishing you slept a few more minutes. -5 hp")
        player_hp = player_hp - 5
        print(player_hp, " hp")
        
    if tent == "n":
        print("You linger in the tent for 30 more minutes. Gaining more sleep +10")
        player_hp = player_hp + 10
        print(player_hp, "hp")

    time.sleep(2)
        
    print("\n Gathering your strength, you shift slowly from the makeshift bed on the floor.",
        "\n A yawn spills out of your mouth as you pull on a thick winter fur coat and walk towards the opening to your tent.",
        "\n You move to let yourself out but find the entrance slightly open, that explains the wind in the tent.")

    print("\nYour boots crunch under the snow, you cast a quick glance of your surroundings."
          "\nYou remember placing your weapons by the fire last night but now you can’t seem to find it in the snow.")
    print()
    
    weapon = input("Look for them? Y/N: ").lower()

    while weapon not in ("y", "n"):
        if weapon is not None:
            print("Try again")
        weapon = input("Look for them? Y/N: ").lower()
        
    if tent == "y":
        print("\n Clawing through the snow, you find your [Silver Sword] and your [Bronze Sword]."
              "\n+10 defence, +10 Weapon")
        player_weapon =+ 10
        player_defence =+ 10
        
        
    if tent == "n":
        print("\n You shrug, knowing you’ll find them at some point."
              "\n Besides, you’re going into town anyways in search of better equipment."
              "\n Maybe you’ll find a better weapon, you walk back your tent taking extra money you stashed away."
              "\n +20 gold")
        player_gold =+ 20
        
    time.sleep(2)

    print("\n You gather your items and begin to walk towards town."
          "\n Even though you know how easier it would be to live in town, you still refuse"
          "\n A part of you can't just break your traditions.")
          
    print("\n Upon arriving into town, you take in the big crowds of people."
          "\n You duck your head already know the two stores you're headed towards."
          "\n The items shop and the tavern."
          "\n Where are you going?")
    print()
    
    shops = input("Shop or Tavern?: ").lower()

    while shops not in ("shop", "tavern"):
        if shops is not None:
            print("Try again")    
        shops = input("Shop or Tavern?: ").lower()
        
    if shops == "shop":
        
            print("\n You are greeted by a feeble old woman."
                  "\n She winks at you once and lists off the different products she has to offer")
            print()
            print("\n 1.Gold sword +30 attack -30 gold"
                  "\n 2. Gold shield +30 defence  -30 gold"
                  "\n 3. Upgrade sword +10 attack -5 gold"
                  "\n 4. Upgrade shield +10 defense -5 gold")
            print()
                  
            items = input("Pick the number of what you would like to buy?: ")
            
            print()
                  
            while items not in ("1", "2", "3", "4"):
                  if items is not None:
                      print("Try again")
                  items = input("Pick the number of what you would like to buy?: ")
                  print()

            if items == "1":
                 print("You have gain a Gold sword! +30 attack -30 gold")
                 player_weapon =+ 30
                 player_gold =-30
                 print("Weapon stat: ", player_weapon)
                 print("Remaining gold: ", player_gold)

            if items == "2":

                 print("You have gain a Gold shield! +30 attack -30 gold")
                 player_defence =+ 30
                 player_gold =-30
                 print("Weapon stat: ", player_weapon)
                 print("Remaining gold: ", player_gold)

            if items == "3":
                 print("You have upgraded you sword! +10 attack -5 gold")
                 player_defence =+ 10
                 player_gold =- 5
                 print("Weapon stat: ", player_weapon)
                 print("Remaining gold: ", player_gold)


            if items == "4":
                 
                 print("You have upgraded you shield! +10 attack -5 gold")
                 player_defence =+ 10
                 player_gold =- 5
                 print("Weapon stat: ", player_weapon)
                 print("Remaining gold: ", player_gold)

            move_t = input("To head to the tavern, type Tavern." ).lower()

            while move_t not in ("tavern"):
                  if move_t is not None:
                      print("Try again")
                  move_t = input("To head to the tavern, type Tavern. If you want to go back home, type home: " ).lower()
                  print()

    if shops or move_t == "tavern":
        
        print("\n You walk into a partly crowded tavern and head straight to the bar."
              "\n You wave over the bartender, who walked over with a long stride."
              "\n 'In an excited manner, the bartender asks you to test his new triva game")

        t =  input("Y or N? :" ).lower()
        
        while t not in ("y","n"):
            if t is not None:
                print("Try again")
                
            t = input("Y or N? :" ).lower()
                             
        if t == "y":
            print("\n The bartender smiles brightly."
                  "\n 'You want to play my game? Oh goodie' He exclaimed."
                  "\n It's a little triva about... colors!")
            import triva
            print("\n The barkeeper is excited that you played"
                  "\n He give you 5 gold just for playing the game")
            player_gold =+ 5

        move_h = input("After playing that game you become very tired and you want to go home. Type home to leave: " ).lower()
        print()

        if t == "n":
            end_game.end_game()

    if move_h == "home":
        end_game.end_game()
        
      

            
                


              



        


          

    

