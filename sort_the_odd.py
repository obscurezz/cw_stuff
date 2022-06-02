def sort_array(source_array: list) -> list:
    odds = sorted((i for i in source_array if i % 2 != 0), reverse=True)
    return [i if i % 2 == 0 else odds.pop() for i in source_array]
