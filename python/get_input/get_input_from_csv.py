import datetime
from dataclasses import dataclass
from typing import Any, TypeVar, Callable
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


def get_input_from_csv(csv: list[dict]) -> Input:
    print("start parse", datetime.datetime.now())
    result: dict = _reduce(_accumulator, csv, {"applicants": {}, "contracts": {}})
    print("end parse", datetime.datetime.now())
    return Input(
        applicants=[*result["applicants"].values()],
        contracts=[*result["contracts"].values()],
    )


T = TypeVar("T")
K = TypeVar("K")


def _reduce(fn: Callable[[T, K], T], items: list[K], init: T) -> T:
    result = init
    for id, item in enumerate(items):
        result = fn(result, item)
    return result


def _accumulator(accumulated: dict, row: dict) -> dict:
    parsed_row = _get_parsed_row(row=row)
    return {
        "contracts": _get_contracts(
            accumulated_contracts=accumulated["contracts"], parsed_row=parsed_row
        ),
        "applicants": _get_applicants(
            accumulated_applicants=accumulated["applicants"], parsed_row=parsed_row
        ),
    }


def _get_parsed_row(row: dict) -> ParsedRow:
    return ParsedRow(
        applicant_id=row["applicant_id"],
        rank=int(row["rank"]),
        priority_score=float(row["priority_score"]),
        contract_id=row["contract_id"],
        capacity=int(row["capacity"]),
        state_funded=row["state_funded"] == "1",
        program_id=row["program_id"],
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
