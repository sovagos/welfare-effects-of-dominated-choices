from typing import TypeVar

from python.get_contracts_with_admitted_applicants.get_contracts_with_admitted_applicants_rec import (
    get_contracts_with_admitted_applicants_rec,
)
from python.types import Applicant, Contract

T = TypeVar("T", Applicant, Contract)


def get_contracts_with_admitted_applicants(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[Contract]:
    return list(
        get_contracts_with_admitted_applicants_rec(
            applicants=_to_map_by_id(elements=applicants),
            contracts=_to_map_by_id(elements=contracts),
        ).values()
    )


def _to_map_by_id(elements: list[T]) -> dict[str, T]:
    return {element.id: element for element in elements}
