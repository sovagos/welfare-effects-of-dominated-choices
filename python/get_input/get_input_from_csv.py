from dataclasses import dataclass
from typing import TypeVar, Callable, Any
from python.types import Input, Contract, Applicant, InitialApplicantStatus, Application

T = TypeVar("T")
K = TypeVar("K")


@dataclass
class ParsedRow:
    applicant_id: str
    rank: int
    priority_score: float
    contract_id: str
    capacity: int
    state_funded: bool
    program_id: str
    admitted: bool


@dataclass
class RawApplication:
    rank: int
    application: Application


@dataclass
class RawApplicant:
    id: str
    ranked_applications: list[RawApplication]


def get_input_from_csv(csv: list[dict]) -> Input:
    result: dict = _reduce(csv)
    return Input(
        applicants=_convert_raw_applicants_to_applicants(
            raw_applicants=[*result["raw_applicants"].values()]
        ),
        contracts=result["contracts"],
    )


def _reduce(items: list[dict]) -> dict:
    result: dict = {"raw_applicants": {}, "contracts": {}}
    for item in items:
        result = _accumulator(result, item)
    return result


def _accumulator(accumulated: dict, row: dict) -> dict:
    parsed_row = _get_parsed_row(row=row)
    return {
        "raw_applicants": _get_applicants(
            accumulated_applicants=accumulated["raw_applicants"], parsed_row=parsed_row
        ),
        "contracts": _get_contracts(
            accumulated_contracts=accumulated["contracts"], parsed_row=parsed_row
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
        admitted=row["admitted"] == "1",
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
    accumulated_applicants: dict[str, RawApplicant], parsed_row: ParsedRow
) -> dict[str, RawApplicant]:
    ranked_applications = _get_ranked_applications_with_new_application(
        ranked_applications=[]
        if parsed_row.applicant_id not in accumulated_applicants
        else accumulated_applicants[parsed_row.applicant_id].ranked_applications,
        parsed_row=parsed_row,
    )
    accumulated_applicants[parsed_row.applicant_id] = RawApplicant(
        id=parsed_row.applicant_id,
        ranked_applications=ranked_applications,
    )
    return accumulated_applicants


def _get_ranked_applications_with_new_application(
    ranked_applications: list[RawApplication], parsed_row: ParsedRow
) -> list[RawApplication]:
    return [
        *ranked_applications,
        RawApplication(
            rank=parsed_row.rank,
            application=Application(
                contract=parsed_row.contract_id,
                priority_score=parsed_row.priority_score,
                admitted=parsed_row.admitted,
            ),
        ),
    ]


def _convert_raw_applicants_to_applicants(
    raw_applicants: list[RawApplicant],
) -> list[Applicant]:
    return [
        _get_applicant_from_raw_applicant(raw_applicant=raw_applicant)
        for raw_applicant in raw_applicants
    ]


def _get_applicant_from_raw_applicant(raw_applicant: Any) -> Applicant:
    raw_ranked_applications = [*raw_applicant.ranked_applications]
    raw_ranked_applications.sort(key=lambda _: _.rank)
    return Applicant(
        status=InitialApplicantStatus(),
        id=raw_applicant.id,
        ranked_applications=[
            raw_application.application for raw_application in raw_ranked_applications
        ],
    )
