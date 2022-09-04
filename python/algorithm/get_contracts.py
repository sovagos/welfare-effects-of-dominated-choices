from python.algorithm.applicant import Applicant
from python.algorithm.contract import Contract, AdmittedApplicant
from python.algorithm.get_marginal_admitted_applicant import (
    get_marginal_admitted_applicant,
)
from python.algorithm.get_next_application import get_next_application
from python.algorithm.get_next_proposer import get_next_proposer
from python.algorithm.has_marginal_admitted_applicant import (
    has_marginal_admitted_applicant,
)
from python.algorithm.has_proposer import has_proposer


def get_contracts(
    applicants: list[Applicant], contracts: list[Contract]
) -> list[Applicant]:
    if not has_proposer(applicants=applicants):
        return applicants

    proposer = get_next_proposer(applicants=applicants)

    application = get_next_application(applicant=proposer)

    [proposed_contract] = [
        contract for contract in contracts if contract.id == application.contract
    ]

    contract_with_admitted_proposer = Contract(
        id=proposed_contract.id,
        capacity=proposed_contract.capacity,
        admitted_applicants=[
            *proposed_contract.admitted_applicants,
            AdmittedApplicant(
                applicant_id=proposer.id, priority_score=application.priority_score
            ),
        ],
    )

    if has_marginal_admitted_applicant(contract=contract_with_admitted_proposer):
        marginal_admitted_applicant = get_marginal_admitted_applicant(
            contract=contract_with_admitted_proposer
        )

    # Remove marginal admitted applicant from contract_with_admitted_proposer
    # Update contracts with the updated contract
    ## Contracts are updated

    # Update status of proposer to admitted in applicants
    # Update status of marginal admitted applicant to rejected/exhausted in applicants
    ## Applicants are updated
