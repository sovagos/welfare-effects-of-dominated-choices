from typing import Any

from python.types import Matching, ApplicantStatusType


def get_matching_from_applicant(applicant: Any) -> Matching:
    if applicant.status.type == ApplicantStatusType.REJECTED:
        return Matching(
            applicant_id=applicant.id,
            contract_id="Unassigned",
            rank=0,
        )
    return Matching(
        applicant_id=applicant.id,
        contract_id=applicant.ranked_applications[applicant.status.rank - 1].contract,
        rank=applicant.status.rank,
    )
