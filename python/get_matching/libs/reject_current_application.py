from typing import Any

from python.types import RejectedApplicantStatus, Applicant


def reject_current_application(applicant: Any) -> Applicant:
    return Applicant(
        id=applicant.id,
        ranked_applications=applicant.ranked_applications,
        status=RejectedApplicantStatus(rank=applicant.status.rank),
    )
