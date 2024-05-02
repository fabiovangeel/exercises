def cycle(xs):
    index = 0
    while True:
        yield xs[index]
        index = (index + 1) % len(xs)
