class Cycle:
    def __init__(self, xs):
        self.__xs = list(xs)
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__xs)
        return self.__xs[self.__index]
