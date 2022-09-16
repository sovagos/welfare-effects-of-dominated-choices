from python.libs.find import find
from tests.unit.helpers import get_random_int


def test__find__has_proper_element__returns_the_element() -> None:
    element = get_random_int()

    result = find(
        lambda _: _ == element,
        [get_random_int(), get_random_int(), element, get_random_int()],
    )

    assert result == element


def test__find__has_no_proper_element__returns_none() -> None:
    result = find(lambda _: False, [])

    assert result is None
