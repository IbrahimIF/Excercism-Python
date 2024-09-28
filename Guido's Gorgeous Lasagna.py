
# variables used in the math below
EXPECTED_BAKE_TIME = 40  
# variable containing the minutes lasganga would take based ont he cook book
PREPARATION_TIME = 2 
# variable containing the minutes taken for each layer of the lasgana


def bake_time_remaining(elapsed_bake_time = 5):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers = 8):
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers = 5, elapsed_bake_time = 8):

    preparation = number_of_layers * PREPARATION_TIME
    return preparation + elapsed_bake_time



# to print out the return value.
bake = bake_time_remaining()
preparation = preparation_time_in_minutes()
elapsed = elapsed_time_in_minutes()
print( 'bake:', bake, 'preparation:', preparation, 'elapsed:', elapsed)