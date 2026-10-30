import random
import os
import time

balance = 1000

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

def dealer_play(deck, dealer_hand, player_hand, balance, bet):
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
	return balance
	

def blackjack(balance): # inte jättelångt från klar, men man kan betta!
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

	if hand_value(player_hand) == 21:
		print(f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
		print(f"Dealer's hand: {dealer_hand} (Value: {hand_value(dealer_hand)})")
		if hand_value(dealer_hand) == 21:
			print("It's a tie! Both you and the dealer have Blackjack.")
		else:
			print("Blackjack! You win!")
			balance += int(bet * 1.5)
		return balance

	print (f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
	print (f"Dealer's hand: {dealer_hand[0]} and [hidden]")
	move = input("Do you want to hit, stand or double down? (h/s/d): ").strip().lower()
	i = 0
	while True:
		if move == 'h':
			i += 1
			player_hand.append(deal_card(deck))
			print(f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
			if hand_value(player_hand) > 21:
				print("You bust! Dealer wins.")
				balance -= bet
				return balance
			move = input("Do you want to hit or stand? (h/s): ").strip().lower()
		elif move == 's':
			balance = dealer_play(deck, dealer_hand, player_hand, balance, bet)
			break
		elif move == 'd':
			bet_original = bet
			bet = bet * 2
			if bet > balance:
				bet = bet_original
				print("Insufficient balance to double down. You can only hit or stand.")
				move = input("Do you want to hit or stand? (h/s): ").strip().lower()
			else:
				print(f"You have doubled down. Your new bet is ${bet}.")
				player_hand.append(deal_card(deck))
				print(f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
				if hand_value(player_hand) > 21:
					print("You bust! Dealer wins.")
					balance -= bet
					return balance
				balance = dealer_play(deck, dealer_hand, player_hand, balance, bet)
				break
		else:
			if i == 0:
				print("Invalid input. Please enter 'h' to hit, 's' to stand, or 'd' to double down.")
				move = input("Do you want to hit, stand or double down? (h/s/d): ").strip().lower()
			else:
				print("Invalid input. Please enter 'h' to hit or 's' to stand.")
				move = input("Do you want to hit or stand? (h/s): ").strip().lower()

	return balance

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
    if choice == "1":
        balance = action(balance)
    elif action() is False:
        break
    time.sleep(2)