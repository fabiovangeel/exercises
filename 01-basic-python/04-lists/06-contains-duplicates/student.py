def contains_duplicates(xs):
    for i in range(len(xs)):
        for z in range(i+1, len(xs)):
            if xs[i] == xs[z]:
                return True
    return False
