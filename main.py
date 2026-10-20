import random
import os
import time

balance = 1000

def show_menu():
	print("\n=== Welcome to the Casino™ ===")
	print("1. Blackjack")
	print("2. Roulette")
	print("3. Show balance")
	print("4. Quit")

print("You start with 1000$ in your balance.")
while True:
	show_menu()
	choice = input("Choose an option(1–4): ").strip()

	if choice == "1":
		os.system("clear")
		print("Blackjack is not available yet.")
		time.sleep(2)
	elif choice == "2":
		os.system("clear")
		print("Roulette is not available yet.")
		time.sleep(2)
	elif choice == "3":
		os.system("clear")
		print(f"Your balance is {balance}$.")
		time.sleep(2)
	elif choice == "4":
		os.system("clear")
		print("Thank you for playing. Goodbye!")
		time.sleep(2)
		break
	else:
		print("Invalid choice. Please select an option between 1 and 4.")