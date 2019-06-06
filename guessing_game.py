import random
import os




class NumberGuessingGame():
    def __init__(self):
        self.player_name = input('What is your Name? ')
        print("Hello Welcome to the guessing game {}".format(str(self.player_name)))
     
    def randomnumbergame(self):
        player_number = int(input("what is your number? "))
        number = random.randint(1,99)
        player_guesses = 5
        guesses = 0
        while player_number != number and player_guesses > guesses :
            if player_number > number:
                print("try lower")
                player_guesses = player_guesses - 1
                print("Player guesses left {}".format(str(player_guesses)))
                player_number = int(input("what is your number? "))
            elif player_number < number:
                print("try higher")
                print("Player guesses left {}".format(str(player_guesses)))
                player_guesses = player_guesses - 1
                player_number = int(input("what is your number? "))
            else:
                print("You have done it well done :)")
        else:
            print("Good Job")
            






def main():
    NumberGuessingGame().randomnumbergame()





if __name__ == "__main__":
    main()

            

