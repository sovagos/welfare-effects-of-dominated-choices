from dataclasses import dataclass
from functools import reduce

from python.types import Input, Contract, Applicant, InitialApplicantStatus, Application


@dataclass
class ParsedRow:
    applicant_id: str
    rank: int
    priority_score: float
    contract_id: str
    capacity: int
    state_funded: bool
    program_id: str


def get_input_from_csv(csv: list[list[str]]) -> Input:
    result: dict = reduce(
        _accumulator, _tail(csv=csv), {"applicants": {}, "contracts": {}}
    )
    return Input(
        applicants=[*result["applicants"].values()],
        contracts=[*result["contracts"].values()],
    )


def _tail(csv: list[list[str]]) -> list[list[str]]:
    if not csv:
        return []
    return csv[1:]


def _accumulator(accumulated: dict, row: list[str]) -> dict:
    parsed_row = _get_parsed_row(row=row)
    return {
        "contracts": _get_contracts(
            accumulated_contracts=accumulated["contracts"], parsed_row=parsed_row
        ),
        "applicants": _get_applicants(
            accumulated_applicants=accumulated["applicants"], parsed_row=parsed_row
        ),
    }


def _get_parsed_row(row: list[str]) -> ParsedRow:
    return ParsedRow(
        applicant_id=row[0],
        rank=int(row[1]),
        priority_score=float(row[2]),
        contract_id=row[3],
        capacity=int(row[4]),
        state_funded=row[5] == "1",
        program_id=row[6],
    )


def _get_contracts(
    accumulated_contracts: dict[str, Contract], parsed_row: ParsedRow
) -> dict[str, Contract]:
    if parsed_row.contract_id in accumulated_contracts:
        return accumulated_contracts
    return {
        **accumulated_contracts,
        parsed_row.contract_id: Contract(
            id=parsed_row.contract_id,
            capacity=parsed_row.capacity,
            program_id=parsed_row.program_id,
            state_funded=parsed_row.state_funded,
            admitted_applicants=[],
        ),
    }


def _get_applicants(
    accumulated_applicants: dict[str, Applicant], parsed_row: ParsedRow
) -> dict[str, Applicant]:
    ranked_applications = _get_ranked_applications_with_new_application(
        ranked_applications=[]
        if parsed_row.applicant_id not in accumulated_applicants
        else accumulated_applicants[parsed_row.applicant_id].ranked_applications,
        parsed_row=parsed_row,
    )
    return {
        **accumulated_applicants,
        parsed_row.applicant_id: Applicant(
            id=parsed_row.applicant_id,
            ranked_applications=ranked_applications,
            status=InitialApplicantStatus(),
        ),
    }


def _get_ranked_applications_with_new_application(
    ranked_applications: list[Application], parsed_row: ParsedRow
) -> list[Application]:
    ranked_applications = [*ranked_applications]
    ranked_applications.insert(
        parsed_row.rank - 1,
        Application(
            contract=parsed_row.contract_id, priority_score=parsed_row.priority_score
        ),
    )
    return ranked_applications
