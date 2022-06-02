def anagrams(word: str, words: list) -> list:
    result = [i for i in words if sorted(word) == sorted(i)]
    return result


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
