import random
import os
import time

balance = int(1000)

def card_value(card):
	rank = card.split(" of")[0]
	if rank in ['J', 'Q', 'K']:
		return 10
	elif rank == 'A':
		return 11
	else:
		return int(rank)

def hand_value(hand):
	value = sum(card_value(card) for card in hand)
	aces = sum(1 for card in hand if card.startswith('A'))
	while value > 21 and aces:
		value -= 10
		aces -= 1
	return value

def deal_card(deck):
	return deck.pop()

def blackjack(balance): # Långt ifrån klar :´( men man kan betta!
	print("Welcome to the Blackjack table.")
	print(f"Your balance is ${balance}."+"\n")
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

	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
	deck = []
	for suit in suits:
		for rank in ranks:
			card = f"{rank} of {suit}"
			deck.append(card)

	random.shuffle(deck)
	player_hand = [deal_card(deck), deal_card(deck)]
	dealer_hand = [deal_card(deck), deal_card(deck)]

	print (f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
	print (f"Dealer's hand: {dealer_hand[0]} and [hidden]")
	move = input("Do you want to hit or stand? (h/s): ").strip().lower()
	while move == 'h':
		player_hand.append(deal_card(deck))
		print(f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
		if hand_value(player_hand) > 21:
			print("You bust! Dealer wins.")
			balance -= bet
			return balance
		move = input("Do you want to hit or stand? (h/s): ").strip().lower()
	if move == 's':
		while hand_value(dealer_hand) < 17:
			dealer_hand.append(deal_card(deck))
		print(f"Dealer's hand: {dealer_hand} (Value: {hand_value(dealer_hand)})")
		if hand_value(dealer_hand) > 21:
			print("Dealer busts! You win.")
			balance += bet
		elif hand_value(player_hand) > hand_value(dealer_hand):
			print("You win!")
			balance += bet
		elif hand_value(player_hand) < hand_value(dealer_hand):
			print("Dealer wins.")
			balance -= bet
		else:
			print("It's a tie!")

	pass
	return balance

def roulette(): # Har påbörjat, man kan endast välja hur mycket man bettar.
	print("Welcome to the Roulette table.")
	print(f"Your balance is ${balance}."+"\n")
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

def show_menu(): # Reminder till vemsomhelst, ta bort TBA sen.
	print("\n=== Welcome to the Casino™ ===")
	print("1. Blackjack !(TBA)!")
	print("2. Roulette  !(TBA)!")
	print("3. Show balance")
	print("4. Quit")

print(f"You start with ${balance} in your balance.")
while True:
	show_menu()
	choice = input("Choose an option(1–4): ").strip()

	if choice == "1": # Inte påbörjad
		os.system("clear")
		blackjack(balance)
		time.sleep(2)

	elif choice == "2": # Inte påbörjad
		os.system("clear")
		roulette()
		time.sleep(2)

	elif choice == "3": # Klar, om man inte kan göra ngt mer med detta?
		os.system("clear")
		print(f"Your balance is ${balance}.")
		time.sleep(2)

	elif choice == "4": # Klar. Finns det ens något man kan lägga till här?
		os.system("clear")
		print("Thank you for playing. Goodbye!")
		time.sleep(2)
		break

	else:
		print("Invalid input. Please use a number between 1 and 4.")