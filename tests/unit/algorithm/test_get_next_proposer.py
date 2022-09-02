from python.algorithm.applicant import InitialApplicantStatus
from python.algorithm.get_next_proposer import get_next_proposer
from tests.unit.algorithm.helpers import (
    create_applicant,
    create_rejected_applicant_status,
    create_application,
    create_admitted_applicant_status,
)


def test__get_next_proposer__returns_next_proposer():
    exhausted_applicant = create_applicant(
        {
            "status": create_rejected_applicant_status({"rank": 1}),
            "ranked_applications": [create_application()],
        }
    )
    admitted_applicant = create_applicant(
        {"status": create_admitted_applicant_status()}
    )
    initial_applicant = create_applicant({"status": InitialApplicantStatus()})
    applicants = [exhausted_applicant, admitted_applicant, initial_applicant]

    result = get_next_proposer(applicants=applicants)

    assert result == initial_applicant
