from typing import Any

from python.types import ApplicantStatusType


def is_proposer(applicant: Any) -> bool:
    return (
        applicant.status.type == ApplicantStatusType.REJECTED
        and len(applicant.ranked_applications) > applicant.status.rank
    ) or (applicant.status.type == ApplicantStatusType.INIT)
