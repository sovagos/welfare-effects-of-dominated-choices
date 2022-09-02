from python.algorithm.applicant import InitialApplicantStatus
from python.algorithm.has_proposer import has_proposer
from tests.unit.algorithm.helpers import (
    create_applicant,
    create_admitted_applicant_status,
    create_rejected_applicant_status,
    create_application,
)


def test__has_proposer__no_proposer__returns_false():
    admitted_applicant = create_applicant(
        {"status": create_admitted_applicant_status()}
    )
    exhausted_applicant = create_applicant(
        {
            "status": create_rejected_applicant_status({"rank": 1}),
            "ranked_applications": [create_application()],
        }
    )
    applicants = [admitted_applicant, exhausted_applicant]

    result = has_proposer(applicants=applicants)

    assert result is False


def test__has_proposer__has_a_proposer__returns_true():
    applicants = [create_applicant({"status": InitialApplicantStatus()})]

    result = has_proposer(applicants=applicants)

    assert result is True
