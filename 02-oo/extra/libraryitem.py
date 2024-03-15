from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, author, id, status):
        self.title = title
        self.author = author
        self.id = id
        self.status = status


class CD(LibraryItem):

    def __init__(self, title, author, id, status, tracks):
        super().__init__(title, author, id, status)
        self.tracks = tracks


class Book(LibraryItem):

    def __init__(self, title, author, id, status, genre):
        super().__init__(title, author, id, status)
        self.genre = genre


class Strip(LibraryItem):

    def __init__(self, title, author, id, status):
        super().__init__(title, author, id, status)
