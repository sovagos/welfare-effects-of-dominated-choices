from typing import TypeVar

from python.get_applicants.types import (
    Applicant,
    InitialApplicantStatus,
    AdmittedApplicantStatus,
    RejectedApplicantStatus,
    Application,
    Contract,
    AdmittedApplicant,
)
from tests.unit.helpers import get_random_string, get_random_int, get_random_float


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
