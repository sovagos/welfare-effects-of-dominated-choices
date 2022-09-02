from python.algorithm.has_marginal_admitted_applicant import (
    has_marginal_admitted_applicant,
)
from tests.unit.algorithm.helpers import create_admitted_applicant, create_contract


def test__has_marginal_admitted_applicant__when_less_admitted_applicants_than_capacity__returns_false():
    admitted_applicants = [create_admitted_applicant()]
    contract = create_contract(
        {"capacity": 2, "admitted_applicants": admitted_applicants}
    )

    result = has_marginal_admitted_applicant(contract=contract)

    assert result is False


def test__has_marginal_admitted_applicant__when_same_admitted_applicants_as_capacity__returns_true():
    admitted_applicants = [create_admitted_applicant()]
    contract = create_contract(
        {"capacity": 1, "admitted_applicants": admitted_applicants}
    )

    result = has_marginal_admitted_applicant(contract=contract)

    assert result is True
