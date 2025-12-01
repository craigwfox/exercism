def is_armstrong_number(number):
    num_str = str(number)
    total = 0
    for x in num_str:
        total += int(x) ** len(num_str)
    return number == total
