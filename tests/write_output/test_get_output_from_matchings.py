import pytest

from python.output.get_output_from_matchings import (
    get_output_from_matchings,
)
from tests.helpers import create_matching

use_cases = [
    {"input": [], "expected": [["applicant_id", "contract_id", "rank"]]},
    {
        "input": [
            create_matching({"applicant_id": "A1", "contract_id": "C1", "rank": 1})
        ],
        "expected": [
            ["applicant_id", "contract_id", "rank"],
            ["A1", "C1", "1"],
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_output_from_matchings(use_case) -> None:
    result = get_output_from_matchings(matchings=use_case["input"])

    assert result == use_case["expected"]
