from python.algorithm.contract import Contract


def has_marginal_admitted_applicant(contract: Contract) -> bool:
    return len(contract.admitted_applicants) == contract.capacity
