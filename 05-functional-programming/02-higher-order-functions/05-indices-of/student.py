def indices_of(xs, condition):
    return [x for x in range(len(xs)) if condition(xs[x])]
