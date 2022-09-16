from functools import reduce

from python.get_applicants.types import Contract, AdmittedApplicant


def get_marginal_admitted_applicant(contract: Contract) -> AdmittedApplicant:
    return reduce(
        lambda minimum, current: current
        if minimum.priority_score > current.priority_score
        else minimum,
        contract.admitted_applicants,
    )
