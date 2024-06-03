import pytest
from search import *
from student import Student


@pytest.mark.parametrize("students, target_id", [
    [[Student(i) for i in range(100)], 1],
    [[Student(i) for i in range(100)], 99],
    [[Student(i) for i in range(100)], 33],
    [[Student(i) for i in range(100)], 66],
    [[Student(i) for i in range(100)], 50],
    [[Student(i) for i in range(100)], 51],
    [[Student(i) for i in range(100)], 49],
])
def test_linear_search(students, target_id):
    assert linear_search(students, target_id).id == target_id


@pytest.mark.parametrize("students, target_id", [
    [[Student(i) for i in range(100)], 1],
    [[Student(i) for i in range(100)], 99],
    [[Student(i) for i in range(100)], 33],
    [[Student(i) for i in range(100)], 66],
    [[Student(i) for i in range(100)], 50],
    [[Student(i) for i in range(100)], 51],
    [[Student(i) for i in range(100)], 49],
])
def test_binary_search(students, target_id):
    assert binary_search(students, target_id).id == target_id
