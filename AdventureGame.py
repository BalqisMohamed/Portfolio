name = input("What is your name? ")
print("Welcome to this adventure,", name)

#beginning
answer = input("You have come to a dirt road. You can choose to go left or right. Which way do you go? ")
if answer.lower() == "left":
    answer = input("You have come to a river. Do you wish to swim across the river or walk around it? (type 'swim' to swim or 'walk' to walk) ")
    if answer.lower() == 'swim':
        print("You drowned. Game over.")
    elif answer.lower() == 'walk':
        answer = input("You have arrived at a party. Do you wish to stay or go back to the river? ")
        if answer.lower() == 'stay':
            print("You enjoyed yourself and had a good night. Game over.")
        else:
            print("You went back to the river and swam. You drowned. Game over.")
    else:
        print("Not a valid option. You lose.")
elif answer.lower() == 'right':
    answer = input("You have come across a jungle. Do you wish to go through it? (yes/no) ")
    if answer.lower() == 'yes':
        print("You have become lost in the forest.")
        answer = input("You are hungry. You see some berries. Do you eat the berries or not? (yes/no) ")
        if answer.lower() == 'yes':
            print("The berries were poisonous. You died. Game over.")
        elif answer.lower() == 'no':
            print("You died from starvation. Game over.")
        else:
            print("Not a valid option. You lose.")
        
else:
    print("Not a valid option. You lose.")





