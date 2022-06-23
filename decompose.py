import math
from decimal import Decimal
from fractions import Fraction


def decompose(n: str) -> list:
    """some stuff about this func"""
    if not any((x in ['.', '/']) for x in n):
        return []

    if "." in n and "/" not in n:
        n = str(Fraction(Decimal(n)))

    numerator, denominator = map(int, (n.split('/')[0], n.split('/')[1]))

    result_list = []

    if numerator > denominator:
        result_list.append(str(numerator // denominator))
        estimate = str(round(numerator % denominator, 1))
        result_list += decompose(f'{estimate}/{denominator}')
    else:
        while numerator != 0:
            x = math.ceil(denominator / numerator)

            result_list.append(f'1/{x}')

            numerator = x * numerator - denominator
            denominator = denominator * x

    return result_list


print(decompose('79/7'))
