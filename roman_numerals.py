class RomanNumerals:
    roman_dict = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }

    def to_roman(val):
        a = ''
        while val != 0:
            for k, v in RomanNumerals.roman_dict.items():
                a += (val // v) * k
                val -= (val // v) * v

        return a

    def from_roman(roman_num):
        s = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i + 2] in RomanNumerals.roman_dict:
                s += RomanNumerals.roman_dict[roman_num[i:i + 2]]
                i += 2
            else:
                s += RomanNumerals.roman_dict[roman_num[i]]
                i += 1
        return s
