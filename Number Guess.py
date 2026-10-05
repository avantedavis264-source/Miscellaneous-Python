import random
from colorama import init, Fore, Style
from pandas.io.common import file_path_to_url

init(autoreset=True)

score = 0
SCORE_FILE = "Highscore.txt"

file_path = file_path_to_url(SCORE_FILE)

print(Fore.RED + Style.DIM + "Welcome to the Number Guessing Game")
print(Fore.GREEN + "You have 10 attempts to guess the number ranging from 1 to 100")

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

while attempts < max_attempts:
    try:
        guess: int = int(input(f"Guess the number ({attempts+1}/{max_attempts}): "))
    except ValueError:
        print(Fore.YELLOW + "Please enter a valid integer.")
        continue
    attempts += 1
    if guess < 1 or guess > 100:
        print("Between 1 and 100")
        attempts -= 1
    elif guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    elif guess == secret_number:
        score += 1
        print(Fore.GREEN + Style.BRIGHT + "Congratulations! You guessed the number!")
        print("Play again? (yes/no)")
        play_again = input().lower()
        if play_again == "no":
            while True:
                try:
                    Name = str(input("Enter your name: "))
                    break
                except ValueError:
                    print(Fore.YELLOW + "Please enter a valid integer for the name.")
            print(Fore.CYAN + Style.BRIGHT + f"Your score: {score}")
            with open(SCORE_FILE, 'a') as file:
                file.write(f"{Name}: {score}\n")
            print(Fore.CYAN + Style.BRIGHT + "High scores:")
            with open(SCORE_FILE, 'r') as file:
                content = file.read()
                print(content)
            print("Exiting... Score is: ", score)
            break
        elif play_again == "yes":
            secret_number = random.randint(1, 100)
            attempts = 0
            continue
        else:
            print(Fore.CYAN + Style.BRIGHT + f"Your score: {score}")
            with open(SCORE_FILE, 'a') as file:
                file.write(f"{Name}: {score}\n")
            print(Fore.CYAN + Style.BRIGHT + "High scores:")
            with open(SCORE_FILE, 'r') as file:
                content = file.read()
                print(content)




















