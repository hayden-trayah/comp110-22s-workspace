"""Dictionary functions tests - Hayden Trayah."""

__author__ = "730325581"

import pytest
from dictionary import invert, count, favorite_color


def test_invert_edgecase() -> None:
    """Edge case involving duplicate values used in the argument."""
    test_dict: dict[str, str] = {"hi": "bye", "hey": "bye"}
    with pytest.raises(KeyError):
        invert(test_dict)


def test_invert_usecase1() -> None:
    """Typical use case of the invert function (two key-value pairs)."""
    test_dict: dict[str, str] = {"yo": "what's good?", "howdy": "sup bro"}
    assert invert(test_dict) == {"what's good?": "yo", "sup bro": "howdy"}


def test_invert_usecase2() -> None:
    """Typical use case of the invert function (three key-value pairs)."""
    test_dict: dict[str, str] = {"ECON": "420", "MATH": "233", "COMP": "110"}
    assert invert(test_dict) == {"420": "ECON", "233": "MATH", "110": "COMP"}


def test_count_edgecase() -> None:
    """Tests the edge case of an empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_usecase1() -> None:
    """Typical use case of the count function (counting five list values)."""
    test_list: list[str] = ["ECON", "COMP", "MATH", "COMM", "ECON"]
    assert count(test_list) == {"ECON": 2, "COMP": 1, "MATH": 1, "COMM": 1}


def test_count_usecase2() -> None:
    """Typical use case of the count function (counting six list values)."""
    test_list: list[str] = ["Hi", "Hi", "Hi", "Hey", "Hey", "WHAT"]
    assert count(test_list) == {"Hi": 3, "Hey": 2, "WHAT": 1}


def test_favorite_color_edgecase() -> None:
    """Edge case confirming that the first of the tied favorite colors in the argument dictionary is returned."""
    test_dict: dict[str, str] = {"Hayden": "blue", "Joey": "blue", "Cade": "yellow", "B": "yellow"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_usecase1() -> None:
    """Typical use case of the favorite colors function (four key-value pairs)."""
    test_dict: dict[str, str] = {"Carolina": "blue", "State": "red", "Duke": "blue", "Harvard": "Crimson"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_usecase2() -> None:
    """Typical use case of the favorite colors function (five key-value pairs)."""
    test_dict: dict[str, str] = {"Leaves": "green", "Ocean": "blue", "Fire": "red", "Starbucks Straw": "green"}
    assert favorite_color(test_dict) == "green"