#syntax
#def new_game():
#    pass
#def check_answer():
#    pass
#def display_score():
#    pass
#def play_again():
#    pass

def new_game():
    geuses = []
    correct_guesses = 0
    question_number = 1
    for key in questions:
        print("----------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        geuses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_number += 1
    display_score(correct_guesses, guess)
def check_answer(answer, guess):
    if answer == guess:
        print("COREECT!!!!")
        return 1
    else:
        print("WRONG!!")
        return 0

def display_score(correct_guesses, geuses):
    print("-------------------------")
    print("RESULTS")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses ", end="")
    for i in geuses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is "+str(score)+"%")

def play_again():
    response = input("Do you want to try again(YES/NO)")
    response =response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {"Who created Python?: ": "A",
             "Which year did python created?: ": "B",
             "Python is tributed to which comedy group?: ": "C",
             "Which is language is this?: ": "A",
             "Guesse my name ": "D"
             }

options = [["A. Guido van Rossum", "B. Elon Musk","C. Bill gates","D. Mark"],
           ["A. 1989", "B. 1991","C. 2000","D. 2013"],
           ["A. Lonely Island", "B. Smoch", "C. Monty Python","D. SNL"],
           ["A. Python", "B. JavaScript", "C. Java", "D. HTML"],
           ["A. John","B. Jared","C. Hassan","D. Joseph"]]
new_game()
while play_again():
    new_game()
print("Thanks for trying")