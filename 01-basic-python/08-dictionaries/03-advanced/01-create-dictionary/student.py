def create_dictionary(keys, values):
    d = {}
    for x, y in zip(keys, values):
        d[x] = y
    return d
