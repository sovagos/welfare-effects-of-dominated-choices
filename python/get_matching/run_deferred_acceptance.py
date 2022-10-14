from typing import TypeVar

from python.get_matching.run_deferred_acceptance_rec import (
    run_deferred_acceptance_rec,
)
from python.types import Applicant, Contract

T = TypeVar("T", Applicant, Contract)


def run_deferred_acceptance(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[Applicant]:
    return list(
        run_deferred_acceptance_rec(
            applicants=_to_map_by_id(elements=applicants),
            contracts=_to_map_by_id(elements=contracts),
        ).values()
    )


def _to_map_by_id(elements: list[T]) -> dict[str, T]:
    return {element.id: element for element in elements}
