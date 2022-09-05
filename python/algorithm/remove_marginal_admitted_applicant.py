from python.algorithm.contract import Contract, AdmittedApplicant


def remove_marginal_admitted_applicant(
    contract: Contract, marginal_admitted_applicant: AdmittedApplicant
) -> Contract:
    contract.admitted_applicants.remove(marginal_admitted_applicant)
    return contract
