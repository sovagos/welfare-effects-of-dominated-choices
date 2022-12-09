from python.get_matching.get_matching_from_applicant import get_matching_from_applicant
from python.get_matching.run_deferred_acceptance import (
    run_deferred_acceptance,
)
from python.types import Applicant, Contracts, Matching


def get_matching(applicants: list[Applicant], contracts: Contracts) -> list[Matching]:
    return [
        get_matching_from_applicant(applicant=applicant)
        for applicant in run_deferred_acceptance(
            contracts=contracts, applicants=applicants
        )
    ]
