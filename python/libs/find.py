from typing import Callable, TypeVar, Any

T = TypeVar("T")


def find(function: Callable[[T], bool], sequence: list[T]) -> Any:
    for element in sequence:
        if function(element):
            return element
    return None
