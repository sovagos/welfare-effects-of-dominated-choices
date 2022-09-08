from python.algorithm.contract import Contract, AdmittedApplicant


def remove_marginal_admitted_applicant(
    contract: Contract, marginal_admitted_applicant: AdmittedApplicant
) -> Contract:
    return Contract(
        id=contract.id,
        capacity=contract.capacity,
        admitted_applicants=[
            admitted_applicant
            for admitted_applicant in contract.admitted_applicants
            if admitted_applicant != marginal_admitted_applicant
        ],
    )
