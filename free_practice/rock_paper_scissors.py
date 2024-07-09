import random
options = ('rock', 'paper', 'scissors')
running = True
while running:
    user_input = None
    while user_input not in options:
        user_input = input("Give your choice(rock, paper, scissors):")
    computer_choice = random.choice(options)
    if user_input == computer_choice:
        print(f"Computer's choice was {computer_choice}. It's a tie.")
    elif user_input == 'rock' and computer_choice == 'scissors':
        print(f"Computer's choice was {computer_choice}. Hurray! You won over the computer.")
    elif user_input == 'paper' and computer_choice == 'rock':
        print(f"Computer's choice was {computer_choice}. Hurray! You won over the computer.")
    elif user_input == 'scissors' and computer_choice == 'paper':
        print(f"Computer's choice was {computer_choice}. Hurray! You won over the computer.")
    else:
        print(f"Computer's choice was {computer_choice}. Sorry! You lose.")
    
    ask = input("Do you want to play again?(Y/N):").capitalize()
    if not ask == 'Y':
        running = False
