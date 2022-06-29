print("Welcome to this game about Geography. \n"
      "I am going to ask 5 questions. \n"
      "One wrong guess and it is game over for you. \n"
      "Only the brave will dare.")

play = input("Do you want to play the game? ").capitalize()

if play == 'Yes':
    print("Okay, let's begin!!")
    answer = input("What is the capital of Somalia? ").capitalize()
    if answer == 'Mogadishu':
        print("Correct.")
        print("Now we are on to question 2. It is only going to get hard from here on out")

        answer = input("In which European country are the Apennine Mountains located? ").capitalize()
        if answer == 'Italy':
            print("Correct")
            print("You are doing very well so far, but it is going to get a lot harder now")
            print("Ready for question 3?")

            answer = input("What is the worlds deepest lake? ").title()
            if answer == 'Lake Baikal':
                print("Correct")
                print("Only 2 questions left, let's see if you have what it takes.")

                answer = input("Byblos is often noted as one of the world’s most ancient cities.\n"
                                      "Where would you find it? ").capitalize()
                if answer == 'Lebanon':
                    print("Correct")
                    print("This is the last question. I hope you do well.")

                    answer = input("What is the southernmost inhabited town in the world? ").title()
                    if answer == 'Puerto Williams':
                        print("CORRECT, YOU WIN THE GAME HOLY SHHHHH!!!!!!!!!!!!!!")
                        print("You did such a good job.")
                    else:
                        print("You were so close to winning, but the answer was Puerto Williams.")
                        quit()
                else:
                    print("So close to the end. The answer was Lebanon.")
                    quit()
            else:
                print("Incorrect. The answer was Lake Baikal. Better luck next time.")
                quit()
        else:
            print("Incorrect. The answer was Italy. Better luck next time.")
            quit()
    else:
        print("Incorrect. The answer was Mogadishu. Better luck next time.")
        quit()

else:
    print("We hope you can play with us another time.")
    quit()