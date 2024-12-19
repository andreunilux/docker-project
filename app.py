# already build in python library
import random
# needs to be installed 
from colorama import Fore, Style




def number_guessing_game():
    """
    A simple CLI-based number guessing game.
    """
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





def display_main_menu():
    """
    Display the main menu with available options.
    """
    print(Fore.CYAN + "\nWelcome to the CLI Game Hub!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Choose from the following options:" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Play Number Guessing Game" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Exit" + Style.RESET_ALL)



def handle_menu_choice(choice):
    """
    Handle the user's menu choice and call the corresponding functionality.
    """
    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        print(Fore.CYAN + "Goodbye! Thanks for playing." + Style.RESET_ALL)
        exit(0)
    else:
        print(Fore.RED + "Invalid choice. Please select a valid option." + Style.RESET_ALL)




def main():
    """
    The main entry point for the CLI app. Displays the menu and processes user input.
    """
    while True:
        display_main_menu()
        choice = input(Fore.WHITE + "Enter your choice: " + Style.RESET_ALL).strip()
        handle_menu_choice(choice)

if __name__ == "__main__":
    main()


