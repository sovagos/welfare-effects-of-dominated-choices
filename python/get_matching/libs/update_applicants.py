from typing import Any

from python.get_matching.libs.is_proposer import is_proposer
from python.types import Applicant, Applicants, ApplicantStatusType


def update_applicants(applicants: Applicants, applicant: Applicant) -> Applicants:
    if is_proposer(applicant=applicant):
        if is_in_proposer(applicants=applicants, applicant=applicant):
            return Applicants(
                proposer=[applicant, *applicants.proposer[1:]],
                admitted=applicants.admitted,
                exhausted=applicants.exhausted,
            )
        return Applicants(
            proposer=[*applicants.proposer, applicant],
            admitted=get_admitted_without_applicant(
                admitted=applicants.admitted, applicant=applicant
            ),
            exhausted=applicants.exhausted,
        )
    if is_exhausted(applicant=applicant):
        if is_in_proposer(applicants=applicants, applicant=applicant):
            return Applicants(
                proposer=applicants.proposer[1:],
                admitted=applicants.admitted,
                exhausted=[*applicants.exhausted, applicant],
            )
        return Applicants(
            proposer=applicants.proposer,
            admitted=get_admitted_without_applicant(
                admitted=applicants.admitted, applicant=applicant
            ),
            exhausted=[*applicants.exhausted, applicant],
        )
    applicants.admitted[applicant.id] = applicant
    if is_in_proposer(applicants=applicants, applicant=applicant):
        return Applicants(
            proposer=applicants.proposer[1:],
            admitted=applicants.admitted,
            exhausted=applicants.exhausted,
        )
    return Applicants(
        proposer=applicants.proposer,
        admitted=applicants.admitted,
        exhausted=applicants.exhausted,
    )


def is_in_proposer(applicants: Applicants, applicant: Applicant) -> bool:
    return len(applicants.proposer) > 0 and applicants.proposer[0].id == applicant.id


def is_exhausted(applicant: Any) -> bool:
    return (
        applicant.status.type == ApplicantStatusType.REJECTED
        and len(applicant.ranked_applications) == applicant.status.rank
    )


def get_admitted_without_applicant(
    admitted: dict[str, Applicant], applicant: Applicant
) -> dict[str, Applicant]:
    admitted.pop(applicant.id, None)
    return admitted
