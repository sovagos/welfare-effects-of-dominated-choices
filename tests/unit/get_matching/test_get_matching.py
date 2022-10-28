import pytest

from python.get_matching.get_matching import (
    get_matching,
)
from tests.unit.helpers import (
    create_contract,
    create_applicant,
    create_application,
    create_matching,
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
            create_matching({"applicant_id": "A1", "contract_id": "C1", "rank": 1}),
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
            create_matching({"applicant_id": "A1", "contract_id": "C1", "rank": 1}),
            create_matching(
                {"applicant_id": "A2", "contract_id": "Unassigned", "rank": 0}
            ),
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
            create_matching({"applicant_id": "A2", "contract_id": "C1", "rank": 1}),
            create_matching({"applicant_id": "A3", "contract_id": "C2", "rank": 1}),
            create_matching({"applicant_id": "A1", "contract_id": "C3", "rank": 3}),
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
            create_matching({"applicant_id": "A1", "contract_id": "C1", "rank": 1}),
            create_matching({"applicant_id": "A2", "contract_id": "C2", "rank": 1}),
            create_matching({"applicant_id": "A3", "contract_id": "C3", "rank": 1}),
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
            create_matching({"applicant_id": "A2", "contract_id": "C1", "rank": 1}),
            create_matching({"applicant_id": "A3", "contract_id": "C1", "rank": 1}),
            create_matching(
                {"applicant_id": "A1", "contract_id": "Unassigned", "rank": 0}
            ),
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_matching(use_case) -> None:
    result = get_matching(
        contracts=use_case["contracts"], applicants=use_case["applicants"]
    )

    assert result == use_case["expected"]
