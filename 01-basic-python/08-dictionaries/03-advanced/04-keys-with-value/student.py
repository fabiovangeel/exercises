def keys_with_value(dictionary, value):
    lst = []
    for k, v in dictionary.items():
        if v == value:
            lst.append(k)
    return lst
