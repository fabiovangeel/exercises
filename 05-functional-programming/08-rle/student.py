def rle_encode(data):
    data = iter(data)
    try:
        last = next(data)
        count = 1
        for datum in data:
            if last == datum:
                count += 1
            else:
                yield (last, count)
                last = datum
                count = 1
        yield (last, count)
    except StopIteration:
        pass


def rle_decode(data):
    for datum, count in data:
        for _ in range(count):
            yield datum
