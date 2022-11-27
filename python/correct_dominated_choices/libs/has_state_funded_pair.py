from python.types import Contract


def has_state_funded_pair(programs: dict, contract: Contract) -> bool:
    return "state_funded" in programs[contract.program_id].keys()
