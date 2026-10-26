import random
import os
import time

balance = 1000

def blackjack(): # Långt ifrån klar :´(
	print("Blackjack is not available yet.")
	pass

def roulette(): # Har påbörjat, man kan endast välja hur mycket man bettar.
	print("Welcome to the Roulette table.")
	show_balance()
	while True:
		bet = input("How much do you want to bet? ").strip()
		if bet.isdigit(): # .isdigit() returnerar True/False
			bet = int(bet)
			if bet > balance:
				print("Insufficient balance. Enter a lower amount")
			elif bet <= 0:
				print("Bets lower than 0 are prohibited.")
			else:
				break
		else:
			print("Invalid input.")

	print("Roulette is not available yet.")
	pass

def show_balance():
    print(f"Your balance is {balance}$."+"\n")

def show_menu(): # Reminder till vemsomhelst, ta bort TBA sen.
	print("=== Welcome to the Casino™ ===")
	print("1. Blackjack !(TBA)!")
	print("2. Roulette  !(TBA)!")
	print("3. Show balance")
	print("4. Quit")

def quit_game():
    print("Thank you for playing. Goodbye!")
    time.sleep(2)
    return False  

menuOptions = { # Dictionary replacing an if/elif/else block.
	"1": blackjack,
	"2": roulette,
	"3": show_balance,
	"4": quit_game,
}

print(f"You start with {balance}$ in your balance.")
while True:
    show_menu()
    choice = input(f"Choose an option (1–{len(menuOptions)}): ").strip()

    action = menuOptions.get(choice) # Accesses the function corresponding to each number
    if action is None:
        print(f"Invalid input. Please use a number between 1 and {len(menuOptions)}.")
        continue
	
    os.system("clear")
    if action() is False:
        break
    time.sleep(2)