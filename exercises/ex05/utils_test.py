"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens() -> None:
xs: list[int] = []
assert only_evens(xs) == 0


def test_sub() -> None:
xs: list[int] = []
assert sub(xs) == 0


def test_concat() -> None:
xs: list[int] = []
assert concat(xs) == 0



__author__ = "730358517"