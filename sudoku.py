from math import isqrt
from random import sample


class Sudoku:
    def __init__(self):
        self.arr = []

    def __repr__(self):
        return self.arr

    def create_object(self, length):
        block = isqrt(length)
        if block ** 2 == length:
            def pattern(r, c):
                return (block * (r % block) + r // block + c) % length

            def shuffle(s):
                return sample(s, len(s))

            r_base = range(block)
            rows = [g * block + r for g in shuffle(r_base) for r in shuffle(r_base)]
            cols = [g * block + c for g in shuffle(r_base) for c in shuffle(r_base)]
            nums = shuffle(range(1, length + 1))
            self.arr = [[nums[pattern(r, c)] for c in cols] for r in rows]
            return self.arr
        raise ValueError('Not a valid sudoku')

    @property
    def length(self):
        return len(self.arr)

    @property
    def block(self):
        return isqrt(self.length)

    def is_valid(self):

        test_arr = [i for i in range(1, self.length + 1)]

        is_vaild_value = lambda r: (
                isinstance(r, list) and len(r) == self.length and all(map(lambda d: type(d) == int, r)))

        if not all(map(is_vaild_value, self.arr)):
            return False

        # check valid rows
        flag_row = all(sorted(line) == test_arr for line in self.arr)

        # check valid cols
        temp_arr = [[d[x] for d in self.arr] for x in range(self.length)]
        flag_col = all(sorted(temp_arr[x]) == test_arr for x in range(self.length))

        # check valid blocks
        temp_arr = [[d[x] for d in self.arr[i:self.block + i] for x in range(j, self.block + j)] for i in
                    range(0, self.length, self.block) for j in range(0, self.length, self.block)]
        flag_block = all(sorted(temp_arr[x]) == test_arr for x in range(self.length))

        return all((flag_row, flag_col, flag_block))


sud1 = Sudoku()
sud1.create_object(9)
for line in sud1.arr:
    print(line)

# print(sud1.is_valid())
# sud1.arr = [[1, 2, 3],[1, 2, 3],[1, 2, 3]]
# for line in sud1.arr:
#     print(line)
# print(sud1.is_valid())
#
