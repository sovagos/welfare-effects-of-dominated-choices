from typing import Any

from python.types import Applicant, Application, ApplicantStatusType


def get_next_application(applicant: Any) -> Application:
    if applicant.status.type == ApplicantStatusType.REJECTED:
        return applicant.ranked_applications[applicant.status.rank]
    return applicant.ranked_applications[0]
