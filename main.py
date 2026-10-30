import random
import os
import time

balance = 1000

roulette_numbers = {
    "red": {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36},
    "black": {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35},
    "green": {0}
}


def blackjack():  # Långt ifrån klar :´(
    print("Blackjack is not available yet.")
    pass


def roulette():  # Kanske klar ?!
    global balance
    print("Welcome to the Roulette table.")

    while True:
        show_balance()
        if balance <= 0:
            print("You don't have enough money to place another bet.")
            break

        while True:
            bet_text = input("How much do you want to bet? ").strip()
            if bet_text.isdigit():
                bet = int(bet_text)
                if bet > balance:
                    print("Insufficient balance. Enter a lower amount.")
                elif bet <= 0:
                    print("Bets lower than 0 are prohibited.")
                else:
                    break
            else:
                print("Invalid input.")

        while True:  # Spelaren får välja vad de vill satsa på, nummer eller färg.
            guess_text = input(
                "Pick a number from 0 to 36 or a color (Red/Black/Green) to bet on: "
            ).strip().lower()
            if guess_text.isdigit() and 0 <= int(guess_text) <= 36:
                guess = int(guess_text)
                break
            elif guess_text in ("red", "black", "green"):
                guess = guess_text
                break
            else:
                print("Please enter a whole number from 0 to 36 or Red/Black/Green.")

        result = random.randint(0, 36)
        balance -= bet
        result_color = None

        for color, numbers in roulette_numbers.items():
            if result in numbers:
                result_color = color
                break
            
        spins = random.randint(3, 6)
        for _ in range(spins):
            print("Spinning...")
            time.sleep(1)

        print(f"\n The spin landed on {result} ({result_color}).")

        if guess == result or (guess == "green" and result_color == "green"):
            balance += bet * 36
            print(f"You won {bet * 35}$ profit!")
        elif guess == result_color:
            balance += bet * 2
            print(f"You won {bet}$ profit!")
        else:
            print("Better luck next time.")

        show_balance()
        if balance <= 0:
            print("You don't have enough money to place another bet.")
            break

        while True:
            play_again = input("Play another round? (y/n): ").strip().lower()
            if play_again in ("y", "yes"):
                break
            if play_again in ("n", "no"):
                return
            print("Please enter yes(y) or no(n).")


def show_balance():
    print(f"Your balance is {balance}$.\n")


def show_menu():  # Reminder till vemsomhelst, ta bort TBA sen.
    print("=== Welcome to the Casino™ ===")
    print("1. Blackjack !(TBA)!")
    print("2. Roulette  !(TBA)!")
    print("3. Show balance")
    print("4. Quit")


def quit_game():
    print("Thank you for playing. Goodbye!")
    time.sleep(2)
    return False


menuOptions = {  # Dictionary replacing an if/elif/else block.
    "1": blackjack,
    "2": roulette,
    "3": show_balance,
    "4": quit_game,
}


print(f"You start with {balance}$ in your balance.")
while True:
    show_menu()
    choice = input(f"Choose an option (1–{len(menuOptions)}): ").strip()

    action = menuOptions.get(choice)  # Accesses the function corresponding to each number
    if action is None:
        print(f"Invalid input. Please use a number between 1 and {len(menuOptions)}.")
        continue

    os.system("clear")
    if action() is False:
        break
    time.sleep(2)