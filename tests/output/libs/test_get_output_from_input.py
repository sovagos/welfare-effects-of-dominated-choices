import pytest

from python.output.libs.get_output_from_input import get_output_from_input
from tests.helpers import (
    create_input,
    create_applicant,
    create_contract,
    create_application,
)

use_cases = [
    {
        "input": create_input({"contracts": {}, "applicants": []}),
        "expected": [
            [
                "applicant_id",
                "rank",
                "priority_score",
                "contract_id",
                "capacity",
                "state_funded",
                "program_id",
                "admitted",
            ]
        ],
    },
    {
        "input": create_input(
            {
                "contracts": {
                    "C1": create_contract(
                        {
                            "id": "C1",
                            "program_id": "P1",
                            "state_funded": True,
                            "capacity": 1,
                        }
                    ),
                    "C2": create_contract(
                        {
                            "id": "C2",
                            "program_id": "P2",
                            "state_funded": False,
                            "capacity": 2,
                        }
                    ),
                },
                "applicants": [
                    create_applicant(
                        {
                            "id": "A1",
                            "ranked_applications": [
                                create_application(
                                    {
                                        "contract": "C1",
                                        "priority_score": 1,
                                        "admitted": True,
                                    }
                                ),
                                create_application(
                                    {
                                        "contract": "C2",
                                        "priority_score": 2,
                                        "admitted": False,
                                    }
                                ),
                            ],
                        }
                    ),
                    create_applicant(
                        {
                            "id": "A2",
                            "ranked_applications": [
                                create_application(
                                    {
                                        "contract": "C1",
                                        "priority_score": 3,
                                        "admitted": False,
                                    }
                                )
                            ],
                        }
                    ),
                ],
            }
        ),
        "expected": [
            [
                "applicant_id",
                "rank",
                "priority_score",
                "contract_id",
                "capacity",
                "state_funded",
                "program_id",
                "admitted",
            ],
            ["A1", "1", "1", "C1", "1", "1", "P1", "1"],
            ["A1", "2", "2", "C2", "2", "0", "P2", "0"],
            ["A2", "1", "3", "C1", "1", "1", "P1", "0"],
        ],
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_output_from_matchings(use_case) -> None:
    result = get_output_from_input(input=use_case["input"])

    assert result == use_case["expected"]
