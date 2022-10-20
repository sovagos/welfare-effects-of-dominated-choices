from typing import TypeVar

from python.get_matching.run_deferred_acceptance_rec import (
    run_deferred_acceptance_rec,
)
from python.types import Applicant, Contract, Applicants

T = TypeVar("T", Applicant, Contract)


def run_deferred_acceptance(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[Applicant]:
    result: Applicants = run_deferred_acceptance_rec(
        Applicants(proposer=applicants, admitted={}, exhausted=[]),
        _to_map_by_id(elements=contracts),
    )
    return [*result.admitted.values(), *result.exhausted]


def _to_map_by_id(elements: list[T]) -> dict[str, T]:
    return {element.id: element for element in elements}
