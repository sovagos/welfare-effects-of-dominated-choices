from typing import TypeVar

from python.get_applicants.get_applicants_rec import get_applicants_rec
from python.get_applicants.types import Applicant, Contract

T = TypeVar("T", Applicant, Contract)


def get_applicants(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[Applicant]:
    return list(
        get_applicants_rec(
            applicants=_to_map_by_id(elements=applicants),
            contracts=_to_map_by_id(elements=contracts),
        ).values()
    )


def _to_map_by_id(elements: list[T]) -> dict[T.id, T]:
    return {element.id: element for element in elements}
