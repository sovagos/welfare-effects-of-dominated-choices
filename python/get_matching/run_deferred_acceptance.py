from python.get_matching.run_deferred_acceptance_rec import (
    run_deferred_acceptance_rec,
)
from python.types import Applicant, Applicants, Contracts


def run_deferred_acceptance(
    applicants: list[Applicant], contracts: Contracts
) -> list[Applicant]:
    result: Applicants = run_deferred_acceptance_rec(
        Applicants(proposer=applicants, admitted={}, exhausted=[]),
        contracts,
    )
    return [*result.admitted.values(), *result.exhausted]
