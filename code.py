import numpy as np 
import random

def hand_total(hand, dealer_card):
    
    total = sum(hand)
    return total, dealer_card, hand[0], hand[1]
    
def ace(hand):
    
    if 'A' in hand:
        return 'soft hand'
    
def to_split(hand):
    no_cards=len(hand)
    if no_cards == 2:
        if hand[0]==hand[1]:
            card = hand[0]
            return 'split',card
        if hand[0]!=hand[1]:
            return 'dont'
        
def hand_aces(hand):
    
    if hand[0] == 'A':
        hand[0] = 1
        
    if hand[1] == 'A':
        hand[1] = 1
        
    return hand

def tester(hand):
    
    player_hand = hand_aces(hand)
    player_total = sum(player_hand)
    no_cards = len(player_hand)
    aces_count = 1*(1 in player_hand)
    soft_total = player_total
    if soft_total == 21 and no_cards == 2:
        return 'BlackJack!'
    
    if player_total <= 11:
        soft_total= player_total + 10*aces_count
        return soft_total

def BasicStrategy(hand, dealer_card):
    
    player_hand = hand_aces(hand)
    player_total = sum(player_hand)
    no_cards = len(player_hand)
    aces_count = 1*(1 in player_hand)
    soft_total = player_total
    if no_cards < 2:
        return "Not enough cards to form a hand"

    #hand becomes soft if ace is present
    
        
    if player_total <= 11:
        soft_total= player_total + 10*aces_count
        
    if soft_total == 21 and no_cards == 2:
        return 'BlackJack!'
    

    
    ######## Basic Strategy #######

    
    #split hands
    
    if no_cards == 2:
        
        if player_hand[0] == player_hand[1]:
            card = player_hand[0]
        
            if card == 2 and dealer_card in [2,3,4,5,6,7]:
                return 'split'
            if card == 2 and dealer_card in [8,9,10,'A']:
                return 'hit'
            
            if card == 3 and dealer_card in [2,3,4,5,6,7]:
                return 'split'
            if card == 3 and dealer_card in [8,9,10,'A']:
                return 'hit'
            
            if card == 4 and dealer_card in [5,6]:
                return 'split'
            if card == 4 and dealer_card in [2,3,4,7,8,9,10,'A']:
                return 'hit'
            
            if card == 6 and dealer_card in [2,3,4,5,6]:
                return 'split'
            if card == 6 and dealer_card in [7,8,9,10,'A']:
                return 'hit'
            
            if card == 7 and dealer_card in [2,3,4,5,6,7]:
                return 'split'
            if card == 7 and dealer_card in [8,9,10,'A']:
                return 'hit'
            
            if card == 9 and dealer_card in [2,3,4,5,6,8,9]:
                return 'split'
            if card == 9 and dealer_card in [7,10,'A']:
                return 'stand'
            
            if card == 8:
                return 'split'
            
            if card == 'A':
                return 'split'
    
    #soft hands
            
    if soft_total == 13 and dealer_card in [2,3,4,7,8,9,10,'A']:
        return 'hit soft'
    if soft_total == 13 and dealer_card in [5,6]:
        return 'double'
    
    if soft_total == 14 and dealer_card in [2,3,4,7,8,9,10,'A']:
        return 'hit soft'
    if soft_total == 14 and dealer_card in [5,6]:
        return 'double'
    
    if soft_total == 15 and dealer_card in [2,3,7,8,9,10,'A']:
        return 'hit soft'
    if soft_total == 15 and dealer_card in [4,5,6]:
        return 'double'
    
    if soft_total == 16 and dealer_card in [2,3,7,8,9,10,'A']:
        return 'hit soft'
    if soft_total == 16 and dealer_card in [4,5,6]:
        return 'double'
    
    if soft_total == 17 and dealer_card in [2,7,8,9,10,'A']:
        return 'hit soft'
    if soft_total == 17 and dealer_card in [3,4,5,6]:
        return 'double'
    
    if soft_total == 18 and dealer_card in [3,4,5,6]:
        return 'double'
    if soft_total == 18 and dealer_card in [2,7,8]:
        return 'stand'
    if soft_total == 18 and dealer_card in [9,10,'A']:
        return 'hit'
    
    if soft_total > 18:
        return 'stand'
    
    # Hard hands

    if player_total < 9:
        return 'hit'

    if player_total == 9 and dealer_card in [3,4,5,6]:
        return 'double'
    
    if player_total == 9 and dealer_card in [2,7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 10 and dealer_card in [10, 'A']:
        return 'hit'
    
    if player_total == 10 and dealer_card in [2,3,4,5,6,7,8,9]:
        return 'double'
    
    if player_total == 11 and dealer_card in [2,3,4,5,6,7,8,9,10]:
        return 'double'
    
    if player_total == 11 and dealer_card == 'A':
        return 'hit'
    
    if player_total == 12 and dealer_card in [2,3,7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 12 and dealer_card in [4,5,6]:
        return 'stand'
    
    if player_total == 13 and dealer_card in [7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 13 and dealer_card in [2,3,4,5,6]:
        return 'stand'
    
    if player_total == 14 and dealer_card in [7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 14 and dealer_card in [2,3,4,5,6]:
        return 'stand'
    
    if player_total == 15 and dealer_card in [7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 15 and dealer_card in [2,3,4,5,6]:
        return 'stand'
    
    if player_total == 16 and dealer_card in [7,8,9,10,'A']:
        return 'hit'
    
    if player_total == 16 and dealer_card in [2,3,4,5,6]:
        return 'stand'
    
    if player_total > 16:
        return 'stand'   


def hand_result(bet=5, player_hand = 'f', dealer_card = 's', hard_code = 2):
    
    deck = np.array([1,2,3,4,5,6,7,8,9,10,10,10,10])
    
    hard_stay = False
    
    if type(player_hand) == str:
        
        player_hand = [random.choice(deck), random.choice(deck)]
        
    if player_hand == [1]:
        hard_stay == True
    
    while len(player_hand)<2:
        
        player_hand.append(random.choice(deck))
        
    if type(dealer_card == str):
        
        dealer_card = random.choice(deck)
    dealer_hand = [dealer_card]
    
    if hard_stay == False:
        
        if BasicStrategy(player_hand, dealer_hand) == 'BlackJack':

            dealer_hand.append(random.choice(deck))
            if 1 in (dealer_hand):
                if sum(dealer_hand)== 11:
                    return 0
                #blackjack payed 3/2
            return bet * 1.5

        if type(hard_code) == str:
            if hard_code == 'hit':
                player_hand.append(random.choice(deck))
                return hand_result(bet, player_hand, dealer_card, hard_code)

            if hard_code == 'double':
                if len(player_hand) == 2:
                    player_hand.append(random.choice(deck))
                    bet = bet * 2
                    if sum(player_hand) > 21:
                        return 0 - bet
                else:
                    return 'cant double'

            if hard_code == 'split':
                if len(player_hand) == 2:
                    if player_hand[0] == player_hand[1]:

                        result = hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split')
                        result += hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split')

                        return result

                    else: 
                        return BasicStrategy(bet=bet, player_hand= player_hand, dealer_card=dealer_card)
                else:
                    return BasicStrategy(bet=bet, player_hand= player_hand, dealer_card=dealer_card)
        else:

            while BasicStrategy(player_hand, dealer_hand) == 'hit':

                player_hand.append(random.choice(deck))
                if sum(player_hand)>21:
                    return 0 - bet

            if BasicStrategy(player_hand, dealer_card) == 'split':
                result = hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split')
                result += hand_result(bet=bet, player_hand=[player_hand[0]], dealer_card=dealer_card, hard_code= 'Split')

                return result

        while True:

            dealer_hand.append(random.choice(deck))
            dealer_score = sum(dealer_hand)
            soft_score = dealer_score
            if dealer_score <= 11 and 1 in dealer_hand:
                soft_score += 10

            if len(dealer_hand) == 2 and soft_score == 21:
                return 0 - bet

            player_score = sum(player_hand)

            if player_score <= 11 and 1 in player_hand:
                player_score += 10

            if soft_score > 21:
                return bet 

            if player_score > soft_score:
                return bet

            if player_score == soft_score:
                return 0

            if player_score < soft_score:
                return 0 - bet
    
    if hard_stay == True:
        
        dealer_hand.append(random.choice(deck))
        dealer_score = sum(dealer_hand)
        soft_score = dealer_score
        if dealer_score <= 11 and 1 in dealer_hand:
            soft_score += 10
            
        if len(dealer_score) == 2 and soft_score == 21:
            return 0 - bet
        
        player_score = sum(player_hand)
        if player_score <= 11 and 1 in player_hand:
            player_score += 10
            
        if soft_score >= 17:
            if soft_score > 21:
                return bet 
            
            if player_score == soft_score:
                return 0
            
            if player_score < soft_score:
                return 0 - bet
            
