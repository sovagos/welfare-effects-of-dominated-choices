from python.types import ApplicantStatusType, InitialApplicantStatus
from python.get_contracts.libs.admint_next_application import (
    admit_next_application,
)
from tests.unit.helpers import (
    create_applicant,
    create_application,
    create_rejected_applicant_status,
)


def test__admit_next_application__when_status_is_initial__update_admitted_applicant_status_to_rank_of_one():
    applicant = create_applicant(
        {
            "status": InitialApplicantStatus(),
            "ranked_applications": [create_application()],
        }
    )

    result = admit_next_application(applicant=applicant)

    assert result.status.type == ApplicantStatusType.ADMITTED
    assert result.status.rank == 1


def test__admit_next_application__when_status_is_rejected__update_status_to_next_contract():
    applicant = create_applicant(
        {
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = admit_next_application(applicant=applicant)

    assert result.status.type == ApplicantStatusType.ADMITTED
    assert result.status.rank == 2
