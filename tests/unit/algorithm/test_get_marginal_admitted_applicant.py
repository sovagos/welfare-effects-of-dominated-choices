from python.algorithm.get_marginal_admitted_applicant import (
    get_marginal_admitted_applicant,
)
from tests.unit.algorithm.helpers import create_admitted_applicant, create_contract


def test__get_marginal_admitted_applicant__returns_applicant_with_lowest_priority_score():
    admitted_applicants = [
        create_admitted_applicant({"priority_score": 0}),
        create_admitted_applicant({"priority_score": 1}),
    ]
    contract = create_contract({"admitted_applicants": admitted_applicants})

    result = get_marginal_admitted_applicant(contract=contract)

    assert result == admitted_applicants[0]
