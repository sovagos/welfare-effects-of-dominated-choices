import pytest

from python.correct_dominated_choices.correct_dominated_choices_lower import (
    correct_dominated_choices_lower,
)
from python.types import Input
from tests.correct_dominated_choices.helper import (
    create_applicant_with_ranked_applications,
)
from tests.helpers import create_contract, create_applicant, create_application

contracts = {
    "Contract_state_funded_with_pair_1": create_contract(
        {
            "id": "Contract_state_funded_with_pair_1",
            "program_id": "Program_with_pair_1",
            "state_funded": True,
        }
    ),
    "Contract_self_funded_with_pair_1": create_contract(
        {
            "id": "Contract_self_funded_with_pair_1",
            "program_id": "Program_with_pair_1",
            "state_funded": False,
        }
    ),
    "Contract_state_funded_with_pair_2": create_contract(
        {
            "id": "Contract_state_funded_with_pair_2",
            "program_id": "Program_with_pair_2",
            "state_funded": True,
        }
    ),
    "Contract_self_funded_with_pair_2": create_contract(
        {
            "id": "Contract_self_funded_with_pair_2",
            "program_id": "Program_with_pair_2",
            "state_funded": False,
        }
    ),
    "Contract_state_funded_with_no_pair": create_contract(
        {
            "id": "Contract_state_funded_with_no_pair",
            "program_id": "Program_state_funded_no_pair",
            "state_funded": True,
        }
    ),
    "Contract_self_funded_with_no_pair": create_contract(
        {
            "id": "Contract_self_funded_with_no_pair",
            "program_id": "Program_self_funded_no_pair",
            "state_funded": False,
        }
    ),
}

use_cases = [
    {
        "description": "No dominated choice",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
            ]
        ),
    },
    {
        "description": "Dominated dropping and the program has a state-funded version",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
            ]
        ),
    },
    {
        "description": "Dominated dropping and the program has no state-funded version",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_self_funded_with_no_pair", "admitted": False}
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_self_funded_with_no_pair", "admitted": False}
            ]
        ),
    },
    {
        "description": "Dominated droppings and correct in right order",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_2", "admitted": False},
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_2", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_2", "admitted": False},
            ]
        ),
    },
    {
        "description": "Dominated flipping",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_2", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_2", "admitted": False},
            ]
        ),
    },
    {
        "description": "Dominated flipping (keep the priority score of the state funded)",
        "applicant": create_applicant(
            {
                "id": "x",
                "ranked_applications": [
                    create_application(
                        {
                            "contract": "Contract_self_funded_with_pair_1",
                            "priority_score": 0,
                        }
                    ),
                    create_application(
                        {
                            "contract": "Contract_state_funded_with_pair_1",
                            "priority_score": 1,
                        }
                    ),
                ],
            }
        ),
        "expected": create_applicant(
            {
                "id": "x",
                "ranked_applications": [
                    create_application(
                        {
                            "contract": "Contract_state_funded_with_pair_1",
                            "priority_score": 1,
                        }
                    ),
                    create_application(
                        {
                            "contract": "Contract_self_funded_with_pair_1",
                            "priority_score": 0,
                        }
                    ),
                ],
            }
        ),
    },
    {
        "description": "Dominated flippings and correct in right order",
        "applicant": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_2", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_2", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            pairs=[
                {"contract_id": "Contract_state_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_1", "admitted": False},
                {"contract_id": "Contract_state_funded_with_pair_2", "admitted": False},
                {"contract_id": "Contract_self_funded_with_pair_2", "admitted": False},
                {
                    "contract_id": "Contract_state_funded_with_no_pair",
                    "admitted": False,
                },
            ]
        ),
    },
]


@pytest.mark.parametrize("use_case", use_cases)
def test__correct_dominated_choices_lower(use_case) -> None:
    result = correct_dominated_choices_lower(
        input=Input(contracts=contracts, applicants=[use_case["applicant"]])
    )

    assert result == Input(contracts=contracts, applicants=[use_case["expected"]])
