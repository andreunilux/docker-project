import random
from colorama import Fore, Style




def number_guessing_game():
    print(Fore.CYAN + "Welcome to the Number Guessing Game!" + Style.RESET_ALL)
    print(Fore.YELLOW + "I have selected a number between 1 and 100. Can you guess it?" + Style.RESET_ALL)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input(Fore.WHITE + "Enter your guess: " + Style.RESET_ALL))
            attempts += 1
            
            if guess < secret_number:
                print(Fore.RED + "Too low! Try again." + Style.RESET_ALL)
            elif guess > secret_number:
                print(Fore.RED + "Too high! Try again." + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Congratulations! You've guessed the number in {attempts} attempts." + Style.RESET_ALL)
                break
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)




def main():
    number_guessing_game()
    
    
    

            
if __name__ == "__main__":
    main()





