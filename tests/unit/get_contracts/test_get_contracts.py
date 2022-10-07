import pytest

from python.get_contracts.get_contracts import (
    get_contracts,
)


use_cases = [
    {
        "contracts": [],
        "applicants": [],
        "expected": [],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_contracts(use_case) -> None:
    result = get_contracts(
        contracts=use_case["contracts"], applicants=use_case["applicants"]
    )

    assert result == use_case["expected"]
