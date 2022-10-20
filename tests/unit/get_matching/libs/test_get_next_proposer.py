from python.get_matching.libs.get_next_proposer import get_next_proposer
from python.types import InitialApplicantStatus
from tests.unit.helpers import (
    create_applicants,
    create_applicant,
    create_application,
)


def test__get_next_proposer__returns_first_proposer() -> None:
    applicant = create_applicant(
        {
            "ranked_applications": [create_application()],
            "status": InitialApplicantStatus(),
        }
    )
    applicants = create_applicants({"proposer": [applicant]})

    result = get_next_proposer(applicants=applicants)

    assert result == applicant
