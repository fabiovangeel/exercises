def findMaximum(lst):
    if len(lst) == 0:
        raise IndexError
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = findMaximum(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest
