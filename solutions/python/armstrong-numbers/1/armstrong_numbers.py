def is_armstrong_number(number):
    str_array = [int(d) for d in str(number)]
    total = 0
    for x in str_array:
        total += x ** len(str_array)
    return True if number == total else False
