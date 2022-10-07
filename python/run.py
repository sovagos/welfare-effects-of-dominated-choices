from python.get_contracts_with_admitted_applicants.get_contracts_with_admitted_applicants import \
    get_contracts_with_admitted_applicants
from python.get_contracts_with_scores.get_contracts_with_scores import get_contracts_with_scores
from python.types import ContractWithScore, Contract, Applicant


def run(contracts: list[Contract], applicants: list[Applicant]) -> list[ContractWithScore]:
    contracts_with_admitted_applicants = get_contracts_with_admitted_applicants(contracts=contracts, applicants=applicants)
    return get_contracts_with_scores(contracts=contracts_with_admitted_applicants)