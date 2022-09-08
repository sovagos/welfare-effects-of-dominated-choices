from python.algorithm.contract import Contract


def update_contracts_with_proposed_contract(
    contracts: list[Contract], proposed_contract: Contract
) -> list[Contract]:
    updated_contracts = []
    for contract in contracts:
        if contract.id == proposed_contract.id:
            updated_contracts.extend([proposed_contract])
        else:
            updated_contracts.extend([contract])
    return updated_contracts
