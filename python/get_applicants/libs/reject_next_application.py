from python.get_applicants.types import (
    Applicant,
    RejectedApplicantStatus,
    ApplicantStatusType,
)


def reject_next_application(applicant: Applicant) -> Applicant:
    return Applicant(
        id=applicant.id,
        ranked_applications=applicant.ranked_applications,
        status=RejectedApplicantStatus(rank=1)
        if applicant.status.type == ApplicantStatusType.INIT
        else RejectedApplicantStatus(rank=applicant.status.rank + 1),
    )
