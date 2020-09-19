import random
cpu_number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")
guesses = 0
while(True):
    user_choice = int(input("Take a guess: "))
    guesses += 1
    if user_choice > cpu_number:
        print("Your guess is too high.")
    elif user_choice < cpu_number:
        print("Your guess is too low.")
    else:
        print(f"Good job! You guessed my number in {guesses} guesses!")
        break;