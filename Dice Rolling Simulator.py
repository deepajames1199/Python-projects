## Dice Rolling Simulator ###
import random
print("Welcome to the Rolling Dice Simulator")

user = input("Start rolling by pressing Y/N: ").lower()
while user == 'y':
    
    print("You got {}".format(random.randint(1, 7)))
    user = input("Roll again by pressing Y/N: ").lower()


print("Goodbye") if user == 'n' else print('Invalid input ')


    
