from python.get_applicants.libs.add_admitted_applicant_to_contract import (
    add_admitted_applicant_to_contract,
)
from tests.unit.get_applicants.helpers import create_admitted_applicant, create_contract


def test__add_admitted_applicant_from_contract__add_admitted_applicant() -> None:
    new_admitted_applicant = create_admitted_applicant()
    admitted_applicants = [
        create_admitted_applicant(),
        create_admitted_applicant(),
    ]

    result = add_admitted_applicant_to_contract(
        applicant=new_admitted_applicant,
        contract=create_contract({"admitted_applicants": admitted_applicants}),
    )

    assert result.admitted_applicants == [
        admitted_applicants[0],
        admitted_applicants[1],
        new_admitted_applicant,
    ]
