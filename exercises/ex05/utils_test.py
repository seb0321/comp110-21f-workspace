"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test Only Evens Empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_even_1() -> None:
    """Test Only Evens 1."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_even_2() -> None:
    """Test Only Evens 1."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_sub_empty() -> None:
    """Test Sub Empty"""
    xs: list[int] = []
    assert sub(xs, 6, 7) == []


def test_sub_1() -> None:
    """Test Sub 1."""
    xs: list[int] = []
    assert sub(xs, 1, 3) == [20, 30]


def test_sub() -> None:
    """Test Sub 2."""
    xs: list[int] = []
    assert sub(xs, 1, 4) == [20, 30, 40]


def test_concat_1() -> None:
    """Test Concat 1."""
    xs: list[int] = [1, 2, 3]
    yay: list[int] = [6, 7, 11]
    assert concat(xs, yay) == [1, 2, 3, 6, 7, 11]


def test_concat_empty() -> None:
    """Test Concat Empty."""
    xs: list[int] = []
    yay: list[int] = []
    assert concat(xs, yay) == []


def test_concat() -> None:
    """Test Concat."""
    xs: list[int] = [4, 5, 6]
    yay: list[int] = [23, 2, 4]
    assert concat(xs, yay) == [4, 5, 6, 23, 2, 4]


__author__ = "730358517"