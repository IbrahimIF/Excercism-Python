"""
Functions for tracking poker hands and assorted card tasks.
"""


def get_rounds(number):
    """
    Create a list containing the current and next two round numbers.
    """
    rounds = []
    for amount in range(3):
        rounds.append(number+amount)
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """
    Concatenate two lists of round numbers.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """
    Check if the list of rounds contains the specified number.
    """
    if number in rounds:
        return True
    return False
    


def card_average(hand):
    """
    returns the average card value from the given list
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """
    Return if the (average of first and last card values) OR ('middle' card) == calculated average.
    """
    first_hand = hand[-1]
    if hand[0] == 0:
        last_hand = hand[1]
    else:
        last_hand = hand[0]
        
    middle = int(len(hand) / 2)
    if sum(hand) / len(hand) == (first_hand+last_hand) / 2:
        return True
    if sum(hand) / len(hand) == hand[middle]:
        return True
    return False


def average_even_is_average_odd(hand):
    """
    returns a Boolean indicating if the average of the cards at even indexes is the same as 
    the average of the cards at odd indexes.
    """
    even_hand =[]
    odd_hand = []
    even_hand.append(0)
    odd_hand.append(0)
    
    for _, number in enumerate(hand):
        if number % 2 == 0:
            even_hand.append(number)
        else:
            odd_hand.append(number)

    if sum(even_hand) == even_hand[-1]:
        even = sum(even_hand)
    else:
        even = sum(even_hand) / 2
    
    if sum(odd_hand) == odd_hand[-1]:
        odd = sum(odd_hand)
    else:
        odd = sum(odd_hand) / 2
    
    if odd == 0 or even == 0 :
        return True
    if odd == even:
        return True
    return False

    

def maybe_double_last(hand):
    """
    takes a hand and checks if the last card is a Jack (11). 
    If the last card is a Jack (11), double its value before returning the hand.
    """
    if hand[-1] == 11:
        newhand = hand[0:-1] + [hand[-1]*2]
        return newhand
    return hand



# to print out the return value.

rounds = get_rounds(27)
concatenate = concatenate_rounds([27, 28, 29], [35, 36])
list_round = list_contains_round([27, 28, 29, 35, 36], 29)
average = card_average([5, 6, 7])
alternate = approx_average_is_average([2, 3, 4, 8, 8])
average_even_odd = average_even_is_average_odd([1, 2, 3])
double = maybe_double_last([5, 9, 11])


# Output
print('| Track Poker Rounds:', rounds, 
      '| keep all rounds:', concatenate, 
      '| find prior rounds:', list_round, 
      '| averaging card values:', average, 
      '| Return true if card value = average:', alternate, 
      '| return true if average of even card value  = average of odd card value:', average_even_odd,
      '| double the last card  its a jack:', double,)

