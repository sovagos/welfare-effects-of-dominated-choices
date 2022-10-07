from python.types import Contract


def remove_admitted_applicant_from_contract(
    applicant_id: str, contract: Contract
) -> Contract:
    return Contract(
        id=contract.id,
        capacity=contract.capacity,
        admitted_applicants=[
            _ for _ in contract.admitted_applicants if _.applicant_id != applicant_id
        ],
    )
