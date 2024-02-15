def remove_duplicates(xs):
    ys = set()
    result = []

    for i in xs:
        if i not in ys:
            ys.add(i)
            result.append(i)
    return result
