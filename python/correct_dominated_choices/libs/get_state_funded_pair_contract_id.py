from python.types import Contract


def get_state_funded_pair_contract_id(programs: dict, contract: Contract) -> str:
    return programs[contract.program_id]["state_funded"]
