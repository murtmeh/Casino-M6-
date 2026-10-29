import random
import os
import time

balance = 1000

roulette_numbers = {
	"red": {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36},
	"black": {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35},
	"green": {0}
}

def blackjack(): # Långt ifrån klar :´(
	print("Blackjack is not available yet.")
	pass

def roulette(): # Har påbörjat, man kan endast välja hur mycket man bettar.
	global balance
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

	while True: # Spelaren får välja vad de vill satsa på, nummer eller färg.
		guess_text = input("Pick a number from 0 to 36 or a color (Red/Black) to bet on: ").strip().lower()
		if guess_text.isdigit() and 0 <= int(guess_text) <= 36:
			guess = int(guess_text)
			break
		elif guess_text in ("red", "black"):
			guess = guess_text
			break
		else:
			print("Please enter a whole number from 0 to 36 or Red/Black.")

	result = random.randint(0, 36)
	balance -= bet

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