import random
import os
import time

balance = 1000

def blackjack(): # Långt ifrån klar :´(
	print("Blackjack is not available yet.")
	pass

def roulette(): # -||-
	print("Roulette is not available yet.")
	pass

def show_menu(): # Reminder till vemsomhelst, ta bort TBA sen.
	print("\n=== Welcome to the Casino™ ===")
	print("1. Blackjack !(TBA)!")
	print("2. Roulette  !(TBA)!")
	print("3. Show balance")
	print("4. Quit")

print(f"You start with {balance}$ in your balance.")
while True:
	show_menu()
	choice = input("Choose an option(1–4): ").strip()

	if choice == "1": # Inte påbörjad
		os.system("clear")
		blackjack()
		time.sleep(2)

	elif choice == "2": # Inte påbörjad
		os.system("clear")
		roulette()
		time.sleep(2)

	elif choice == "3": # Klar, om man inte kan göra ngt mer med detta?
		os.system("clear")
		print(f"Your balance is {balance}$.")
		time.sleep(2)

	elif choice == "4": # Klar. Finns det ens något man kan lägga till här?
		os.system("clear")
		print("Thank you for playing. Goodbye!")
		time.sleep(2)
		break

	else:
		print("Invalid input. Please use a number between 1 and 4.")