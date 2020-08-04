import time
import random
def intro():
    print("You are on the way to your Home")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(2)
    print("You have two choices when reaching crossroads")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(2)
    print("One leads to your home and other to hell")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    time.sleep(2)
    print("Good Luck with your journey!!!!")

def choosepath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")
    return path
def checkpath(chosen_path):
    correct_path = random.randint(1,2)
    print("correct path is",correct_path)
    if (int(chosen_path)==correct_path):
        print("You are lucky. Welcome home!!!")
    else:
        print("What an unlucky day.")


play_again = "y"
while play_again == "y":
    intro()
    choice=choosepath()
    print("you chose path ",choice)
    checkpath(choice)
    play_again = input("Do you want to play again (Y/N): ").lower()
