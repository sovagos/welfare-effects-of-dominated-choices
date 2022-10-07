from python.types import InitialApplicantStatus
from python.get_contracts_with_admitted_applicants.libs.is_proposer import is_proposer
from tests.unit.helpers import (
    create_applicant,
    create_application,
    create_admitted_applicant_status,
    create_rejected_applicant_status,
)


def test__is_proposer__when_applicant_is_in_initial_status__returns_true():
    applicant = create_applicant({"status": InitialApplicantStatus()})

    result = is_proposer(applicant=applicant)

    assert result is True


def test__is_proposer__when_applicant_is_admitted__returns_false():
    applicant = create_applicant({"status": create_admitted_applicant_status()})

    result = is_proposer(applicant=applicant)

    assert result is False


def test__is_proposer__when_applicant_is_rejected_but_ranking_is_not_exhausted__returns_true():
    applicant = create_applicant(
        {
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = is_proposer(applicant=applicant)

    assert result is True
