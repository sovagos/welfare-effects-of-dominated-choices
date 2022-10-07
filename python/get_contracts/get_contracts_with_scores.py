from functools import reduce

from math import floor

from python.types import ContractWithScore, Contract, AdmittedApplicant


def get_contracts_with_scores(contracts: list[Contract]) -> list[ContractWithScore]:
    return [
        ContractWithScore(
            id=contract.id,
            score=floor(_get_admitted_applicant_with_minimum_point(
                admitted_applicants=contract.admitted_applicants
            ).priority_score),
        )
        for contract in contracts if contract.admitted_applicants
    ]


def _get_admitted_applicant_with_minimum_point(
    admitted_applicants: list[AdmittedApplicant],
) -> AdmittedApplicant:
    return reduce(
        lambda minimum, current: minimum
        if minimum.priority_score < current.priority_score
        else current,
        admitted_applicants,
    )
