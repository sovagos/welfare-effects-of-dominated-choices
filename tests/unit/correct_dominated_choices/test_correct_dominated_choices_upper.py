import pytest

from python.correct_dominated_choices.correct_dominated_choices_upper import (
    correct_dominated_choices_upper,
)
from python.types import Input
from tests.unit.correct_dominated_choices.helper import (
    create_applicant_with_ranked_applications,
)
from tests.unit.helpers import create_contract, create_applicant, create_application

contracts = [
    create_contract(
        {
            "id": "Contract_state_funded_with_pair_1",
            "program_id": "Program_with_pair_1",
            "state_funded": True,
        }
    ),
    create_contract(
        {
            "id": "Contract_self_funded_with_pair_1",
            "program_id": "Program_with_pair_1",
            "state_funded": False,
        }
    ),
    create_contract(
        {
            "id": "Contract_state_funded_with_pair_2",
            "program_id": "Program_with_pair_2",
            "state_funded": True,
        }
    ),
    create_contract(
        {
            "id": "Contract_self_funded_with_pair_2",
            "program_id": "Program_with_pair_2",
            "state_funded": False,
        }
    ),
    create_contract(
        {
            "id": "Contract_state_funded_with_no_pair",
            "program_id": "Program_state_funded_no_pair",
            "state_funded": True,
        }
    ),
    create_contract(
        {
            "id": "Contract_self_funded_with_no_pair",
            "program_id": "Program_self_funded_no_pair",
            "state_funded": False,
        }
    ),
]

use_cases = [
    {
        "description": "No dominated choice",
        "applicant": create_applicant_with_ranked_applications(
            contract_ids=[
                "Contract_state_funded_with_pair_1",
                "Contract_self_funded_with_pair_1",
            ]
        ),
        "expected": create_applicant_with_ranked_applications(
            contract_ids=[
                "Contract_state_funded_with_pair_1",
                "Contract_self_funded_with_pair_1",
            ]
        ),
    },
    {
        "description": "Dominated dropping and the program has a state-funded version",
        "applicant": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                ]
            }
        ),
        "expected": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                ]
            }
        ),
    },
    {
        "description": "Dominated dropping and the program has no state-funded version",
        "applicant": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_self_funded_with_no_pair"}
                    ),
                ]
            }
        ),
        "expected": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_self_funded_with_no_pair"}
                    ),
                ]
            }
        ),
    },
    {
        "description": "Dominated droppings and correct in right order",
        "applicant": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_2"}
                    ),
                ]
            }
        ),
        "expected": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_2"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_2"}
                    ),
                ]
            }
        ),
    },
    {
        "description": "Dominated flipping",
        "applicant": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_2"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                ]
            }
        ),
        "expected": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_2"}
                    ),
                ]
            }
        ),
    },
    {
        "description": "Dominated flippings and correct in right order",
        "applicant": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_2"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_2"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                ]
            }
        ),
        "expected": create_applicant(
            {
                "ranked_applications": [
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_pair_2"}
                    ),
                    create_application(
                        {"contract": "Contract_state_funded_with_no_pair"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_1"}
                    ),
                    create_application(
                        {"contract": "Contract_self_funded_with_pair_2"}
                    ),
                ]
            }
        ),
    },
]


@pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize("use_case", use_cases)
def test__correct_dominated_choices_upper(use_case) -> None:
    result = correct_dominated_choices_upper(
        input=Input(contracts=contracts, applicants=[use_case["applicant"]])
    )

    assert result == Input(contracts=contracts, applicants=[use_case["expected"]])