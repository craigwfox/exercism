def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    total = 0
    i = 1
    while i <= number:
        total = total * 2 if total > 0 else 1
        i += 1
    return total


print(square(64))


def total():
    max = 0
    total = 0
    i = 1
    while i <= 64:
        total = total * 2 if total > 0 else 1
        max = max + total
        i += 1
    return max
