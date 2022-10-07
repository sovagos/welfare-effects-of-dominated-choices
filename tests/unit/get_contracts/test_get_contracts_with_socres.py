import pytest

from python.get_contracts.get_contracts_with_scores import (
    get_contracts_with_scores,
)
from tests.unit.helpers import (
    create_contract,
    create_contract_with_priority_score_cutoff,
    create_admitted_applicant,
)

use_cases = [
    {
        "input": [],
        "expected": [],
    },
    {
        "input": [
            create_contract(
                {
                    "id": "[X]",
                    "admitted_applicants": [
                        create_admitted_applicant({"priority_score": 1})
                    ],
                }
            )
        ],
        "expected": [
            create_contract_with_priority_score_cutoff(
                {"id": "[X]", "priority_score_cutoff": 1}
            )
        ],
    },
    {
        "input": [
            create_contract(
                {
                    "id": "[X]",
                    "admitted_applicants": [
                        create_admitted_applicant({"priority_score": 1.4})
                    ],
                }
            )
        ],
        "expected": [
            create_contract_with_priority_score_cutoff(
                {"id": "[X]", "priority_score_cutoff": 1}
            )
        ],
    },
    {
        "input": [
            create_contract(
                {
                    "id": "[X]",
                    "admitted_applicants": [
                        create_admitted_applicant({"priority_score": 3}),
                        create_admitted_applicant({"priority_score": 1}),
                    ],
                }
            )
        ],
        "expected": [
            create_contract_with_priority_score_cutoff(
                {"id": "[X]", "priority_score_cutoff": 1}
            )
        ],
    },
    {
        "input": [
            create_contract(
                {
                    "id": "[X]",
                    "admitted_applicants": [],
                }
            )
        ],
        "expected": [
            create_contract_with_priority_score_cutoff(
                {"id": "[X]", "priority_score_cutoff": 0}
            )
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_contracts_with_scores(use_case) -> None:
    result = get_contracts_with_scores(contracts=use_case["input"])

    assert result == use_case["expected"]
