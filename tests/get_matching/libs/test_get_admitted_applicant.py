from python.get_matching.libs.get_admitted_applicant import get_admitted_applicant
from tests.helpers import create_applicant, create_applicants, get_random_string


def test__get_admitted_applicant__returns_applicant() -> None:
    applicant_id = get_random_string()
    applicant = create_applicant({"id": applicant_id})
    applicants = create_applicants({"admitted": {applicant_id: applicant}})

    result = get_admitted_applicant(applicants=applicants, applicant_id=applicant_id)

    assert result == applicant
