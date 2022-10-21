from python.types import ApplicantStatusType
from python.get_matching.libs.reject_current_application import (
    reject_current_application,
)
from tests.unit.helpers import (
    create_applicant,
    create_application,
    create_rejected_applicant_status,
)


def test__reject_next_application__update_status_to_rejected():
    applicant = create_applicant(
        {
            "ranked_applications": [create_application(), create_application()],
            "status": create_rejected_applicant_status({"rank": 1}),
        }
    )

    result = reject_current_application(applicant=applicant)

    assert result.status.type == ApplicantStatusType.REJECTED
    assert result.status.rank == 1
