def newgame():
    year = int(input("Enter a year to check: "))
    if year % 4 == 0 and year % 2 == 0:
        print("Is a leapyear")
    else:
        print("Not a leap year")
newgame()
def play_again():
    response = input("Do you want to try again(YES/NO)")
    response =response.upper()
    if response == "YES":
        newgame()
    else:
        False
play_again()
