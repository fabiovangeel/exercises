class Book:
    def __init__(self, title: str, isbn: str):
        if title is None or title.strip() == '':
            raise RuntimeError()

        isbn_cleaned = isbn.replace(' ', '').replace('-', '')

        if len(isbn_cleaned) != 13 or not isbn_cleaned.isdigit():
            raise RuntimeError()

        digits = list(map(int, isbn_cleaned))

        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                checksum += digit
            else:
                checksum += digit * 3

        if checksum % 10 != 0:
            raise RuntimeError()

        self._title = title
        self._isbn = isbn

    @property
    def title(self):
        return self._title

    @property
    def isbn(self):
        return self._isbn
