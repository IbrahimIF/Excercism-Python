def steps(number):
    num = number
    count = 0
    while num != 1:
        if number <= 0:
            raise ValueError("Only positive integers are allowed")
        if num % 2 == 0:
            num = num / 2
            count = count + 1
        elif num % 2 != 0:
            num = (num * 3) + 1
            count = count + 1
    return count

print(steps(9))