"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count 


def invert_first_test() -> None:
    """Test Invert Empty."""
    xs: dict[str, str] = {'sarah': 'jordan', 'michael': 'jordan'}
    assert invert(xs) == KeyError


def invert_2() -> None:
    """Test Invert 1."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def invert_3() -> None:
    """Test Invert 1."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def favorite_color_test() -> None:
    """Favorite Color."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == 'blue'


def favorite_color_1() -> None:
    """Favorite Color 1."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "blue"}
    assert favorite_color(xs) == 'yellow'


def favorite_color_2() -> None:
    """Favorite Color 2."""
    xs: dict[str, str] = {"Marc": "orange", "Ezri": "orange", "Kris": "blue"}
    assert favorite_color(xs) == 'orange'


def count_test() -> None:
    """Test Favorite Color."""
    xs: list[str] = ['sarah', 'sam', 'sarah']
    assert count(xs) == ["sarah: 2, sam: 1"]


def Count_test_1() -> None:
    """Test Favorite Color 1."""
    xs: list[str] = ['jackson', 'sam', 'sarah']
    assert count(xs) == ["jackson: 1, sam: 1, sarah: 1"]


def Count_test_2() -> None:
    """Test Favorite Color 2."""
    xs: list[str] = ['sam', 'sarah', 'sam']
    assert count(xs) == ["sam: 2, sarah: 1"]


__author__ = "730358517"