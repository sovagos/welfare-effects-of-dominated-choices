from python.types import Contract, AdmittedApplicant


def add_admitted_applicant_to_contract(
    applicant: AdmittedApplicant, contract: Contract
) -> Contract:
    return Contract(
        id=contract.id,
        capacity=contract.capacity,
        admitted_applicants=[*contract.admitted_applicants, applicant],
    )
