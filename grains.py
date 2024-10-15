# Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

number = 1 #this represents the chessboard tile, and will provide the amount of garins on that specific tile

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        i = number -1

        return 2**i

        
## the total number of grains on the whole of the chess board

def total():
    array = []
    for i in range(1, 66):
        number = i - 1
        amount = 2**number 
        array.append(amount)

    for x in array:
        total_amount = 0 + x - 1

    return total_amount


# to print out the return value.

square = square(number)
total = total()


# Output
print('| square:', square, 
      '| total:', total, )