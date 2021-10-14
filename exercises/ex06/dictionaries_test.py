"""Unit tests for dictionary functions."""


from exercises.ex06.dictionaries import invert, favorite_color, count 


def test_invert_1() -> None:
    """Test Invert."""
    xs: dict[str, str] = {'sarah': 'jordan', 'michael': 'jordan'}
    assert invert(xs) == KeyError


def test_invert_2() -> None:
    """Test Invert 1."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_3() -> None:
    """Test Invert 2."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_favorite_color() -> None:
    """Favorite Color."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Sam": "yellow"}
    assert favorite_color(xs) == 'yellow'


def test_favorite_color_1() -> None:
    """Favorite Color 1."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "yellow", "Kris": "yellow"}
    assert favorite_color(xs) == 'yellow'


def test_favorite_color_2() -> None:
    """Favorite Color 2."""
    xs: dict[str, str] = {"Marc": "orange", "Ezri": "orange", "Kris": "blue"}
    assert favorite_color(xs) == 'orange'


def test_count_1() -> None:
    """Count Test 1."""
    xs: list[str] = ['sarah', 'sam', 'sarah']
    assert count(xs) == {'sarah': 2, 'sam': 1}


def test_count_2() -> None:
    """Count Test 2."""
    xs: list[str] = ['jackson', 'sam', 'sarah']
    assert count(xs) == {'jackson': 1, 'sam': 1, 'sarah': 1}


def test_count_3() -> None:
    """Count Test 3."""
    xs: list[str] = ['sam', 'sarah', 'sam']
    assert count(xs) == {'sam': 2, 'sarah': 1}


__author__ = "730358517"