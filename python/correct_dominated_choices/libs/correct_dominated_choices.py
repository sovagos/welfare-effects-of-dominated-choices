from typing import Callable

from python.types import Applicant, Contract, Input, Contracts

GetCorrectedApplicant = Callable[[dict, dict[str, Contract], Applicant], Applicant]


def correct_dominated_choices(
    input: Input, get_corrected_applicant: GetCorrectedApplicant
) -> Input:
    programs = _get_programs(contracts=input.contracts)
    return Input(
        contracts=input.contracts,
        applicants=[
            get_corrected_applicant(
                programs,
                input.contracts,
                applicant,
            )
            for applicant in input.applicants
        ],
    )


def _get_programs(contracts: Contracts) -> dict:
    programs: dict = {}
    for contract in contracts.values():
        program = programs.get(contract.program_id, {})
        program[
            "state_funded" if contract.state_funded else "self_funded"
        ] = contract.id
        programs[contract.program_id] = program
    return programs


def _to_map_by_id(elements: list[Contract]) -> dict[str, Contract]:
    return {element.id: element for element in elements}
