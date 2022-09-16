from typing import Callable, TypeVar

T = TypeVar("T")


def find(function: Callable[[T], bool], sequence: list[T]) -> T:
    for element in sequence:
        if function(element):
            return element
    return None
