def triangle(row):
    color_dict = {
        ('G', 'G'): 'G',
        ('R', 'R'): 'R',
        ('B', 'B'): 'B',
        ('B', 'G'): 'R',
        ('R', 'G'): 'B',
        ('B', 'R'): 'G',
    }
    new_row = ''
    if len(row) == 1:
        return row
    else:
        for i in range(len(row) - 1):
            for k, v in color_dict.items():
                if sorted((row[i], row[i + 1])) == sorted(k):
                    new_row += v
        return triangle(new_row)


print(triangle('RRGBRGBB'))
