class Duration:
    def __init__(self, *, time_in_seconds):
        self.__time_in_seconds = time_in_seconds

    @staticmethod
    def from_seconds(amount):
        return Duration(time_in_seconds=amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(time_in_seconds=amount*60)

    @staticmethod
    def from_hours(amount):
        return Duration(time_in_seconds=amount*3600)

    @property
    def seconds(self):
        return self.__time_in_seconds

    @property
    def minutes(self):
        return self.__time_in_seconds / 60

    @property
    def hours(self):
        return self.__time_in_seconds / 3600
