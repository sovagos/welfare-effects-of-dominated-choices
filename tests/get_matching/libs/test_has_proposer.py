from python.get_matching.libs.has_proposer import has_proposer
from python.types import InitialApplicantStatus
from tests.helpers import (
    create_applicants,
    create_applicant,
    create_application,
)


def test__has_proposer__proposer_is_empty__returns_false() -> None:
    applicants = create_applicants({"proposer": []})

    result = has_proposer(applicants=applicants)

    assert result is False


def test__has_proposer__proposer_is_not_empty__returns_true() -> None:
    applicants = create_applicants(
        {
            "proposer": [
                create_applicant(
                    {
                        "ranked_applications": [create_application()],
                        "status": InitialApplicantStatus(),
                    }
                )
            ]
        }
    )

    result = has_proposer(applicants=applicants)

    assert result is True
