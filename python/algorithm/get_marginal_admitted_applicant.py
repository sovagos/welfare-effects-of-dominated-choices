from functools import reduce

from python.algorithm.contract import AdmittedApplicant, Contract


def get_marginal_admitted_applicant(contract: Contract) -> AdmittedApplicant:
    return reduce(
        lambda marginal_applicant, applicant: applicant
        if applicant.priority_score < marginal_applicant.priority_score
        else marginal_applicant,
        contract.admitted_applicants,
    )
