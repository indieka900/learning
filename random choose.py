import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("gues the number"))
    if user == number:
        print("hurray")
        print("you guessed right it's " +str(number))
        break
if user != number:
    print("INCORRECT the number is "+str(number))