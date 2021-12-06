import random
win = 0
while True:

    game_choices = ["rock", "paper", "scissors"]
    guess = input("\n\nrock\npaper\nscissors\nInput your choice: ").lower()
    comp_guesse = random.choice(game_choices)
    if guess == "rock":
        if comp_guesse == "rock":
            print("Tie")
        elif comp_guesse == "paper":
            print("You loss\ncomputer win")
            print("Computer choice was paper")
        elif comp_guesse == "scissors":
            print("You win!!!")
            win += 1
    elif guess == "scissors":
        if comp_guesse == "rock":
            print("loss")
            print("Computer choice was rock")
        elif comp_guesse == "paper":
            print("You win")
            win += 1
        elif comp_guesse == "scissors":
            print("You tie")
    elif guess == "paper":
        if comp_guesse == "rock":
            print("you win")
            win += 1
        elif comp_guesse == "paper":
            print("Tie")
        elif comp_guesse == "scissors":
            print("you loss!!!")
            print("Computer choice was scissors")
    elif guess == "exit":
        print("You win",win,"time(s)")
        break
    else:
        print("Invalid input")