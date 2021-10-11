"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count 


def invert() -> None:
    """Test Invert Empty."""
    xs: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    assert invert(xs) == KeyError


def invert_1() -> None:
    """Test Invert 1."""
    xs: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def invert_2() -> None:
    """Test Invert 1."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def favorite_color_1() -> None:
    """Test Count Empty."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == 'blue'


def favorite_color_2() -> None:
    """Test Count 1."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"}
    assert favorite_color(xs) == 'yellow'


def favorite_color_3() -> None:
    """Test Count 2."""
    xs: dict[str, str] = {"Marc": "orange", "Ezri": "orange", "Kris": "blue"}
    assert favorite_color(xs) == 'orange'


def favorite_color_empty() -> None:
    """Test Favorite Color Empty."""
    xs: list[int] = [1, 2, 3]
    assert favorite_color(xs, yay) == [1, 2, 3, 6, 7, 11]


def favorite_color_1() -> None:
    """Test Favorite Color 1."""
    xs: list[int] = []
    yay: list[int] = []
    assert favorite_color(xs, yay) == []


def favorite_color_2() -> None:
    """Test Favorite Color 2."""
    xs: list[int] = [4, 5, 6]
    yay: list[int] = [23, 2, 4]
    assert favorite_color(xs, yay) == [4, 5, 6, 23, 2, 4]


__author__ = "730358517"