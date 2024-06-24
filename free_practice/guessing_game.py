import random
target = random.randint(1, 100)
while True:
    userChoice = input("Enter a guess for number between 1 and 100 or quit(Q):")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Congratulations your guess is correct.")
        break
    elif(userChoice < target):
        print("Your guess is smaller than the correct number. Try greater number.")
    elif(userChoice > target):
        print("Your guess is greater than the correct number. Try smaller number.")
print("--Gameover--")