from python.get_applicants.types import Applicant, ApplicantStatusType


def is_proposer(applicant: Applicant) -> bool:
    return (
        applicant.status.type == ApplicantStatusType.REJECTED
        and len(applicant.ranked_applications) > applicant.status.rank
    ) or (applicant.status.type == ApplicantStatusType.INIT)
