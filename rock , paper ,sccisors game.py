import random


options =("rock", "paper", "scissors")
is_running = True
while is_running:
    player = None
    computer = random.choice(options)
    while player not in options:
         player = input ("Enter your choice  (rock, paper, scissors):  ")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print ("its a tie")
    elif player == "rock" and computer == "scissors":
        print ("you win")
    elif player == "paper" and computer == "rock":
        print ("you win")
    elif player == "scissors" and computer == "paper":
        print ("you win")
    else:
        print ("you lose")
    play_again = input ("Do you want to play again? (y/N): ").lower()
    if not play_again=="y":
        is_running=False

print ("thanks for playing")