from python.get_contracts.get_contracts_with_admitted_applicants import (
    get_contracts_with_admitted_applicants,
)
from python.get_contracts.get_contracts_with_scores import get_contracts_with_scores
from python.types import ContractWithPriorityScoreCutoff, Applicant, Contract


def get_contracts(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[ContractWithPriorityScoreCutoff]:
    return get_contracts_with_scores(
        contracts=get_contracts_with_admitted_applicants(
            contracts=contracts, applicants=applicants
        )
    )
