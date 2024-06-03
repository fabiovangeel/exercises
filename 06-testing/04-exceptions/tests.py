import pytest
from book import Book


@pytest.mark.parametrize(('title', 'isbn'), [
    ("Title", "978-3-16-148410-0"),
    ("Another Title", "978-3-16-148410-0"),
    ("Yet Another Title", "978-3-16-148410-0"),
])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize(('title', 'isbn'), [
    ("", "978-3-16-148410-0"),
    (" ", "978-3-16-148410-0"),
    (None, "978-3-16-148410-0"),
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)


@pytest.mark.parametrize(('title', 'isbn'), [
    ("Title", "978-3-16-148410-"),
    ("Another Title", "978-3-16-148410-"),
    ("Yet Another Title", "978-3-16-148410-"),
    ("Title", "978-3-16-148410-00"),
    ("Another Title", "978-3-16-148410-00"),
    ("Yet Another Title", "978-3-16-148410-00"),
    ("Title", "978-3-16-148410-000"),
    ("Another Title", "978-3-16-148410-000"),
    ("Yet Another Title", "978-3-16-148410-000"),
    ("Title", "978-3-16-148410-0000"),
    ("Another Title", "978-3-16-148410-0000"),
    ("Yet Another Title", "978-3-16-148410-0000"),
    ("Title", "978-3-16-148410-00000"),
    ("Another Title", "978-3-16-148410-00000"),
    ("Yet Another Title", "978-3-16-148410-00000"),
    ("Title", "978-3-16-148410-000000"),
    ("Another Title", "978-3-16-148410-000000"),
    ("Yet Another Title", "978-3-16-148410-000000"),
    ("Title", "978-3-16-148410-0000000"),
    ("Another Title", "978-3-16-148410-0000000"),
    ("Yet Another Title", "978-3-16-148410-0000000"),
    ("Title", "978-3-16-148410-00000000"),
    ("Another Title", "978-3-16-148410-00000000"),
    ("Yet Another Title", "978-3-16-148410-00000000"),
    ("Title", "978-3-16-148410-000000000"),
    ("Another Title", "978-3-16-148410-000000000"),
    ("Yet Another Title", "978-3-16-148410-000000000"),
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
