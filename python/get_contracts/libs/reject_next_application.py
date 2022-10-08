from typing import Any

from python.types import (
    Applicant,
    RejectedApplicantStatus,
    ApplicantStatusType,
)


def reject_next_application(applicant: Any) -> Applicant:
    return Applicant(
        id=applicant.id,
        ranked_applications=applicant.ranked_applications,
        status=RejectedApplicantStatus(rank=1)
        if applicant.status.type == ApplicantStatusType.INIT
        else RejectedApplicantStatus(rank=applicant.status.rank + 1),
    )
