##Write a Rock Paper Scissors Lizard Spock game 

##randomly generate a throw for the computer 
##display win lose or draw

## imports
import random
## welcome statement and program description
print("Welcome to the Big Bang Rock Paper Scissors Lizard Spock game\n")
print("You will be asked to choose an item to throw.\n")
print("The computer will then randomly generate one of the choices against you.\n")
print("You will then be told who won.\n")
print("The rules:\n")
print("Scissors cuts Paper\n")
print("Paper covers Rock\n")
print("Rock crushes Lizard\n")
print("Lizard poisons Spock\n")
print("Spock smashes Scissors\n")
print("Scissors decapitates Lizard\n")
print("Lizard eats Paper\n")
print("Paper disproves Spock\n")
print("Spock vaporizes Rock\n")
print("And as it always has - Rock crushes Scissors\n")
print()
print("Spelling does matter. No choices are capitalized.\n")

## throw variable
throw = ["rock","paper","scissors","lizard","spock"]
## comparison test function
def throw_down (user_input, computer_choice):
    if computer_choice == ("scissors" or "lizard") and user_input == "rock":
        print("You won!\n")
    elif computer_choice == ("rock" or "spock") and user_input == "paper":
        print("You won!\n")
    elif computer_choice == ("paper" or "lizard") and user_input == "scissors":
        print("You won!\n")
    elif computer_choice == ("paper" or "spock") and user_input == "lizard":
        print("You won!\n")
    elif computer_choice == ("rock" or "scissors") and user_input == "spock":
        print("You won!\n")
    elif user_input == computer_choice:
        print("It's a tie!\n")
    else:
        print("You lost!\n")
## computer_throw function
def computer_throw(x):
    x = random.choice(throw)
    return x
## user_throw function
user_input = input("Choose an item to throw: ")
print()
if user_input in throw:
    user_input = user_input
    print("You chose: ",user_input,"\n")
else:
    print("You did not enter a valid choice\n")    
# computer chooses
computer_choice = computer_throw(throw)
print("The computer threw: ",computer_choice,"\n")
# The throw down!!
throw_down(user_input, computer_choice)


print("This is the end. This is the end my friend")
