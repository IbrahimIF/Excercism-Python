def exchange_money(budget, exchange_rate):

    return budget / exchange_rate



def get_change(budget, exchanging_value):

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):

    return denomination * number_of_bills



def get_number_of_bills(amount, denomination):

    return amount // denomination



def get_leftover_of_bills(amount, denomination):

    return amount % denomination


# to print out the return value.
exchange = exchange_money(8, 8)
change = get_change(8, 8)
value = get_value_of_bills(8, 8)
number = get_number_of_bills(8, 8)
leftover = get_leftover_of_bills(8, 8)
print( 'Money Exchange:', exchange, 'Change:', change, 'Value of bills:', value, 'Number of bills:', number, 'leftover of bills:', leftover)