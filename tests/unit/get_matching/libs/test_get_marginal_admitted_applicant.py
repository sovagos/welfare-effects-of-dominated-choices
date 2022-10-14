from python.get_matching.libs.get_marginal_admitted_applicant import (
    get_marginal_admitted_applicant,
)
from tests.unit.helpers import (
    get_random_float,
    create_contract,
    create_admitted_applicant,
)


def test__get_marginal_admitted_applicant__returns_with_the_id() -> None:
    priority_score = get_random_float()
    marginal_applicant = create_admitted_applicant({"priority_score": priority_score})

    result = get_marginal_admitted_applicant(
        contract=create_contract(
            {
                "admitted_applicants": [
                    marginal_applicant,
                    create_admitted_applicant({"priority_score": priority_score + 1}),
                    create_admitted_applicant({"priority_score": priority_score + 2}),
                ]
            }
        )
    )

    assert result == marginal_applicant
