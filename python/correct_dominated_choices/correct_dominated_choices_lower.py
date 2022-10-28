from python.types import Input, Contract


def correct_dominated_choices_lower(input: Input) -> Input:
    corrected_applicants = []
    for applicant in input.applicants:
        corrected_applicants.append(applicant)

    return Input(contracts=input.contracts, applicants=corrected_applicants)


def _get_programs(contracts: list[Contract]) -> dict:
    programs: dict = {}
    for contract in contracts:
        program = programs.get(contract.program_id, {})
        program[
            "state_funded" if contract.state_funded else "self_funded"
        ] = contract.id
        programs[contract.program_id] = program
    return programs
