from numpy import array


def next_smaller(n):
    text_number_reversed = [int(i) for i in str(n)][::-1]

    for i in range(len(text_number_reversed)):
        try:
            if text_number_reversed[i] < text_number_reversed[i + 1]:
                suffix = text_number_reversed[:i + 1]
                prefix = text_number_reversed[i + 1:]
                break
        except IndexError:
            return -1

    arr_of_list = array(suffix)
    closest_value = arr_of_list[arr_of_list < prefix[0]].max()

    suffix[suffix.index(closest_value)] = prefix[0]
    prefix[0] = closest_value

    result_list = prefix[::-1] + suffix
    int_res = int(''.join(map(str, result_list)))

    if len(str(int_res)) == len(str(n)):
        return int_res
    else:
        return -1


print(next_smaller(100))
