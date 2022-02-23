"""Utils test file for exercise 05."""

__author__ = "730325581"

from utils import only_evens, sub, concat


def test_only_evens_edgecase() -> None:
    """Tests the scenerio of an empty list edge case."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_usecase1() -> None:
    """Tests both even and odd numbers in a list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_list) == [2, 4]


def test_only_evens_usecase2() -> None:
    """Tests only odd numbers."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_sub_edgecase() -> None:
    """Tests the scenerio where the start index is greater than the length of the list."""
    assert sub([1, 2, 3], 5, 2) == []


def test_sub_usecase1() -> None:
    """Tests a typical use scenerio of the sub function."""
    assert sub([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]


def test_sub_usecase2() -> None:
    """Tests another typical use scenerio of the sub function."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8], 1, 4) == [2, 3, 4]  


def test_concat_edgecase() -> None:
    """Tests the scenerio where one list is empty."""
    assert concat([1, 2, 3], []) == [1, 2, 3]


def test_concat_usecase1() -> None:
    """Tests a typical scenerio of the concat function."""
    assert concat([233, 347, 110], [400, 410, 420, 470]) == [233, 347, 110, 400, 410, 420, 470]


def test_concat_usecase2() -> None:
    """Tests another typical scenerio of the concat function."""
    assert concat([1], [99, 98, 97, 96]) == [1, 99, 98, 97, 96]