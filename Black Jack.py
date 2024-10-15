card = '4'
card_one = '2'
card_two = 'K'
def value_of_card(card):

    face_card = {'J', 'Q', 'K'}
    
    if card in face_card:
        return 10
    elif card == 'A':
        return 1
    else: 
        return int(card)


def higher_card(card_one, card_two):

    face_card = {'J', 'Q', 'K', '10'}
    ace_card = {'A', '1'}
    
    if card_one in face_card:
        one = 10
    elif card_one in ace_card:
        one = 1
    else: 
        one = int(card_one)
        
    if card_two in face_card:
        two = 10
    elif card_two in ace_card:
        two = 1
    else: 
        two = int(card_two)
        
    if one == two:
        return card_one, card_two
    elif one > two:
        return card_one
    else: 
        return card_two

    

def value_of_ace(card_one, card_two):

    face_card = {'J', 'Q', 'K', '10'}
    ace_card = {'A'}

    if card_one in face_card:
        one = 10
    elif card_one in ace_card:
        one = 11
    else: 
        one = int(card_one)
        
    if card_two in face_card:
        two = 10
    elif card_two in ace_card:
        two = 11
    else: 
        two = int(card_two)
        
    if one + two <= 10:
        return 11
    elif one + two > 10:
        return 1
    else: 
        return 1

    


def is_blackjack(card_one, card_two):

    face = {'J', 'Q', 'K', '10'}
    ace = {'A'}
    if (card_one in ace or card_two in ace) and (card_one in face or card_two in face):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):

    face = {'J', 'Q', 'K'}

    if (card_one in face and card_two in face) or card_one == card_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):

    face_card = {'J', 'Q', 'K', '10'}
    ace_card = {'A', '1'}
    
    if card_one in face_card:
        one = 10
    elif card_one in ace_card:
        one = 1
    else: 
        one = int(card_one)
        
    if card_two in face_card:
        two = 10
    elif card_two in ace_card:
        two = 1
    else: 
        two = int(card_two)

    if (one + two == 9) or (one + two == 10) or (one + two == 11):
        return True
    else:
        return False

    

# to print out the return value.

value_Card = value_of_card(card)
Higher_Card = higher_card(card_one, card_two)
value_Ace = value_of_ace(card_one, card_two)
Is_blackjack = is_blackjack(card_one, card_two)
Can_Split_Pairs = can_split_pairs(card_one, card_two)
Can_Double_Down = can_double_down(card_one, card_two)

# Output
print('|Value of Card:', value_Card, 
      '| higher_card:', Higher_Card, 
      '| value_Ace:', value_Ace, 
      '| is it blackjack?:', Is_blackjack, 
      '| can the cards be split?:', Can_Split_Pairs, 
      '| can player place a double down bet?:', Can_Double_Down)