import uuid


class ID_UTIL:
    @staticmethod
    def generate_id():
        return uuid.getnode()
