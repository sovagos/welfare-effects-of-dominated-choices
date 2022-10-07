from python.types import (
    Applicant,
    AdmittedApplicantStatus,
    ApplicantStatusType,
)


def admit_next_application(applicant: Applicant) -> Applicant:
    return Applicant(
        id=applicant.id,
        ranked_applications=applicant.ranked_applications,
        status=AdmittedApplicantStatus(rank=1)
        if applicant.status.type == ApplicantStatusType.INIT
        else AdmittedApplicantStatus(rank=applicant.status.rank + 1),
    )
