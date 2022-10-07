import pytest

from python.get_contracts.get_contracts import (
    get_contracts,
)
from tests.unit.helpers import (
    create_contract_with_score,
    create_contract,
    create_applicant,
    create_application,
)


use_cases = [
    {
        "contracts": [
            create_contract({"id": "C1", "capacity": 1}),
            create_contract({"id": "C2", "capacity": 1}),
            create_contract({"id": "C3", "capacity": 1}),
        ],
        "applicants": [
            create_applicant(
                {
                    "id": "A1",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 10}),
                        create_application({"contract": "C2", "priority_score": 10}),
                        create_application({"contract": "C3", "priority_score": 11}),
                    ],
                }
            )
        ],
        "expected": [
            create_contract_with_score({"id": "C1", "score": 10}),
            create_contract_with_score({"id": "C2", "score": 0}),
            create_contract_with_score({"id": "C3", "score": 0}),
        ],
    },
    {
        "contracts": [
            create_contract({"id": "C1", "capacity": 1}),
            create_contract({"id": "C2", "capacity": 1}),
        ],
        "applicants": [
            create_applicant(
                {
                    "id": "A1",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 11}),
                        create_application({"contract": "C2", "priority_score": 11}),
                    ],
                },
            ),
            create_applicant(
                {
                    "id": "A2",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 9}),
                    ],
                }
            ),
        ],
        "expected": [
            create_contract_with_score({"id": "C1", "score": 11}),
            create_contract_with_score({"id": "C2", "score": 0}),
        ],
    },
    {
        "contracts": [
            create_contract({"id": "C1", "capacity": 1}),
            create_contract({"id": "C2", "capacity": 1}),
            create_contract({"id": "C3", "capacity": 1}),
        ],
        "applicants": [
            create_applicant(
                {
                    "id": "A1",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 10}),
                        create_application({"contract": "C2", "priority_score": 10}),
                        create_application({"contract": "C3", "priority_score": 10}),
                    ],
                },
            ),
            create_applicant(
                {
                    "id": "A2",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 11}),
                    ],
                }
            ),
            create_applicant(
                {
                    "id": "A3",
                    "ranked_applications": [
                        create_application({"contract": "C2", "priority_score": 11}),
                    ],
                }
            ),
        ],
        "expected": [
            create_contract_with_score({"id": "C1", "score": 11}),
            create_contract_with_score({"id": "C2", "score": 11}),
            create_contract_with_score({"id": "C3", "score": 10}),
        ],
    },
    {
        "contracts": [
            create_contract({"id": "C1", "capacity": 1}),
            create_contract({"id": "C2", "capacity": 1}),
            create_contract({"id": "C3", "capacity": 1}),
        ],
        "applicants": [
            create_applicant(
                {
                    "id": "A1",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 9}),
                    ],
                },
            ),
            create_applicant(
                {
                    "id": "A2",
                    "ranked_applications": [
                        create_application({"contract": "C2", "priority_score": 10}),
                    ],
                }
            ),
            create_applicant(
                {
                    "id": "A3",
                    "ranked_applications": [
                        create_application({"contract": "C3", "priority_score": 11}),
                    ],
                }
            ),
        ],
        "expected": [
            create_contract_with_score({"id": "C1", "score": 9}),
            create_contract_with_score({"id": "C2", "score": 10}),
            create_contract_with_score({"id": "C3", "score": 11}),
        ],
    },
    {
        "contracts": [
            create_contract({"id": "C1", "capacity": 2}),
        ],
        "applicants": [
            create_applicant(
                {
                    "id": "A1",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 9}),
                    ],
                },
            ),
            create_applicant(
                {
                    "id": "A2",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 10}),
                    ],
                }
            ),
            create_applicant(
                {
                    "id": "A3",
                    "ranked_applications": [
                        create_application({"contract": "C1", "priority_score": 11}),
                    ],
                }
            ),
        ],
        "expected": [
            create_contract_with_score({"id": "C1", "score": 10}),
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_contracts(use_case) -> None:
    result = get_contracts(
        contracts=use_case["contracts"], applicants=use_case["applicants"]
    )

    assert result == use_case["expected"]
