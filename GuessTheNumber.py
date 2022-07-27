import random

repeat = 'Y'
cpuRandomNum = random.randint(1, 21)

while (repeat == 'Y' or repeat == 'y'):
    userNum = input("Enter Your number between 1 and 20: ")
    userNum = int(userNum)
    if (cpuRandomNum < userNum):
        print("Your number is too high. Try again!")
    elif (cpuRandomNum > userNum):
        print("Your number is too low. Try again!")
    else:
        print("You got the number, Congrats!")
    repeat = input("Do you wish to continue ('Y' or 'N'): ")
