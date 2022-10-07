from random import randint, random
from typing import TypeVar
from uuid import uuid4

from python.types import (
    Applicant,
    InitialApplicantStatus,
    Application,
    AdmittedApplicantStatus,
    RejectedApplicantStatus,
    Contract,
    AdmittedApplicant,
    ContractWithPriorityScoreCutoff, Input,
)


def get_random_string() -> str:
    return str(uuid4()).replace("-", "_")


def get_random_int() -> int:
    return randint(1, 20000)


def get_random_float() -> float:
    return random()


def create_applicant(override=None) -> Applicant:
    if not override:
        override = {}
    return Applicant(
        **{
            "id": get_random_string(),
            "ranked_applications": [],
            "status": InitialApplicantStatus(),
            **override,
        }
    )


def create_application(override=None) -> Application:
    if not override:
        override = {}
    return Application(
        **{
            "contract": get_random_string(),
            "priority_score": get_random_float(),
            **override,
        }
    )


def create_admitted_applicant_status(override=None) -> AdmittedApplicantStatus:
    if not override:
        override = {}
    return AdmittedApplicantStatus(**{"rank": get_random_int(), **override})


def create_rejected_applicant_status(override=None) -> RejectedApplicantStatus:
    if not override:
        override = {}
    return RejectedApplicantStatus(**{"rank": get_random_int(), **override})


def create_contract(override=None) -> Contract:
    if not override:
        override = {}
    return Contract(
        **{
            "id": get_random_string(),
            "capacity": get_random_int(),
            "program_id": get_random_string(),
            "state_funded": True,
            "admitted_applicants": [],
            **override,
        }
    )


def create_admitted_applicant(override=None) -> AdmittedApplicant:
    if not override:
        override = {}
    return AdmittedApplicant(
        **{
            "applicant_id": get_random_string(),
            "priority_score": get_random_float(),
            **override,
        }
    )


T = TypeVar("T", Applicant, Contract)


def to_map_by_id(elements: list[T]) -> dict[str, T]:
    return {element.id: element for element in elements}


def create_contract_with_priority_score_cutoff(override=None) -> ContractWithPriorityScoreCutoff:
    if not override:
        override = {}
    return ContractWithPriorityScoreCutoff(
        **{
            "id": get_random_string(),
            "priority_score_cutoff": get_random_int(),
            **override,
        }
    )

def create_input(override=None) -> Input:
    if not override:
        override = {}
    return Input(
        **{
            "contracts": [],
            "applicants": [],
            **override,
        }
    )
