from python.get_contracts.libs.remove_admitted_applicant_from_contract import (
    remove_admitted_applicant_from_contract,
)
from tests.unit.helpers import (
    get_random_string,
    create_contract,
    create_admitted_applicant,
)


def test__remove_admitted_applicant_from_contract__removes_admitted_applicant() -> None:
    applicant_id = get_random_string()
    admitted_applicants = [
        create_admitted_applicant(),
        create_admitted_applicant(),
        create_admitted_applicant({"applicant_id": applicant_id}),
        create_admitted_applicant(),
    ]

    result = remove_admitted_applicant_from_contract(
        applicant_id=applicant_id,
        contract=create_contract({"admitted_applicants": admitted_applicants}),
    )

    assert result.admitted_applicants == [
        admitted_applicants[0],
        admitted_applicants[1],
        admitted_applicants[3],
    ]
