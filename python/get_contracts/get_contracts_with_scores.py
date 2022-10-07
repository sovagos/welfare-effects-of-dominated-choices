from functools import reduce

from math import floor

from python.types import ContractWithPriorityScoreCutoff, Contract, AdmittedApplicant


def get_contracts_with_scores(
    contracts: list[Contract],
) -> list[ContractWithPriorityScoreCutoff]:
    return [
        ContractWithPriorityScoreCutoff(
            id=contract.id,
            priority_score_cutoff=_get_score(
                admitted_applicants=contract.admitted_applicants
            ),
        )
        for contract in contracts
    ]


def _get_score(admitted_applicants: list[AdmittedApplicant]) -> int:
    if not admitted_applicants:
        return 0
    return floor(
        _get_admitted_applicant_with_minimum_point(
            admitted_applicants=admitted_applicants
        ).priority_score
    )


def _get_admitted_applicant_with_minimum_point(
    admitted_applicants: list[AdmittedApplicant],
) -> AdmittedApplicant:
    return reduce(
        lambda minimum, current: minimum
        if minimum.priority_score < current.priority_score
        else current,
        admitted_applicants,
    )
