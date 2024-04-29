def merge_dictionaries(d1, d2, merge_function):
    for key in d2:
        if key in d1:
            d1[key] = merge_function(d1[key], d2[key])
        else:
            d1[key] = d2[key]
    return d1
