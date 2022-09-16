from python.get_applicants.types import Applicant, Application, ApplicantStatusType


def get_next_application(applicant: Applicant) -> Application:
    if applicant.status.type == ApplicantStatusType.REJECTED:
        return applicant.ranked_applications[applicant.status.rank]
    return applicant.ranked_applications[0]
