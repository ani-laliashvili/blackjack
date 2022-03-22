############### Blackjack Project #####################
from art import logo
import random

def deal_card():
    """
    :return: New random card from the list
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def deal_cards(user_cards, first_computer_card):
    """
    deal new card
    """
    print(f'Your cards: {user_cards}, current score {sum(user_cards)}')
    print(f'Computer\'s first card: {first_computer_card}')
    play = input('Type \'y\' to get another card, type \'n\' to pass: ')

    if play == 'y':
        user_cards.append(deal_card())

    return play

def got_blackjack(hand):
    """
    check if user or dealer have blackjack
    """
    if sum(hand) == 21 and len(hand) == 2:
        return True
    else:
        return False

def get_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        score = score - 11 + 1
    return score

def get_winner(user_cards, computer_cards):
    """
    get winner based on player hands
    """
    print(f'Your final hand: {user_cards}, final score: {get_score(user_cards)}')
    print(f'Computer\'s final hand: {computer_cards}, final score: {get_score(computer_cards)}')

    user_score = get_score(user_cards)
    computer_score = get_score(computer_cards)

    if got_blackjack(computer_cards):
        print('You Lose. Computer got a blackjack.')
    elif got_blackjack(user_cards):
        print('You Win. You got a blackjack.')
    elif user_score > 21:
        print('You Lose. You went over 21.')
    elif user_score == computer_score:
        print('Draw')
    elif user_score > computer_score:
        print('You Win. Your score was higher than dealer\'s.')
    elif user_score < computer_score:
        print('You Lose. Your score was lower than dealer\'s.')

def blackjack():
    """
    play blackjack
    """
    play = input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ')
    if play != 'y':
        print('Goodbye.')
        quit()

    print(logo)

    # Deal initial hand
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # Keep dealing as long as user does not go over 21 and elects to draw card
    while get_score(user_cards) <= 21 and play == 'y' and not got_blackjack(user_cards) and not got_blackjack(computer_cards):
        play = deal_cards(user_cards, computer_cards[0])

    # Dealer draws until they reach the score of 17
    while get_score(computer_cards) < 17 and not got_blackjack(user_cards) and not got_blackjack(computer_cards):
        computer_cards.append(deal_card())

    # Get the winner
    get_winner(user_cards, computer_cards)

    # Repeat game if prompted
    blackjack()

if __name__ == '__main__':
    ############### Our Blackjack House Rules #####################

    ## The deck is unlimited in size.
    ## There are no jokers.
    ## The Jack/Queen/King all count as 10.
    ## The the Ace can count as 11 or 1.
    ## The cards in the list have equal probability of being drawn.
    ## Cards are not removed from the deck as they are drawn.
    ## The computer is the dealer.

    # play
    blackjack()