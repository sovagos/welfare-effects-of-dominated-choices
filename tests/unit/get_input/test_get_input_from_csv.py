import pytest

from python.get_input.get_input_from_csv import get_input_from_csv
from python.types import InitialApplicantStatus
from tests.unit.helpers import (
    create_input,
    create_contract,
    create_applicant,
    create_application,
)

use_cases = [
    {"csv": [], "expected": create_input({"contracts": [], "applicants": []})},
    {
        "csv": [
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
        "expected": create_input({"contracts": [], "applicants": []}),
    },
    {
        "csv": [
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
            [
                "A1",
                "1",
                "1",
                "C1",
                "1",
                "1",
                "P1",
                "1",
            ],
        ],
        "expected": create_input(
            {
                "contracts": [
                    create_contract(
                        {
                            "id": "C1",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P1",
                            "admitted_applicants": [],
                        }
                    )
                ],
                "applicants": [
                    create_applicant(
                        {
                            "id": "A1",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C1", "priority_score": 1}
                                )
                            ],
                        }
                    )
                ],
            }
        ),
    },
    {
        "csv": [
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
            [
                "A1",
                "1",
                "1",
                "C1",
                "1",
                "1",
                "P1",
                "1",
            ],
            [
                "A2",
                "1",
                "1",
                "C2",
                "1",
                "1",
                "P2",
                "1",
            ],
        ],
        "expected": create_input(
            {
                "contracts": [
                    create_contract(
                        {
                            "id": "C1",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P1",
                            "admitted_applicants": [],
                        }
                    ),
                    create_contract(
                        {
                            "id": "C2",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P2",
                            "admitted_applicants": [],
                        }
                    ),
                ],
                "applicants": [
                    create_applicant(
                        {
                            "id": "A1",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C1", "priority_score": 1}
                                )
                            ],
                        }
                    ),
                    create_applicant(
                        {
                            "id": "A2",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C2", "priority_score": 1}
                                )
                            ],
                        }
                    ),
                ],
            }
        ),
    },
    {
        "csv": [
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
            [
                "A1",
                "2",
                "1",
                "C1",
                "1",
                "1",
                "P1",
                "1",
            ],
            [
                "A1",
                "1",
                "1",
                "C2",
                "1",
                "1",
                "P2",
                "1",
            ],
        ],
        "expected": create_input(
            {
                "contracts": [
                    create_contract(
                        {
                            "id": "C1",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P1",
                            "admitted_applicants": [],
                        }
                    ),
                    create_contract(
                        {
                            "id": "C2",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P2",
                            "admitted_applicants": [],
                        }
                    ),
                ],
                "applicants": [
                    create_applicant(
                        {
                            "id": "A1",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C2", "priority_score": 1}
                                ),
                                create_application(
                                    {"contract": "C1", "priority_score": 1}
                                ),
                            ],
                        }
                    ),
                ],
            }
        ),
    },
    {
        "csv": [
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
            [
                "A1",
                "1",
                "1",
                "C1",
                "1",
                "1",
                "P1",
                "1",
            ],
            [
                "A2",
                "1",
                "1",
                "C1",
                "1",
                "1",
                "P1",
                "1",
            ],
        ],
        "expected": create_input(
            {
                "contracts": [
                    create_contract(
                        {
                            "id": "C1",
                            "capacity": 1,
                            "state_funded": True,
                            "program_id": "P1",
                            "admitted_applicants": [],
                        }
                    ),
                ],
                "applicants": [
                    create_applicant(
                        {
                            "id": "A1",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C1", "priority_score": 1}
                                ),
                            ],
                        }
                    ),
                    create_applicant(
                        {
                            "id": "A2",
                            "status": InitialApplicantStatus(),
                            "ranked_applications": [
                                create_application(
                                    {"contract": "C1", "priority_score": 1}
                                ),
                            ],
                        }
                    ),
                ],
            }
        ),
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__get_input_from_csv(use_case) -> None:
    result = get_input_from_csv(csv=use_case["csv"])

    assert result == use_case["expected"]
