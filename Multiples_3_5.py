def solution(number: int) -> int:
    if number <= 0:
        return 0
    result_arr = []
    for i in range(number):
        if any((i % 3 ==0, i % 5 == 0)):
            result_arr.append(i)
    return sum(result_arr)


assert solution(4) == 3
assert solution(6) == 8
assert solution(15) == 45
