from functools import reduce

from math import floor

from python.types import ContractWithScore, Contract, AdmittedApplicant


def get_contracts_with_scores(contracts: list[Contract]) -> list[ContractWithScore]:
    return [
        ContractWithScore(
            id=contract.id,
            score=_get_score(admitted_applicants=contract.admitted_applicants),
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
