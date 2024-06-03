import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize("string", [
    "((()))",
    "(()())",
    "()()()",
    "((()()))",
])
def test_matching_parentheses(string):
    assert matching_parentheses(string)


@pytest.mark.parametrize("string", [
    "((())",
    "(()()",
    ")))(((",
    "())()",
])
def test_non_matching_parentheses(string):
    assert not matching_parentheses(string)
