#Point counter
points = int(0)

#Putting answers and questions into a list
##Questions
questions = ["1. What are the primary colors?", "2. What are the secondary colors?",
             "3. Which two colors make green?", "4. Which two make purple?",
             "5. About how many colors can the human eye see?",
             "6. What are the color-sensitive cells in the eyes called?",
             "7. Which country is said to have one of the most colorful flags?",
             "Bonus +3 points: 8. What is the rainbow flag color order?"  ]


##answers
answers_q1 = ["A. Red, blue and yellow", "B. Black, white and gary",
               "C. Purple and green", "D. Orange and Yellow"]
answers_q2 = ["A. Black and white", "B. Red, blue and yellow",
              "C. Orange, Purple and Green", "D. Purple and green"]
answers_q3 = ["A. Red and Blue", "B. Black and yellow",
              "C. Red and orange", "D. Yellow and Blue"]
answers_q4 = ["A. Blue and Red", "B. Orange and Purple",
              "C. Blue and Green", "D. Yellow and Green"]
answers_q5 = ["A. 10", "B. 1,000", "C. 7,000,000", "D. 2"]
answers_q6 = ["A. Rods", "B. Cones", "C. Iris","D. Pupil"]
answers_q7 = ["A. Zimbabwe", "B. China", "C. Germeny", "D. Seychelles"]
answers_q8 = ["A. Orange, purple, green, yellow, blue and indigo",
              "B. Red, orange, yellow, green, blue, indigo, violet",
              "C. Yellow, green, blue, orange, black and purple",
              "D. White, blue, green, red, yellow, blue and purple"]

#List of answers
a_list = [answers_q1, answers_q2, answers_q3, answers_q4,
          answers_q5, answers_q6, answers_q7, answers_q8]

#List of correct answers
correct_answers = ["a","c","d","a","c","b","a","a"]

#Introducting the Game           
print("\nWelcome to the colors triva game!")
print("Thanks for playing!")

#Asking name
print()
name = input("What's you're name?: ")
print("Thanks" , name ,". Lets get started!\n" )


#Calling question
print(questions[0])
print()

###Question 1

#Calling Answers and orginizing them     
for x in a_list[0]:
    print(x)
print()

#Telling if question is right or wrong + points
q1= input("Answer: ").lower()

while q1 != correct_answers[0]:
    print("Sorry! ", name, "! Try again!")
    points -= 1
    print("Points: " , points)
    q1= input("Answer: ").lower()
else:
    if q1 == correct_answers[0]:
        points += 1
        print("\nCorrect! " +"Next question")
        print("Points: " , points)
  

####Questions 2
print()
print(questions[1])
print()

#Calling Answers and orginizing them
for x in a_list[1]:
    print(x)
print()

#Telling if question is right or wrong + points
q2= input("Answer: ").lower()

while q2 != correct_answers[1]:
    print("Oh no!")
    points -= 1
    print("Points: " , points)
    q2= input("Answer: ").lower()
else:
    if q2 == correct_answers[1]:
        points += 1
        print("Nice ", name ," Next one")
        print("Points: " , points)

###Questions 3
        
#Calling question
print()
print(questions[2])
print()

#Calling answers and orginizing them
for x in a_list[2]:
    print(x)
print()

#Telling if question is right or wrong + points
q3= input("Answer: ").lower()

while q3 != correct_answers[2]:
    print("Oh no", name, ". Its okay try again.")
    points -= 1
    print("Points: " , points)
    q3= input("Answer: ").lower()
else:
    if q3 == correct_answers[2]:
        points += 1
        print("Nice! " + "Next one")
        print("Points: " , points)

###Questions 4

#Calling Question
print()
print(questions[3])
print()

#Calling Answers and orginizing them
for x in a_list[3]:
    print(x)
print()

#Telling if question is right or wrong + points
q4= input("Answer: ").lower()

while q4 != correct_answers[3]:
    print("Oh no!")
    points -= 1
    print("Points: " , points)
    q4= input("Answer: ").lower()
else:
    if q4 == correct_answers[3]:
        points += 1
        print(name, " you got it!")
        print("Points: " , points)


        
###Questions 5

#Calling questions
print()
print(questions[4])
print()

#Calling answers and orginizing them
for x in a_list[4]:
    print(x)
print()

#Telling if question is right or wrong + points

q5= input("Answer: ").lower()
              
while q5 != correct_answers[4]:
    print("Awww :( ")
    points -= 1
    print("Points: " , points)
    q5 = input("Answer: ").lower()
else:
    if q5 == correct_answers[4]:
        points += 1
        print("Nice! " + "Next one")
        print("Points: " , points)

              


###Questions 6

#Calling question
print()
print(questions[5])
print()

#Calling answers and orginizing them
for x in a_list[5]:
    print(x)
print()

#Telling if question is right or wrong + points
q6= input("Answer: ").lower()

while q6 != correct_answers[5]:
    print("Oh no ", name)
    points -= 1
    print("Points: " , points)
    q6 = input("Answer: ").lower()
else:
    if q6 == correct_answers[5]:
        points += 1
        print("Great!")
        print("Points: " , points)
    



###Questions 7

#Calling questions
print()
print(questions[6])
print()

#Calling answers and orginizing them
for x in a_list[6]:
    print(x)
print()

#Telling if question is right or wrong + points
q7= input("Answer: ").lower()

while q7 != correct_answers[6]:
    print("Yikes!")
    points -= 1
    print("Points: " , points)
    q7 = input("Answer: ").lower()
else:
    if q7 == correct_answers[6]:
        points += 1
        print("Cool ", name, "!" )
        print("Points: " , points)
    


    

###Questions 8

#Calling Questions
print()
print(questions[7])
print()

#Calling Answers and orginizing them
for x in a_list[7]:
    print(x)
print()

#Telling if question is right or wrong + points
q8= input("Answer: ").lower()

while q7 != correct_answers[7]:
    print("It's okay! No points are removed for this one")
    points -= 1
    print("Points: " , points)
    q7 = input("Answer: ").lower()
else:
    if q7 == correct_answers[7]:
        points += 1
        print("Whoa", name, "Nice!")
        print("Points: " , points)
    



##End game
print()
print("You finished the game with: ")
print(points, "points")

player_gold =+ int(points)
              
    


