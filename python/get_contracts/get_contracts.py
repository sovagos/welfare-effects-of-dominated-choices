from python.get_contracts.run_deferred_acceptance import (
    run_deferred_acceptance,
)
from python.get_contracts.get_contracts_with_scores import get_contracts_with_scores
from python.types import ContractWithPriorityScoreCutoff, Applicant, Contract


def get_contracts(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[ContractWithPriorityScoreCutoff]:
    return get_contracts_with_scores(
        contracts=run_deferred_acceptance(contracts=contracts, applicants=applicants)
    )
