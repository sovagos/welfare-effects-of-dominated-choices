from python.algorithm.applicant import (
    Applicant,
    ApplicantStatusType,
    RejectedApplicantStatus,
    AdmittedApplicantStatus,
)
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
from python.algorithm.remove_marginal_admitted_applicant import (
    remove_marginal_admitted_applicant,
)
from python.algorithm.update_applicants_with_proposer import (
    update_applicants_with_proposer,
)
from python.algorithm.update_contracts_with_proposed_contract import (
    update_contracts_with_proposed_contract,
)
from python.algorithm.update_marginal_admitted_applicant import (
    update_marginal_admitted_applicant,
)
from python.algorithm.update_proposer import update_proposer


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

    # Update status of proposer to admitted in applicants
    updated_proposer = update_proposer(applicant=proposer)
    applicants = update_applicants_with_proposer(
        applicants=applicants, proposer=updated_proposer
    )

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
        contract_without_marginal_admitted_applicant = (
            remove_marginal_admitted_applicant(
                contract=contract_with_admitted_proposer,
                marginal_admitted_applicant=marginal_admitted_applicant,
            )
        )
        # Update status of marginal admitted applicant to rejected/exhausted in applicants
        marginally_rejected_applicant = update_marginal_admitted_applicant(
            applicants=applicants,
            marginal_admitted_applicant=marginal_admitted_applicant,
        )
        applicants = update_applicants_with_proposer(
            applicants=applicants, proposer=marginally_rejected_applicant
        )
        ## Applicants are updated

    # Update contracts with the updated contract
    contracts = update_contracts_with_proposed_contract(
        contracts=contracts,
        proposed_contract=contract_without_marginal_admitted_applicant,
    )

    ## Contracts are updated
