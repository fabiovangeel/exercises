class PadZip:
    def __init__(self, xs, ys, padding=None):
        self.__xs = iter(xs)
        self.__ys = iter(ys)
        self.__padding = padding

    def __iter__(self):
        return self

    def __next__(self):
        endcount = 0
        try:
            xs = next(self.__xs)
        except StopIteration:
            xs = self.__padding
            endcount += 1

        try:
            ys = next(self.__ys)
        except StopIteration:
            ys = self.__padding
            endcount += 1

        if endcount == 2:
            raise StopIteration()

        return (xs, ys)
