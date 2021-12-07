import random
while True:
    choices = ["rock","stone","cement","sand"]
    computer = random.choice(choices)
    worker = None
    while worker not in choices:
        worker = input("Hey rock, stone, cement or sand?: ").lower()

    if worker == computer:
            print("computer choose",computer)
            print("you chosed: ",worker)
            print("You win!!!!")
            break
    else:
            print("computer choose: ",computer)
            print("you chosed: ",worker)
            print("You lost the game")
    play_again = input("Do you want to play again (yes/no) ").lower()
    if play_again != "yes":
        break
print('bye thanks for playing')