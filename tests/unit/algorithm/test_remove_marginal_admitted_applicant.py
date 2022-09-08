from python.algorithm.remove_marginal_admitted_applicant import (
    remove_marginal_admitted_applicant,
)
from tests.unit.algorithm.helpers import create_admitted_applicant, create_contract


def test__remove_marginal_admitted_applicant__when_a_single_applicant_is_admitted__returns_contract_with_no_admitted_applicants():
    marginal_admitted_applicant = create_admitted_applicant()
    admitted_applicants = [marginal_admitted_applicant]
    contract = create_contract({"admitted_applicants": admitted_applicants})
    expected_result = create_contract(
        {"id": contract.id, "capacity": contract.capacity, "admitted_applicants": []}
    )

    result = remove_marginal_admitted_applicant(
        contract=contract, marginal_admitted_applicant=marginal_admitted_applicant
    )

    assert result == expected_result


def test__remove_marginal_admitted_applicant__when_multiple_applicants_are_admitted__returns_contract_with_inframarginal_admitted_applicants():
    inframarginal_admitted_applicant = create_admitted_applicant()
    marginal_admitted_applicant = create_admitted_applicant()
    admitted_applicants = [
        inframarginal_admitted_applicant,
        marginal_admitted_applicant,
    ]
    contract = create_contract({"admitted_applicants": admitted_applicants})

    result = remove_marginal_admitted_applicant(
        contract=contract, marginal_admitted_applicant=marginal_admitted_applicant
    )

    assert result.admitted_applicants == [inframarginal_admitted_applicant]
