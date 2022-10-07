from python.types import Contract


def is_contract_full(contract: Contract) -> bool:
    return len(contract.admitted_applicants) == contract.capacity
