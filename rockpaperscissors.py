import random
import sys
list = ['Rock', 'Paper', 'Scissors']
NoWinner = True
while (NoWinner):
    user_choice = input("Your Choice(Enter 0 to exit): ")
    user_choice = user_choice.capitalize()
    cpu_choice = random.choice(list)
    
    if user_choice == '0':
        print("Thank you playing the game.")
        sys.exit(0)
        
    elif user_choice == 'Rock' and cpu_choice == 'Paper':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("CPU Wins - Paper beats Rock")
        
    elif user_choice == 'Rock' and cpu_choice == 'Scissors':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("CPU Wins - Scissors beats Rock")
    
    elif user_choice == 'Paper' and cpu_choice == 'Scissors':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("You Win - Paper beats Scissors")
    
    elif cpu_choice == 'Rock' and user_choice == 'Paper':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("You Win - Paper beats Rock")
    
    elif cpu_choice == 'Rock' and user_choice == 'Scissors':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("You Win - Scissors beats Rock")
    
    elif cpu_choice == 'Paper' and user_choice == 'Scissors':
        print(f"You chose '{user_choice}' and the CPU chose '{cpu_choice}'")
        print("CPU Wins - Scissors beats Paper")
    
    elif cpu_choice == user_choice:
        print(f"Both of you chose '{user_choice}'")
        print(f"Tie\nTryAgain.")
    
    else:
        print("Wrong Output\nTry Again.")
