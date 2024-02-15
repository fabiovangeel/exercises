def odd_keys_dict(dictionary):
    d = {}
    for key, value in dictionary.items():
        if key % 2 != 0:
            d[key] = value
    return d
