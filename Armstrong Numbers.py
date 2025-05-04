"An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits."

def is_armstrong_number(number):
    group = 0
    for num in str(number):
        calc = pow(int(num), len(str(number)))
        group = group + calc
    print(group)
    return( True if group == number else False)


print(is_armstrong_number(153))
