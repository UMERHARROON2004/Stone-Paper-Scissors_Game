import random
choices = ["stone", "paper",  "scissors"]
user_choice = input("Choose One from stone, paper, or scissors:\n")
if user_choice not in choices:
    print("Invalid Input")
    exit()
winner = None
computer_choice = random.choice(choices)
if user_choice == computer_choice:
    print("It,s a TIE")
elif (user_choice == "stone" and computer_choice == "scissors") or\
     (user_choice == "paper" and computer_choice == "stone") or\
     (user_choice == "scissors" and computer_choice == "paper"):
      winner = "Congratulations! You are the WINNER"
else:
    winner = "computer"
    print("Sorry you lost the game Computer Win")
print("You Choose", user_choice)
print("Computer Choose", computer_choice)
print("Winner", winner)

print("-------GAME OVER-----")