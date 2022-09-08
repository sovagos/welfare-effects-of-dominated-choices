from python.algorithm.applicant import Applicant, RejectedApplicantStatus
from python.algorithm.contract import AdmittedApplicant


def update_marginal_admitted_applicant(
    applicants: list[Applicant], marginal_admitted_applicant: AdmittedApplicant
) -> Applicant:
    for applicant in applicants:
        if applicant.id == marginal_admitted_applicant.applicant_id:
            updated_marginal_admitted_applicant = Applicant(
                id=applicant.id,
                ranked_applications=applicant.ranked_applications,
                status=RejectedApplicantStatus(rank=applicant.status.rank),
            )
    return updated_marginal_admitted_applicant
