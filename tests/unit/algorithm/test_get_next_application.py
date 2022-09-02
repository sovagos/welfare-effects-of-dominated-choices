from python.algorithm.applicant import InitialApplicantStatus
from python.algorithm.get_next_application import get_next_application
from tests.unit.algorithm.helpers import (
    create_applicant,
    create_application,
    create_rejected_applicant_status,
)


def test__get_next_application__when_applicant_is_in_initial_state__returns_first_application():
    ranked_application = [create_application()]
    applicant = create_applicant(
        {"ranked_applications": ranked_application, "status": InitialApplicantStatus()}
    )

    result = get_next_application(applicant=applicant)

    assert result == ranked_application[0]


def test__get_next_application__when_applicant_is_rejected__returns_next_application():
    ranked_applications = [create_application(), create_application()]
    applicant = create_applicant(
        {
            "ranked_applications": ranked_applications,
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = get_next_application(applicant=applicant)

    assert result == ranked_applications[1]
