import pytest

from python.write_output.get_output_from_contracts_with_priority_score_cutoffs import (
    get_output_from_contracts_with_priority_score_cutoffs,
)
from tests.unit.helpers import create_contract_with_priority_score_cutoff

use_cases = [
    {"input": [], "expected": [["contract_id", "priority_score_cutoff"]]},
    {
        "input": [
            create_contract_with_priority_score_cutoff(
                {"id": "C1", "priority_score_cutoff": 1}
            )
        ],
        "expected": [
            ["contract_id", "priority_score_cutoff"],
            ["C1", "1"],
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_output_from_contracts_with_priority_score_cutoffs(use_case) -> None:
    result = get_output_from_contracts_with_priority_score_cutoffs(
        contracts_with_priority_score_cutoffs=use_case["input"]
    )

    assert result == use_case["expected"]
