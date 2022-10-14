from python.types import InitialApplicantStatus
from python.get_matching.libs.has_proposer import has_proposer
from tests.unit.helpers import (
    create_applicant,
    create_application,
    create_admitted_applicant_status,
    create_rejected_applicant_status,
    to_map_by_id,
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
    applicants = to_map_by_id([admitted_applicant, exhausted_applicant])

    result = has_proposer(applicants=applicants)

    assert result is False


def test__has_proposer__has_a_proposer__returns_true():
    applicants = to_map_by_id([create_applicant({"status": InitialApplicantStatus()})])

    result = has_proposer(applicants=applicants)

    assert result is True
