from python.algorithm.update_contracts_with_proposed_contract import (
    update_contracts_with_proposed_contract,
)
from tests.unit.algorithm.helpers import create_contract, create_admitted_applicant


def test__update_contracts_with_proposed_contract__updates_contracts():
    contract_1 = create_contract({"admitted_applicants": [create_admitted_applicant()]})
    contract_2 = create_contract({"admitted_applicants": [create_admitted_applicant()]})
    contract_3 = create_contract({"admitted_applicants": [create_admitted_applicant()]})
    contracts = [contract_1, contract_2, contract_3]
    proposed_contract = create_contract(
        {"id": contract_2.id, "admitted_applicants": [create_admitted_applicant()]}
    )

    result = update_contracts_with_proposed_contract(
        contracts=contracts, proposed_contract=proposed_contract
    )

    assert result == [contract_1, proposed_contract, contract_3]
