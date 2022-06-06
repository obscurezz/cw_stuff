def last_digit(lst: list) -> int:
    if len(lst) == 0 or lst == [0, 0]:
        return 1

    result = 1

    for num in reversed(lst):
        result = num ** (result if result < 4 else result % 4 + 4)

    return result % 10


print(last_digit([937640, 767456, 981242]))
