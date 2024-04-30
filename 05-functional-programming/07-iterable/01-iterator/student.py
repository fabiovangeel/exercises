class InclusiveRangeIterator:
    def __init__(self, start, end):
        self.__pos = start
        self.__end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos <= self.__end:
            result = self.__pos
            self.__pos += 1
            return result
        else:
            raise StopIteration()


class InclusiveRange:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def __iter__(self):
        return InclusiveRangeIterator(self.__start, self.__end)
